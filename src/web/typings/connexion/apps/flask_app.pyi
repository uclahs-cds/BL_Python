"""
This type stub file was generated by pyright.
"""

import pathlib
import types
from typing import Any

from flask import json

from ..apis.flask_api import FlaskApi
from ..options import ConnexionOptions
from ..resolver import Resolver
from .abstract import AbstractApp

"""
This module defines a FlaskApp, a Connexion application to wrap a Flask application.
"""
logger = ...

class FlaskApp(AbstractApp):
    api_cls: FlaskApi
    app: FlaskApp

    def __init__(
        self,
        import_name: str,
        server: str = "flask",
        extra_files: list[str | pathlib.Path] | None = None,
        port: int | None = None,
        specification_dir: pathlib.Path | str = ...,
        host: str | None = None,
        server_args: dict[Any, Any] | None = None,
        arguments: dict[Any, Any] | None = None,
        auth_all_paths: bool = False,
        debug: bool | None = None,
        resolver: Resolver | types.FunctionType | None = None,
        options: ConnexionOptions = ...,
        skip_error_handlers: bool = False,
    ) -> None:
        """
        :param extra_files: additional files to be watched by the reloader, defaults to the swagger specs of added apis
        :type extra_files: list[str | pathlib.Path], optional

        See :class:`~connexion.AbstractApp` for additional parameters.
        """
        ...
    def create_app(self): ...
    def get_root_path(self): ...
    def set_errors_handlers(self): ...
    def common_error_handler(self, exception):  # -> Any | None:
        """
        :type exception: Exception
        """
        ...
    def add_api(
        self,
        specification: pathlib.Path | str | dict[Any, Any],
        base_path: str | None = None,
        arguments: dict[Any, Any] | None = None,
        auth_all_paths: bool | None = None,
        validate_responses: bool = False,
        strict_validation: bool = False,
        resolver: Resolver | types.FunctionType | None = None,
        resolver_error: int | None = None,
        pythonic_params: bool = False,
        pass_context_arg_name: str | None = None,
        options: dict[Any, Any] | None = None,
        validator_map: dict[Any, Any] | None = None,
    ) -> FlaskApi: ...
    def add_error_handler(
        self, error_code: int, function: types.FunctionType
    ) -> None: ...
    def run(
        self, port=..., server=..., debug=..., host=..., extra_files=..., **options
    ):  # -> None:
        """
        Runs the application on a local development server.

        :param host: the host interface to bind on.
        :type host: str
        :param port: port to listen to
        :type port: int
        :param server: which wsgi server to use
        :type server: str | None
        :param debug: include debugging information
        :type debug: bool
        :param extra_files: additional files to be watched by the reloader.
        :type extra_files: Iterable[str | pathlib.Path]
        :param options: options to be forwarded to the underlying server
        """
        ...

class FlaskJSONEncoder(json.JSONEncoder):
    def default(self, o): ...

class NumberConverter(werkzeug.routing.BaseConverter):
    """Flask converter for OpenAPI number type"""

    regex = ...
    def to_python(self, value): ...

class IntegerConverter(werkzeug.routing.BaseConverter):
    """Flask converter for OpenAPI integer type"""

    regex = ...
    def to_python(self, value): ...
