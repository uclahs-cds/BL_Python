"""
This type stub file was generated by pyright.
"""

import typing as t
from starlette.types import ASGIApp, Receive, Scope, Send
from connexion.middleware.abstract import RoutedAPI, RoutedMiddleware
from connexion.operations import AbstractOperation

"""
Validation Middleware.
"""
logger = ...
class RequestValidationOperation:
    def __init__(self, next_app: ASGIApp, *, operation: AbstractOperation, strict_validation: bool = ..., validator_map: t.Optional[dict] = ...) -> None:
        ...
    
    def extract_content_type(self, headers: t.List[t.Tuple[bytes, bytes]]) -> t.Tuple[str, str]:
        """Extract the mime type and encoding from the content type headers.

        :param headers: Headers from ASGI scope

        :return: A tuple of mime type, encoding
        """
        ...
    
    def validate_mime_type(self, mime_type: str) -> None:
        """Validate the mime type against the spec if it defines which mime types are accepted.

        :param mime_type: mime type from content type header
        """
        ...
    
    @property
    def security_query_params(self) -> t.List[str]:
        """Get the names of query parameters that are used for security."""
        ...
    
    async def __call__(self, scope: Scope, receive: Receive, send: Send): # -> None:
        ...
    


class RequestValidationAPI(RoutedAPI[RequestValidationOperation]):
    """Validation API."""
    def __init__(self, *args, strict_validation=..., validator_map=..., uri_parser_class=..., **kwargs) -> None:
        ...
    
    def make_operation(self, operation: AbstractOperation) -> RequestValidationOperation:
        ...
    


class RequestValidationMiddleware(RoutedMiddleware[RequestValidationAPI]):
    """Middleware for validating requests according to the API contract."""
    api_cls = RequestValidationAPI


class MissingValidationOperation(Exception):
    """Missing validation operation"""
    ...


