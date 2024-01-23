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
class ResponseValidationOperation:
    def __init__(self, next_app: ASGIApp, *, operation: AbstractOperation, validator_map: t.Optional[dict] = ...) -> None:
        ...
    
    def extract_content_type(self, headers: t.List[t.Tuple[bytes, bytes]]) -> t.Tuple[str, str]:
        """Extract the mime type and encoding from the content type headers.

        :param headers: Headers from ASGI scope

        :return: A tuple of mime type, encoding
        """
        ...
    
    def validate_mime_type(self, mime_type: str) -> None:
        """Validate the mime type against the spec if it defines which mime types are produced.

        :param mime_type: mime type from content type header
        """
        ...
    
    @staticmethod
    def validate_required_headers(headers: t.List[tuple], response_definition: dict) -> None:
        ...
    
    async def __call__(self, scope: Scope, receive: Receive, send: Send): # -> None:
        ...
    


class ResponseValidationAPI(RoutedAPI[ResponseValidationOperation]):
    """Validation API."""
    def __init__(self, *args, validator_map=..., validate_responses=..., **kwargs) -> None:
        ...
    
    def make_operation(self, operation: AbstractOperation) -> ResponseValidationOperation:
        ...
    


class ResponseValidationMiddleware(RoutedMiddleware[ResponseValidationAPI]):
    """Middleware for validating requests according to the API contract."""
    api_cls = ResponseValidationAPI

