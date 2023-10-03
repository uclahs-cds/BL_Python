"""
This type stub file was generated by pyright.
"""

import abc
import pathlib
import types
from typing import Any

from ..options import ConnexionOptions
from ..resolver import Resolver

"""
This module defines an AbstractApp, which defines a standardized user interface for a Connexion
application.
"""
logger = ...

class AbstractApp(metaclass=abc.ABCMeta):
    port: int | None = None
    host: str | None = None
    debug: bool | None = None
    resolver: Resolver | types.FunctionType | None = None
    import_name: str = ...
    arguments: dict[Any, Any] | None = ...
    api_cls: type[AbstractApp] = ...
    resolver_error: int | None = None
    auth_all_paths: bool = False
    options: ConnexionOptions
    server: str | None = None
    server_args: dict[Any, Any] | None = None
    app: type = ...
    root_path: pathlib.Path = ...
    specification_dir: pathlib.Path | str = ...

    def __init__(
        self,
        import_name: str,
        api_cls: type[AbstractApp],
        port: int | None = None,
        specification_dir: pathlib.Path | str = ...,
        host: str | None = None,
        server: str | None = None,
        server_args: dict[Any, Any] | None = None,
        arguments: dict[Any, Any] | None = None,
        auth_all_paths: bool = False,
        debug: bool | None = None,
        resolver: Resolver | types.FunctionType | None = None,
        options: ConnexionOptions = ...,
        skip_error_handlers: bool = False,
    ) -> None:
        """
        :param import_name: the name of the application package
        :type import_name: str
        :param host: the host interface to bind on.
        :type host: str
        :param port: port to listen to
        :type port: int
        :param specification_dir: directory where to look for specifications
        :type specification_dir: pathlib.Path | str
        :param server: which wsgi server to use
        :type server: str | None
        :param server_args: dictionary of arguments which are then passed to appropriate http server (Flask or aio_http)
        :type server_args: dict | None
        :param arguments: arguments to replace on the specification
        :type arguments: dict | None
        :param auth_all_paths: whether to authenticate not defined paths
        :type auth_all_paths: bool
        :param debug: include debugging information
        :type debug: bool
        :param resolver: Callable that maps operationID to a function
        """
        ...
    @abc.abstractmethod
    def create_app(self):  # -> None:
        """
        Creates the user framework application
        """
        ...
    @abc.abstractmethod
    def get_root_path(self):  # -> None:
        """
        Gets the root path of the user framework application
        """
        ...
    @abc.abstractmethod
    def set_errors_handlers(self):  # -> None:
        """
        Sets all errors handlers of the user framework application
        """
        ...
    def add_api(
        self,
        specification,
        base_path=...,
        arguments=...,
        auth_all_paths=...,
        validate_responses=...,
        strict_validation=...,
        resolver=...,
        resolver_error=...,
        pythonic_params=...,
        pass_context_arg_name=...,
        options=...,
        validator_map=...,
    ):
        """
        Adds an API to the application based on a swagger file or API dict

        :param specification: swagger file with the specification | specification dict
        :type specification: pathlib.Path or str or dict
        :param base_path: base path where to add this api
        :type base_path: str | None
        :param arguments: api version specific arguments to replace on the specification
        :type arguments: dict | None
        :param auth_all_paths: whether to authenticate not defined paths
        :type auth_all_paths: bool
        :param validate_responses: True enables validation. Validation errors generate HTTP 500 responses.
        :type validate_responses: bool
        :param strict_validation: True enables validation on invalid request parameters
        :type strict_validation: bool
        :param resolver: Operation resolver.
        :type resolver: Resolver | types.FunctionType
        :param resolver_error: If specified, turns ResolverError into error
            responses with the given status code.
        :type resolver_error: int | None
        :param pythonic_params: When True CamelCase parameters are converted to snake_case
        :type pythonic_params: bool
        :param options: New style options dictionary.
        :type options: dict | None
        :param pass_context_arg_name: Name of argument in handler functions to pass request context to.
        :type pass_context_arg_name: str | None
        :param validator_map: map of validators
        :type validator_map: dict
        :rtype: AbstractAPI
        """
        ...
    def add_url_rule(self, rule, endpoint=..., view_func=..., **options):  # -> None:
        """
        Connects a URL rule.  Works exactly like the `route` decorator.  If a view_func is provided it will be
        registered with the endpoint.

        Basically this example::

            @app.route('/')
            def index():
                pass

        Is equivalent to the following::

            def index():
                pass
            app.add_url_rule('/', 'index', index)

        If the view_func is not provided you will need to connect the endpoint to a view function like so::

            app.view_functions['index'] = index

        Internally`route` invokes `add_url_rule` so if you want to customize the behavior via subclassing you only need
        to change this method.

        :param rule: the URL rule as string
        :type rule: str
        :param endpoint: the endpoint for the registered URL rule. Flask itself assumes the name of the view function as
                         endpoint
        :type endpoint: str
        :param view_func: the function to call when serving a request to the provided endpoint
        :type view_func: types.FunctionType
        :param options: the options to be forwarded to the underlying `werkzeug.routing.Rule` object.  A change
                        to Werkzeug is handling of method options. methods is a list of methods this rule should be
                        limited to (`GET`, `POST` etc.).  By default a rule just listens for `GET` (and implicitly
                        `HEAD`).
        """
        ...
    def route(self, rule, **options):
        """
        A decorator that is used to register a view function for a
        given URL rule.  This does the same thing as `add_url_rule`
        but is intended for decorator usage::

            @app.route('/')
            def index():
                return 'Hello World'

        :param rule: the URL rule as string
        :type rule: str
        :param endpoint: the endpoint for the registered URL rule.  Flask
                         itself assumes the name of the view function as
                         endpoint
        :param options: the options to be forwarded to the underlying `werkzeug.routing.Rule` object.  A change
                        to Werkzeug is handling of method options.  methods is a list of methods this rule should be
                        limited to (`GET`, `POST` etc.).  By default a rule just listens for `GET` (and implicitly
                        `HEAD`).
        """
        ...
    @abc.abstractmethod
    def run(self, port=..., server=..., debug=..., host=..., **options):  # -> None:
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
        :param options: options to be forwarded to the underlying server
        """
        ...
    def __call__(self, environ, start_response):
        """
        Makes the class callable to be WSGI-compliant. As Flask is used to handle requests,
        this is a passthrough-call to the Flask callable class.
        This is an abstraction to avoid directly referencing the app attribute from outside the
        class and protect it from unwanted modification.
        """
        ...
