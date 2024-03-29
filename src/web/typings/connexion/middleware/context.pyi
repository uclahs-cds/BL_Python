"""
This type stub file was generated by pyright.
"""

from starlette.types import ASGIApp, Receive, Scope, Send
from connexion.middleware.abstract import RoutedAPI, RoutedMiddleware
from connexion.operations import AbstractOperation

"""The ContextMiddleware creates a global context based the scope. It should be last in the
middleware stack, so it exposes the scope passed to the application"""
class ContextOperation:
    def __init__(self, next_app: ASGIApp, *, operation: AbstractOperation) -> None:
        ...
    
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        ...
    


class ContextAPI(RoutedAPI[ContextOperation]):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def make_operation(self, operation: AbstractOperation) -> ContextOperation:
        ...
    


class ContextMiddleware(RoutedMiddleware[ContextAPI]):
    """Middleware to expose operation specific context to application."""
    api_cls = ContextAPI


