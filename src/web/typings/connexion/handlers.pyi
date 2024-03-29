"""
This type stub file was generated by pyright.
"""

"""
This module defines error handlers, operations that produce proper response problems.
"""
logger = ...
RESOLVER_ERROR_ENDPOINT_RANDOM_DIGITS = ...
class ResolverErrorHandler:
    """
    Handler for responding to ResolverError.
    """
    def __init__(self, status_code, exception) -> None:
        ...
    
    @property
    def function(self): # -> Callable[..., NoReturn]:
        ...
    
    def handle(self, *args, **kwargs):
        ...
    
    @property
    def operation_id(self): # -> Literal['noop']:
        ...
    
    @property
    def randomize_endpoint(self): # -> Literal[6]:
        ...
    
    def get_path_parameter_types(self): # -> dict[Any, Any]:
        ...
    
    @property
    def uri_parser_class(self): # -> Literal['dummy']:
        ...
    
    @property
    def api(self): # -> Literal['dummy']:
        ...
    
    def get_mimetype(self): # -> Literal['dummy']:
        ...
    
    async def __call__(self, *args, **kwargs):
        ...
    


