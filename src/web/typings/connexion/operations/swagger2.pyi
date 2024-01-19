"""
This type stub file was generated by pyright.
"""

from connexion.operations.abstract import AbstractOperation

"""
This module defines a Swagger2Operation class, a Connexion operation specific for Swagger 2 specs.
"""
logger = ...
COLLECTION_FORMAT_MAPPING = ...
class Swagger2Operation(AbstractOperation):
    """
    Exposes a Swagger 2.0 operation under the AbstractOperation interface.
    The primary purpose of this class is to provide the `function()` method
    to the API. A Swagger2Operation is plugged into the API with the provided
    (path, method) pair. It resolves the handler function for this operation
    with the provided resolver, and wraps the handler function with multiple
    decorators that provide security, validation, serialization,
    and deserialization.
    """
    def __init__(self, method, path, operation, resolver, app_produces, app_consumes, path_parameters=..., app_security=..., security_schemes=..., definitions=..., randomize_endpoint=..., uri_parser_class=...) -> None:
        """
        :param method: HTTP method
        :type method: str
        :param path: relative path to this operation
        :type path: str
        :param operation: swagger operation object
        :type operation: dict
        :param resolver: Callable that maps operationID to a function
        :type resolver: resolver.Resolver
        :param app_produces: list of content types the application can return by default
        :type app_produces: list
        :param app_consumes: list of content types the application consumes by default
        :type app_consumes: list
        :param path_parameters: Parameters defined in the path level
        :type path_parameters: list
        :param app_security: list of security rules the application uses by default
        :type app_security: list
        :param security_schemes: `Security Definitions Object
            <https://github.com/swagger-api/swagger-spec/blob/master/versions/2.0.md#security-definitions-object>`_
        :type security_schemes: dict
        :param definitions: `Definitions Object
            <https://github.com/swagger-api/swagger-spec/blob/master/versions/2.0.md#definitionsObject>`_
        :type definitions: dict
        :param randomize_endpoint: number of random characters to append to operation name
        :type randomize_endpoint: integer
        :param uri_parser_class: class to use for uri parsing
        :type uri_parser_class: AbstractURIParser
        """
        ...
    
    @classmethod
    def from_spec(cls, spec, *args, path, method, resolver, **kwargs): # -> Self:
        ...
    
    @property
    def request_body(self) -> dict:
        ...
    
    @property
    def parameters(self):
        ...
    
    @property
    def consumes(self):
        ...
    
    @property
    def produces(self):
        ...
    
    def get_path_parameter_types(self): # -> dict[Any, Any]:
        ...
    
    def with_definitions(self, schema):
        ...
    
    def response_schema(self, status_code=..., content_type=...):
        ...
    
    def example_response(self, status_code=..., *args, **kwargs): # -> tuple[Any, int] | tuple[Any | dict[Any, Any] | list[Any], int] | tuple[None, int]:
        """
        Returns example response from spec
        """
        ...
    
    def body_name(self, content_type: str = ...) -> str:
        ...
    
    def body_schema(self, content_type: str = ...) -> dict:
        """
        The body schema definition for this operation.
        """
        ...
    
    def body_definition(self, content_type: str = ...) -> dict:
        """
        The body complete definition for this operation.

        **There can be one "body" parameter at most.**
        """
        ...
    


