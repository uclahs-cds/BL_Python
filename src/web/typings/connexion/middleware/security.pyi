"""
This type stub file was generated by pyright.
"""

import typing as t
from starlette.types import ASGIApp, Receive, Scope, Send
from connexion.exceptions import ProblemException
from connexion.middleware.abstract import RoutedAPI, RoutedMiddleware
from connexion.operations import AbstractOperation
from connexion.security import SecurityHandlerFactory
from connexion.spec import Specification

logger = ...
class SecurityOperation:
    def __init__(self, next_app: ASGIApp, *, security_handler_factory: SecurityHandlerFactory, security: list, security_schemes: dict) -> None:
        ...
    
    @classmethod
    def from_operation(cls, operation: t.Union[AbstractOperation, Specification], *, next_app: ASGIApp, security_handler_factory: SecurityHandlerFactory) -> SecurityOperation:
        """Create a SecurityOperation from an Operation of Specification instance

        :param operation: The operation can be both an Operation or Specification instance here
            since security is defined at both levels in the OpenAPI spec. Creating a
            SecurityOperation based on a Specification can be used to create a SecurityOperation
            for routes not explicitly defined in the specification.
        :param next_app: The next ASGI app to call.
        :param security_handler_factory: The factory to be used to generate security handlers for
            the different security schemes.
        """
        ...
    
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        ...
    


class SecurityAPI(RoutedAPI[SecurityOperation]):
    def __init__(self, *args, auth_all_paths: bool = ..., security_map: dict = ..., **kwargs) -> None:
        ...
    
    def add_auth_on_not_found(self) -> None:
        """Register a default SecurityOperation for routes that are not found."""
        ...
    
    def make_operation(self, operation: t.Union[AbstractOperation, Specification]) -> SecurityOperation:
        """Create a SecurityOperation from an Operation of Specification instance

        :param operation: The operation can be both an Operation or Specification instance here
            since security is defined at both levels in the OpenAPI spec. Creating a
            SecurityOperation based on a Specification can be used to create a SecurityOperation
            for routes not explicitly defined in the specification.
        """
        ...
    


class SecurityMiddleware(RoutedMiddleware[SecurityAPI]):
    """Middleware to check if operation is accessible on scope."""
    api_cls = SecurityAPI


class MissingSecurityOperation(ProblemException):
    ...

