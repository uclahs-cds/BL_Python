"""
This type stub file was generated by pyright.
"""

import functools
from inspect import ismethod
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    TypeVar,
    Union,
    cast,
    get_type_hints,
)

import flask
import flask_restx
from flask import Config, Request
from flask_restful import Api as FlaskRestfulApi
from flask_restful.utils import unpack as flask_response_unpack
from flask_restx.utils import unpack as flask_response_unpack
from injector import (
    Binder,
    Injector,
    Module,
    Provider,
    Scope,
    ScopeDecorator,
    inject,
    singleton,
)
from werkzeug.local import Local, LocalManager, LocalProxy
from werkzeug.wrappers import Response

__author__ = ...
__version__ = ...
__all__ = ['request', 'RequestScope', 'Config', 'Request', 'FlaskInjector']

request: ScopeDecorator

T = TypeVar('T', LocalProxy[Any], Callable[..., Any])
def instance_method_wrapper(im: T) -> T:
    ...

def wrap_fun(fun: T, injector: Injector) -> T:
    ...

def wrap_function(fun: Callable[..., Any], injector: Injector) -> Callable[..., Any]:
    ...

def wrap_class_based_view(fun: Callable[..., Any], injector: Injector) -> Callable[..., Any]:
    ...

def wrap_flask_restful_resource(fun: Callable[..., Any], flask_restful_api: Any, injector: Injector) -> Callable[..., Any]:
    """
    This is needed because of how flask_restful views are registered originally.

    :type flask_restful_api: :class:`flask_restful.Api`
    """
    ...

TProvider = TypeVar("TProvider")
class CachedProviderWrapper(Provider[TProvider]):
    def __init__(self, old_provider: Provider[TProvider]) -> None:
        ...
    
    def get(self, injector: Injector) -> Any:
        ...
    


class RequestScope(Scope):
    """A scope whose object lifetime is tied to a request.

    @request
    class Session:
        pass
    """
    if False:
        ...
    def cleanup(self) -> None:
        ...
    
    def prepare(self) -> None:
        ...
    
    def configure(self) -> None:
        ...
    
    def get(self, key: Any, provider: Provider[TProvider]) -> Any:
        ...
    
    _locals: Local
    _local_manager: LocalManager


request = ...
_ModuleT = Union[Callable[[Binder], Any], Module]
class FlaskInjector:
    injector: Injector
    app: flask.Flask
    def __init__(self, app: flask.Flask, modules: Iterable[_ModuleT] = ..., injector: Injector = ..., request_scope_class: type = ...) -> None:
        """Initializes Injector for the application.

        .. note::

            Needs to be called *after* all views, signal handlers, template globals
            and context processors are registered.

        :param app: Application to configure
        :param modules: Configuration for newly created :class:`injector.Injector`
        :param injector: Injector to initialize app with, if not provided
            a new instance will be created.
        :type app: :class:`flask.Flask`
        :type modules: Iterable of configuration modules
        :rtype: :class:`injector.Injector`
        """
        ...
    


def process_dict(d: dict[Any, Any], injector: Injector) -> None:
    ...

def process_list(l: list[Any], injector: Injector) -> None:
    ...

class FlaskModule(Module):
    def __init__(self, app: flask.Flask, request_scope_class: type = ...) -> None:
        ...
    
    def configure(self, binder: Binder) -> None:
        ...
    


