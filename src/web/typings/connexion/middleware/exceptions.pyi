"""
This type stub file was generated by pyright.
"""

import typing as t
from starlette.exceptions import HTTPException
from starlette.middleware.exceptions import ExceptionMiddleware as StarletteExceptionMiddleware
from starlette.requests import Request as StarletteRequest
from starlette.responses import Response as StarletteResponse
from starlette.types import ASGIApp, Receive, Scope, Send
from connexion.exceptions import ProblemException
from connexion.lifecycle import ConnexionRequest, ConnexionResponse
from connexion.types import MaybeAwaitable

logger = ...
def connexion_wrapper(handler: t.Callable[[ConnexionRequest, Exception], MaybeAwaitable[ConnexionResponse]]) -> t.Callable[[StarletteRequest, Exception], t.Awaitable[StarletteResponse]]:
    """Wrapper that translates Starlette requests to Connexion requests before passing
    them to the error handler, and translates the returned Connexion responses to
    Starlette responses."""
    ...

class ExceptionMiddleware(StarletteExceptionMiddleware):
    """Subclass of starlette ExceptionMiddleware to change handling of HTTP exceptions to
    existing connexion behavior."""
    def __init__(self, next_app: ASGIApp) -> None:
        ...
    
    def add_exception_handler(self, exc_class_or_status_code: t.Union[int, t.Type[Exception]], handler: t.Callable[[ConnexionRequest, Exception], StarletteResponse]) -> None:
        ...
    
    @staticmethod
    def problem_handler(_request: ConnexionRequest, exc: ProblemException): # -> ConnexionResponse:
        """Default handler for Connexion ProblemExceptions"""
        ...
    
    @staticmethod
    @connexion_wrapper
    def http_exception(_request: StarletteRequest, exc: HTTPException, **kwargs) -> StarletteResponse:
        """Default handler for Starlette HTTPException"""
        ...
    
    @staticmethod
    def common_error_handler(_request: StarletteRequest, exc: Exception) -> ConnexionResponse:
        """Default handler for any unhandled Exception"""
        ...
    
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        ...
    


