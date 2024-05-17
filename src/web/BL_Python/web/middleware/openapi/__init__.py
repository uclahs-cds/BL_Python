import re
import uuid
from contextlib import ExitStack
from contextvars import Token
from logging import Logger
from typing import Any, Awaitable, Callable, Literal, TypeVar, cast
from uuid import uuid4

import json_logging
from BL_Python.programming.collections.dict import AnyDict, merge
from connexion import ConnexionMiddleware, FlaskApp, context, utils
from connexion.middleware import MiddlewarePosition
from flask import Flask, Request, Response, request
from flask.ctx import AppContext
from flask.globals import _cv_app  # pyright: ignore[reportPrivateUsage]
from flask.globals import current_app
from flask.typing import (
    AfterRequestCallable,
    BeforeRequestCallable,
    ResponseReturnValue,
)
from injector import inject
from starlette.types import ASGIApp, Receive, Scope, Send
from typing_extensions import TypedDict, final

from ...config import Config
from ..consts import (
    CONTENT_SECURITY_POLICY_HEADER,
    CORRELATION_ID_HEADER,
    INCOMING_REQUEST_MESSAGE,
    OUTGOING_RESPONSE_MESSAGE,
    REQUEST_COOKIE_HEADER,
    RESPONSE_COOKIE_HEADER,
)

# pyright: reportUnusedFunction=false


# Fixes type problems when using @inject with @app.before_request and @app.after_request.
# The main difference with these types as opposed to the Flask-defined types is that
# these types allow the handler to take any arguments, versus no arguments or just Response.
AfterRequestCallable = Callable[..., Response] | Callable[..., Awaitable[Response]]
BeforeRequestCallable = (
    Callable[..., ResponseReturnValue | None]
    | Callable[..., Awaitable[ResponseReturnValue | None]]
)
T_request_callable = TypeVar(
    "T_request_callable", bound=BeforeRequestCallable | AfterRequestCallable | None
)
# Fixes type problems when using Flask-Injector, which automatically sets up any bound
# error handlers. The error handler types in Flask have the same problem as After/BeforeRequestCallable
# in that their parameters are `[Any]` rather than `...`. This relaxes that. The type
# is valid here because Flask-Injector does actually include the provided types as parameters.
ErrorHandlerCallable = (
    Callable[..., ResponseReturnValue] | Callable[..., Awaitable[ResponseReturnValue]]
)
T_error_handler = TypeVar("T_error_handler", bound=ErrorHandlerCallable)

TFlaskApp = Flask | FlaskApp
T_flask_app = TypeVar("T_flask_app", bound=TFlaskApp)


MiddlewareRequestDict = TypedDict(
    "MiddlewareRequestDict",
    {
        "type": Literal["http"],
        "http_version": str,
        "method": Literal[
            "GET",
            "POST",
            "PATCH",
            "PUT",
            "DELETE",
            "OPTIONS",
            "HEAD",
            "CONNECT",
            "TRACE",
        ],
        "path": str,
        "raw_path": bytes,
        "root_path": str,
        "scheme": str,
        "query_string": bytes,
        "headers": list[tuple[bytes, bytes]],
        "client": list[
            str | int
        ],  # this is actually a 2-item list whose first item is a str and second item is an int
        "server": list[str | int],  # same here
        "extensions": dict[str, dict[str, str]],
        "state": AnyDict,
        "app": ConnexionMiddleware,
        "starlette.exception_handlers": tuple[
            dict[type[Any], Callable[..., Any]], dict[Any, Any]
        ],
        "path_params": dict[Any, Any],
    },
)

MiddlewareResponseDict = TypedDict(
    "MiddlewareResponseDict",
    {
        "type": Literal["http.response.start"],
        "status": int,
        "headers": list[tuple[bytes, bytes]],
    },
)


def _get_correlation_id(
    request: MiddlewareRequestDict, response: MiddlewareResponseDict, log: Logger
) -> str:
    correlation_id = _get_correlation_id_from_json_logging(response, log)

    if not correlation_id:
        correlation_id = _get_correlation_id_from_headers(request, response, log)

    return correlation_id


def _get_correlation_id_from_headers(
    request: MiddlewareRequestDict, response: MiddlewareResponseDict, log: Logger
) -> str:
    try:
        headers = _headers_as_dict(request)
        correlation_id = headers.get(CORRELATION_ID_HEADER.lower())

        if not correlation_id:
            headers = _headers_as_dict(response)
            correlation_id = headers.get(CORRELATION_ID_HEADER.lower())

        if correlation_id:
            # validate format
            _ = uuid.UUID(correlation_id)
        else:
            correlation_id = str(uuid4())
            log.info(
                f'Generated new UUID "{correlation_id}" for {CORRELATION_ID_HEADER} request header.'
            )

        return correlation_id

    except ValueError as e:
        log.warning(f"Badly formatted {CORRELATION_ID_HEADER} received in request.")
        raise e


def _get_correlation_id_from_json_logging(
    request_response: MiddlewareRequestDict | MiddlewareResponseDict, log: Logger
) -> str | None:
    correlation_id: None | str
    try:
        correlation_id = json_logging.get_correlation_id(request_response)
        # validate format
        _ = uuid.UUID(correlation_id)
        return correlation_id
    except ValueError as e:
        log.warning(f"Badly formatted {CORRELATION_ID_HEADER} received in request.")
        raise e
    except Exception as e:
        log.debug(
            f"Error received when getting {CORRELATION_ID_HEADER} header from `json_logging`. Possibly `json_logging` is not configured, and this is not an error.",
            exc_info=e,
        )


def _headers_as_dict(
    request_response: MiddlewareRequestDict | MiddlewareResponseDict,
):
    if (
        isinstance(request_response, dict)  # pyright: ignore[reportUnnecessaryIsInstance]
        and "headers" in request_response.keys()
    ):
        # FIXME does this work for a middleware _response_ as well?
        return {
            key: value for (key, value) in decode_headers(request_response["headers"])
        }
    else:
        raise Exception("Unable to extract headers from request when logging request.")


@inject
def _log_all_api_requests(
    request: MiddlewareRequestDict,
    response: MiddlewareResponseDict,
    config: Config,
    log: Logger,
):
    request_headers_safe: dict[str, str] = _headers_as_dict(request)

    correlation_id = _get_correlation_id(request, response, log)

    if (
        request_headers_safe.get(REQUEST_COOKIE_HEADER)
        and config.flask
        and config.flask.session
    ):
        request_headers_safe[REQUEST_COOKIE_HEADER] = re.sub(
            rf"({config.flask.session.cookie.name}=)[^;]+(;|$)",
            r"\1<redacted>\2",
            request_headers_safe[REQUEST_COOKIE_HEADER],
        )

    server = request.get("server")
    client = request.get("client")
    log.info(
        INCOMING_REQUEST_MESSAGE,
        request["method"],
        request["path"],
        # ASGI spec states `server` and `client`
        # can be `None` if not available.
        f"{server[0]}:{server[1]}" if server else "None",
        f"{client[0]}:{client[1]}" if client else "None",
        request.get("remote_user"),  # FIXME fix this when auth is done
        extra={
            "props": {
                "correlation_id": correlation_id,
                "headers": request_headers_safe,
            }
        },
    )


def _wrap_all_api_responses(
    request: MiddlewareRequestDict,
    response: MiddlewareResponseDict,
    config: Config,
    log: Logger,
):
    correlation_id = _get_correlation_id(request, response, log)
    response_headers = _headers_as_dict(response)

    response_headers[CORRELATION_ID_HEADER] = correlation_id

    if config.web.security.csp:
        response_headers[CONTENT_SECURITY_POLICY_HEADER] = config.web.security.csp

    # if config.flask and config.flask.openapi and config.flask.openapi.use_swagger:
    #    # Use a permissive CSP for the Swagger UI
    #    # https://github.com/swagger-api/swagger-ui/issues/7540
    #    FIXME what to use other than `request` w/ Connexion middleware?
    #    if request.path.startswith("/ui/") or (
    #        request.url_rule and request.url_rule.endpoint == "/v1./v1_swagger_ui_index"
    #    ):
    #        response.headers[
    #            CONTENT_SECURITY_POLICY_HEADER
    #        ] = "default-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self'; script-src 'self' 'unsafe-inline'"


def _log_all_api_responses(
    request: MiddlewareRequestDict,
    response: MiddlewareResponseDict,
    config: Config,
    log: Logger,
):
    response_headers_safe: dict[str, str] = _headers_as_dict(response)

    correlation_id = _get_correlation_id(request, response, log)

    if (
        response_headers_safe.get(RESPONSE_COOKIE_HEADER)
        and config.flask
        and config.flask.session
    ):
        response_headers_safe[RESPONSE_COOKIE_HEADER] = re.sub(
            rf"({config.flask.session.cookie.name}=)[^;]+(;|$)",
            r"\1<redacted>\2",
            response_headers_safe[RESPONSE_COOKIE_HEADER],
        )

    log.info(
        OUTGOING_RESPONSE_MESSAGE,
        response["status"],
        response["status"],
        extra={
            "props": {
                "correlation_id": correlation_id,
                "headers": response_headers_safe,
            }
        },
    )


def decode_headers(headers: list[tuple[bytes, bytes]]):
    content_type = utils.extract_content_type(headers)
    _, encoding = utils.split_content_type(content_type)
    if encoding is None:
        encoding = "utf-8"

    decoded_headers = [
        (header.decode(encoding), value.decode(encoding)) for (header, value) in headers
    ]

    return decoded_headers


def encode_headers(
    headers: list[tuple[bytes, bytes]],
    append_headers: list[tuple[str, str]],
    encoding: str = "utf-8",
):
    for header, value in append_headers:
        headers.append((header.encode(encoding), value.encode(encoding)))


class RequestLoggerMiddleware:
    _app: ASGIApp

    def __init__(self, app: ASGIApp):
        super().__init__()
        self._app = app

    @inject
    async def __call__(
        self, scope: Scope, receive: Receive, send: Send, config: Config, log: Logger
    ) -> None:
        async def wrapped_send(message: Any) -> None:
            nonlocal scope
            nonlocal receive
            nonlocal send

            if message["type"] != "http.response.start":
                return await send(message)

            response = cast(MiddlewareResponseDict, scope)
            request = cast(MiddlewareRequestDict, scope)

            _log_all_api_requests(request, response, config, log)

            return await send(message)

        await self._app(scope, receive, wrapped_send)


class ResponseLoggerMiddleware:
    _app: ASGIApp

    def __init__(self, app: ASGIApp):
        super().__init__()
        self._app = app

    @inject
    async def __call__(
        self, scope: Scope, receive: Receive, send: Send, config: Config, log: Logger
    ) -> None:
        async def wrapped_send(message: Any) -> None:
            nonlocal scope
            nonlocal receive
            nonlocal send

            if message["type"] != "http.response.start":
                return await send(message)

            request = cast(MiddlewareRequestDict, scope)
            response = cast(MiddlewareResponseDict, message)

            _log_all_api_responses(request, response, config, log)
            _wrap_all_api_responses(request, response, config, log)

            return await send(message)

        await self._app(scope, receive, wrapped_send)


class CorrelationIDMiddleware:
    _app: ASGIApp

    def __init__(self, app: ASGIApp):
        super().__init__()
        self._app = app

    @inject
    async def __call__(
        self, scope: Scope, receive: Receive, send: Send, log: Logger
    ) -> None:
        async def wrapped_send(message: Any) -> None:
            nonlocal scope
            nonlocal send

            if message["type"] != "http.response.start":
                return await send(message)

            request = cast(MiddlewareRequestDict, scope)
            response = cast(MiddlewareResponseDict, message)

            response_headers = response["headers"]
            content_type = utils.extract_content_type(response_headers)
            _, encoding = utils.split_content_type(content_type)
            if encoding is None:
                encoding = "utf-8"

            request_headers = request["headers"]
            try:
                correlation_id_header_encoded = CORRELATION_ID_HEADER.lower().encode(
                    encoding
                )

                request_correlation_id: bytes | None = next(
                    (
                        correlation_id
                        for (header, correlation_id) in request_headers
                        if header == correlation_id_header_encoded
                    ),
                    None,
                )

                if request_correlation_id:
                    # validate format
                    _ = uuid.UUID(request_correlation_id.decode(encoding))
                else:
                    request_correlation_id = str(uuid4()).encode(encoding)
                    request_headers.append((
                        correlation_id_header_encoded,
                        request_correlation_id,
                    ))
                    log.info(
                        f'Generated new UUID "{request_correlation_id}" for {CORRELATION_ID_HEADER} request header.'
                    )

                response_headers.append((
                    correlation_id_header_encoded,
                    request_correlation_id,
                ))

                return await send(message)
            except ValueError as e:
                log.warning(
                    f"Badly formatted {CORRELATION_ID_HEADER} received in request."
                )
                raise e

        await self._app(scope, receive, wrapped_send)


@final
class FlaskContextMiddleware:
    """
    Connexion does not set Flask contexts in all cases they may be needed, like
    in middlewares that execute before ContextMiddleware. This middleware creates
    the Flask application, request, and session contexts if they are not currently set.
    """

    def __init__(
        self,
        app: ASGIApp,
    ) -> None:
        self.app = app

    @inject
    async def __call__(
        self, scope: Scope, receive: Receive, send: Send, app: Flask
    ) -> None:
        receive_token: Token[Receive] | None = None
        scope_token: Token[Scope] | None = None
        app_ctx_token: Token[AppContext] | None = None

        try:
            receive_token = context._receive.set(receive)  # pyright: ignore[reportPrivateUsage]
            scope_token = context._scope.set(scope)  # pyright: ignore[reportPrivateUsage]

            if scope["type"] not in ["http", "websocket"]:
                await self.app(scope, receive, send)
                return

            with ExitStack() as exit_stack:
                if not isinstance(current_app, Flask):  # pyright: ignore[reportUnnecessaryIsInstance] it is not a Flask if it is not set
                    app_ctx = exit_stack.enter_context(app.app_context())

                    app_ctx_token = _cv_app.set(app_ctx)

                if not isinstance(request, Request):  # pyright: ignore[reportUnnecessaryIsInstance] it is not a Request if it is not set
                    request_environ = merge(
                        {
                            "PATH_INFO": scope.get("path")
                            or context.request._starlette_request.url.path,
                            "wsgi.url_scheme": scope.get("scheme")
                            or context.request._starlette_request.url.scheme,
                            "REQUEST_METHOD": scope.get("method")
                            or context.request._starlette_request.method,
                            # there is the possibility this value in scope is "127.0.0.1" when using "localhost"
                            # which is not consistent with the _starlette_request value.
                            "SERVER_NAME": (
                                scope["server"][0]
                                if scope.get("server")
                                else context.request._starlette_request.base_url.hostname
                            ),
                            "SERVER_PORT": (
                                scope["server"][1]
                                if scope.get("server")
                                else context.request._starlette_request.base_url.port
                            ),
                            "QUERY_STRING": scope.get("query_string")
                            or context.request._starlette_request.url.query,
                            "REMOTE_ADDR": ":".join([
                                str(value) for value in scope["client"]
                            ])
                            or f"{context.request._starlette_request.client.host}:{context.request._starlette_request.client.port}",
                        },
                        dict({
                            (
                                f"{'HTTP_' if header.upper() not in ['CONTENT_TYPE', 'CONTENT_LENGTH'] else ''}{header.upper().replace('-', '_')}",
                                value,
                            )
                            for header, value in context.request.headers.items()
                        }),
                    )

                    # Some values, like the query string, are stored as bytes.
                    # Decode as a UTF-8 str so encoding later doesn't fail.
                    for key, value in request_environ.items():
                        if isinstance(value, bytes):
                            request_environ[key] = value.decode("utf-8")

                    request_ctx = exit_stack.enter_context(
                        app.request_context(request_environ)
                    )
                    request_ctx.push()

                await self.app(scope, receive, send)

        finally:
            if app_ctx_token is not None:
                _cv_app.reset(app_ctx_token)
            if receive_token is not None:
                context._receive.reset(receive_token)  # pyright: ignore[reportPrivateUsage]
            if scope_token is not None:
                context._scope.reset(scope_token)  # pyright: ignore[reportPrivateUsage]


def register_openapi_api_request_handlers(app: FlaskApp):
    app.add_middleware(RequestLoggerMiddleware)


def register_openapi_api_response_handlers(app: FlaskApp):
    app.add_middleware(CorrelationIDMiddleware)
    app.add_middleware(ResponseLoggerMiddleware)


def register_openapi_context_middleware(app: FlaskApp):
    app.add_middleware(FlaskContextMiddleware, MiddlewarePosition.BEFORE_EXCEPTION)
