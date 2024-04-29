import logging as log
from abc import ABC
from functools import wraps
from logging import Logger
from typing import Any, Callable, ParamSpec, Protocol, Sequence, TypeVar, cast

from BL_Python.identity.config import Config
from BL_Python.identity.config import Config as RootSSOConfig
from BL_Python.identity.config import SAML2Config, SSOConfig
from BL_Python.platform.identity.user_loader import Role, UserId, UserLoader, UserMixin
from flask import Flask, Response
from flask_login import LoginManager as FlaskLoginManager
from flask_login import UserMixin as FlaskLoginUserMixin
from flask_login import current_user
from flask_login import login_required as flask_login_required
from injector import Injector, inject
from starlette.types import ASGIApp, Receive, Scope, Send
from typing_extensions import override


class _LoginUserMixin(FlaskLoginUserMixin, ABC):
    """Used strictly for typecasting. This matches the Protocol UserMixin in user_loader."""

    id: UserId
    roles: Sequence[Role]


class AuthCheckUser(Protocol):
    id: UserId
    roles: Sequence[Role]


class AuthCheckOverrideCallable(Protocol):
    def __call__(self, user: AuthCheckUser, *args: Any, **kwargs: Any) -> bool: ...


P = ParamSpec("P")
R = TypeVar("R")


def login_required(
    roles: Sequence[Role] | Callable[P, R] | Callable[..., Any] | None = None,
    auth_check_override: AuthCheckOverrideCallable | None = None,
):
    """
    Require a valid Flask session before calling the decorated function.

    This method uses the list of `roles` to determine whether the current session user
    has any of the roles listed. Alternatively, the use of `auth_check_override` can is used to
    bypass the role check. If the `auth_check_override` method returns True, the user is considered
    to have access to the decorated API endpoint. If the `auth_check_override` method returns False,
    `login_required` falls back to checking `roles`.

    If `roles` is a list, the user must have been assigned one of the roles specified.
    If `roles` is None, or if the decorator is not explicitly called, this will
    only require a valid Flask session regardless of the user's roles.

    If both `auth_check_override` and `roles` are None, this returns `flask_login.login_required`.
    Call this directly, rather than as a decorator.
    See https://flask-login.readthedocs.io/en/latest/#flask_login.login_required for more information.

    If `roles` is a callable and `auth_check_override` is None, this executes `flask_login.login_required` in its usual way.
    This is the same as using `flask_login.login_required` as a decorator.
    See https://flask-login.readthedocs.io/en/latest/#flask_login.login_required for more information.

    If `roles` is a list of User Roles and the current session user's roles intersect with `roles`,
    this returns True. If the current session user's roles do not intersect with `roles`, this returns False.

    If `auth_check_override` is a callable, it will be called with the following parameters:
        * `user` is the current session user
        * `*args` will be any arguments passed without argument keywords. When using `login_required` as a
          decorator, this will be an empty tuple.
        * `**kwargs` will be any parameters specified with keywords. When using `login_required` as a decorator,
          this will be the parameters passed into the decorated method.
          In the case of a Flask API endpoint, for example, this will be all of the endpoint method parameters.
    """

    if auth_check_override is None:
        if roles is None:
            return flask_login_required

        # In this case, `roles` is actually a function.
        # It is probably a decorated function.
        if callable(roles):
            return flask_login_required(roles)
    else:
        if not callable(auth_check_override):
            raise TypeError("Override must be a callable.")

    if not isinstance(roles, list):
        raise TypeError("Roles must be a list of User Roles.")

    login_manager = FlaskLoginManager()

    def wrapper(fn: Callable[P, R]) -> Callable[P, R | Response]:
        @wraps(fn)
        def decorated_view(*args: P.args, **kwargs: P.kwargs) -> R | Response:
            unauthorized = True
            try:
                user = cast(_LoginUserMixin, current_user)
                if not user.is_authenticated:
                    # this should end up raising a 401 exception
                    return login_manager.unauthorized()

                if callable(auth_check_override):
                    if auth_check_override(user, *args, **kwargs):
                        unauthorized = False

                # if authorization was overriden and successful, don't check roles
                if unauthorized:
                    if not isinstance(roles, list):  # pyright: ignore[reportUnnecessaryIsInstance]
                        # this should end up raising a 401 exception
                        return login_manager.unauthorized()

                    # if roles is empty, no roles will intersect.
                    # this means an empty list means "no roles have access"
                    role_intersection = [
                        role for role in user.roles if role in (roles or [])
                    ]
                    if len(role_intersection) == 0:
                        # this should end up raising a 401 exception
                        return login_manager.unauthorized()
            except Exception as e:
                log.exception(e)
                # this should end up raising a 401 exception
                return login_manager.unauthorized()

            return fn(*args, **kwargs)

        return decorated_view

    return wrapper


import logging
from dataclasses import dataclass
from logging import Logger
from typing import Any, Dict, cast
from urllib.parse import urlparse

import flask_login
from flask import Blueprint, current_app, redirect, request, session, url_for
from flask.helpers import make_response
from flask.wrappers import Response

# fmt: off
# isort: off
from flask_login import login_user, logout_user # pyright: ignore[reportUnknownVariableType]
# isort: on
from BL_Python.identity.SAML2 import SAML2Client
from BL_Python.platform.identity.user_loader import UserId, UserLoader
from BL_Python.web.config import Config
from BL_Python.web.encryption import decrypt_flask_cookie

# fmt: on
from injector import inject
from saml2.validate import (
    MustValueError,
    NotValid,
    OutsideCardinality,
    ResponseLifetimeExceed,
    ShouldValueError,
    ToEarly,
)
from werkzeug.exceptions import BadRequest, Forbidden, Unauthorized


class SSOBlueprint:
    sso_blueprint: Blueprint

    def __init__(self) -> None:
        super().__init__()
        # https://github.com/jpf/okta-pysaml2-example/blob/master/app.py
        self.sso_blueprint = Blueprint("sso", __name__, url_prefix="/saml")
        self._SSOBlueprint(self.sso_blueprint)

    @dataclass(frozen=True)
    class _SessionValueNames:
        USERNAME = "username"
        AUTHENTICATED = "authenticated"
        USER_ID = "user_id"

    SESSION_VALUE_NAMES = _SessionValueNames()

    @staticmethod
    @inject
    def user(log: Logger):
        user = flask_login.current_user
        userId: UserId = user.id
        username = userId.username
        log.debug(f"Flask current user is {username}")
        return {"username": username}

    @staticmethod
    def apikey_auth(token: str, required_scopes: Any):
        """
        This is used by Connexion to authorize requests. It is specified in API-v1.yaml.
        `token` is the value passed either through Connexion ingesting the `session` cookie,
        or through the manually set value in the Swagger UI. The `session` cookie is available
        after authenticating.
        """
        log = logging.getLogger("connexion")

        session_data: Dict[str, Any]
        try:
            session_data = decrypt_flask_cookie(current_app.config["SECRET_KEY"], token)  # pyright: ignore[reportUnknownArgumentType]
            # under normal circumstances these session objects are equivalent.
            # The values will not be equivalent if the cookie is expired and
            # the browser did not send the `session` cookie, but Swagger UI did.
            if session_data["_id"] == session["_id"]:
                log.info("Connexion request has a valid session.")
                return SSOBlueprint.user(log)
        except Exception as e:
            log.error(e)

        log.info("Connexion request is unauthorized.")
        raise Unauthorized()

    @staticmethod
    def _delete_username_cookie(response: Response, log: Logger):
        response.delete_cookie(SSOBlueprint.SESSION_VALUE_NAMES.USERNAME)

        # `delete_cookie` doesn't have parameters for "Secure" or "SameSite,"
        # so we add them below.
        headers = response.headers.get("Set-Cookie")
        if headers is None:
            log.error(
                "Headers is empty, but was expected in order to correctly log out a user.\
        The user's browser will retain the `username` cookie."
            )
            return response

        # Using a dict as an ordered set so the cookie contains only unique parts.
        header_parts = dict.fromkeys([
            header_part.strip() for header_part in headers.split(";")
        ])
        header_parts["Secure"] = None
        header_parts["SameSite=None"] = None
        response.headers.set("Set-Cookie", "; ".join(header_parts.keys()))
        return response

    def _SSOBlueprint(self, sso_blueprint: Blueprint):
        @sso_blueprint.route("/user")
        @flask_login_required
        @inject
        def user(log: Logger):
            return SSOBlueprint.user(log)

        @sso_blueprint.route("/logout")
        @flask_login_required
        @inject
        def logout(log: Logger):
            log.info(f"Logging out user {flask_login.current_user}")
            logout_user()
            response = make_response('{"status_code": 200, "status": "200 OK"}', 200)
            response.headers["Content-Type"] = "application/json"

            return SSOBlueprint._delete_username_cookie(response, log)

        @sso_blueprint.route("/login/<idp_name>")
        @inject
        def sp_initiated(
            idp_name: str, cap_saml2: SAML2Client, config: SSOConfig, log: Logger
        ):
            redirect_url = cap_saml2.prepare_user_authentication(
                relay_state=cast(SAML2Config, config.settings).relay_state
            )

            log.info(f"Redirecting client to {redirect_url} for IDP {idp_name}")
            response = redirect(redirect_url, code=302)

            response.headers["Cache-Control"] = "no-cache, no-store"
            response.headers["Pragma"] = "no-cache"
            return response

        @sso_blueprint.route("/login/<idp_name>", methods=["POST"])
        @inject
        def idp_initiated(
            idp_name: str,
            cap_saml2: SAML2Client,
            user_loader: UserLoader[UserMixin[Role]],
            config: Config,
            log: Logger,
        ):
            log.info(f"Trying to log in from SAML2 response for IDP {idp_name}")
            saml_response: str = request.form["SAMLResponse"]

            user: UserMixin[Role] | None = None
            try:
                (username, _) = cap_saml2.handle_user_login(saml_response)
                log.info(f"Login username is {username}")
                # FIXME should enable a way to set the default role here?
                user = user_loader.user_loader(username, None, True)
                if user is None:
                    raise
            except (
                NotValid,
                MustValueError,
                OutsideCardinality,
                ResponseLifetimeExceed,
                ShouldValueError,
                ToEarly,
            ) as e:
                log.exception(e)
                raise BadRequest("SAML2 Response is invalid.")

            session_duration = (
                config.flask.session.lifetime
                if config.flask and config.flask.session
                else None
            )

            login_user(user, remember=False, duration=session_duration)

            session[SSOBlueprint.SESSION_VALUE_NAMES.AUTHENTICATED] = True
            session[SSOBlueprint.SESSION_VALUE_NAMES.USERNAME] = user.id.username
            session[SSOBlueprint.SESSION_VALUE_NAMES.USER_ID] = user.id.user_id
            log.info(f"Login for user {user.id.user_id} succeeded")

            url: str = ""
            if "RelayState" in request.form:
                redirect_url: str = request.form["RelayState"]
                expected_url = cast(
                    SAML2Config, cast(RootSSOConfig, config).sso.settings
                ).relay_state
                parsed_redirect_url = urlparse(redirect_url)
                parsed_expected_url = urlparse(expected_url)
                if (
                    parsed_redirect_url.scheme != parsed_expected_url.scheme
                    or parsed_redirect_url.netloc != parsed_expected_url.netloc
                ):
                    log.error(
                        f'Parsed URL "{redirect_url}" does not match expected URL "{expected_url}"'
                    )
                    raise Forbidden()
                url: str = request.form["RelayState"]
                log.info(f'SAML2 response has RelayState="{url}"')

            if url == "":
                url = url_for("sso.user")
                log.info(
                    f"SAML2 response does not have RelayState. Redirecting client to {url}"
                )

            response = redirect(url)

            response.set_cookie(
                "username",
                str(user.id.username),
                samesite="None",
                secure=True,
                httponly=False,
                max_age=session_duration,
            )
            return response

        # @sso_blueprint.before_app_request  # pyright: ignore[reportUntypedFunctionDecorator]
        @inject
        def make_session_permanent(config: Config):
            session.permanent = (
                config.flask.session.permanent
                if config.flask and config.flask.session
                else False
            )

        # FIXME these after_app_requests need to be made middleware
        # @sso_blueprint.after_app_request  # pyright: ignore[reportUntypedFunctionDecorator]
        @inject
        def remove_username_cookie_without_session(response: Response, log: Logger):
            # if the session has expired but the client still has the username cookie,
            # the username cookie needs to be cleared from the client
            if not session.get(  # pyright: ignore[reportUnknownMemberType]
                SSOBlueprint.SESSION_VALUE_NAMES.AUTHENTICATED
            ) and request.cookies.get(SSOBlueprint.SESSION_VALUE_NAMES.USERNAME):
                log.info("Session expired; clearing username cookie.")
                return SSOBlueprint._delete_username_cookie(response, log)

            return response


# TODO this should probably be moved into the tests
class LoginManager(FlaskLoginManager):
    @inject
    def __init__(
        self,
        user_loader: UserLoader[UserMixin[Role]],
        app: Flask,
        log: Logger,
        add_context_processor: bool = True,
    ):
        super().__init__(app=app, add_context_processor=add_context_processor)

        self._app = app
        self._log = log

        user_loader_lambda: Callable[[str], UserMixin[Role] | None] = (
            lambda username: user_loader.user_loader(username, None)
        )
        _ = self.user_loader(user_loader_lambda)
        self.init_app(app)

    @override
    def unauthorized(self):
        """
        Raises an `Unauthorized` exception.
        """
        saml_idp_url = url_for("sso.sp_initiated", idp_name="okta", _external=True)
        self._log.debug(
            f"Redirecting unauthenticated client to {saml_idp_url} from {request.url}"
        )
        response: Response = self._app.make_response((
            "Unauthorized",
            401,
            {
                "Content-Type": "text/plain; charset=utf-8",
                # Clients can access this IDP URL to authenticate and POST back with a valid SAML request.
                "Location": saml_idp_url,
                # "SAML" isn't in the HTTP standard, but it's the only auth method supported by CAP.
                "WWW-Authenticate": 'SAML realm="Authenticate with the SAML IDP at the URL provided by Location.", charset="UTF-8"',
                "Access-Control-Expose-Headers": "Location, WWW-Authenticate",
            },
        ))
        raise Unauthorized(response.data, response)


class SAML2Middleware:
    _app: ASGIApp

    def __init__(self, app: ASGIApp):
        super().__init__()
        self._app = app

    @inject
    async def __call__(
        self,
        scope: Scope,
        receive: Receive,
        send: Send,
        app: Flask,
        injector: Injector,
        log: Logger,
    ) -> None:
        async def wrapped_send(message: Any) -> None:
            nonlocal scope
            nonlocal receive
            nonlocal send
            nonlocal app

            # Only run during startup of the application
            if (
                scope["type"] != "lifespan"
                or message["type"] != "lifespan.startup.complete"
                or not scope["app"]
            ):
                return await send(message)

            log.debug("Registering SSO blueprint.")
            app.register_blueprint(SSOBlueprint().sso_blueprint)
            # trigger side-effect - adds login_manager to app
            _ = injector.get(LoginManager)
            log.debug("SSO blueprint registered and LoginManager installed.")
            return await send(message)

        await self._app(scope, receive, wrapped_send)
