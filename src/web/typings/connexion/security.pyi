"""
This type stub file was generated by pyright.
"""

import typing as t

"""
This module defines a SecurityHandlerFactory which supports the creation of
SecurityHandler instances for different security schemes.

It also exposes a `SECURITY_HANDLERS` dictionary which maps security scheme
types to SecurityHandler classes. This dictionary can be used to register
custom SecurityHandler classes for custom security schemes, or to overwrite
existing SecurityHandler classes.
This can be done by supplying a value for `security_map` argument of the
SecurityHandlerFactory.

Swagger 2.0 lets you define the following authentication types for an API:

- Basic authentication
- API key (as a header or a query string parameter)
- OAuth 2 common flows (authorization code, implicit, resource owner password credentials, client credentials)


Changes from OpenAPI 2.0 to OpenAPI 3.0
If you used OpenAPI 2.0 before, here is a summary of changes to help you get started with OpenAPI 3.0:
- securityDefinitions were renamed to securitySchemes and moved inside components.
- type: basic was replaced with type: http and scheme: basic.
- The new type: http is an umbrella type for all HTTP security schemes, including Basic, Bearer and other,
and the scheme keyword indicates the scheme type.
- API keys can now be sent in: cookie.
- Added support for OpenID Connect Discovery (type: openIdConnect).
- OAuth 2 security schemes can now define multiple flows.
- OAuth 2 flows were renamed to match the OAuth 2 Specification: accessCode is now authorizationCode,
and application is now clientCredentials.


OpenAPI uses the term security scheme for authentication and authorization schemes.
OpenAPI 3.0 lets you describe APIs protected using the following security schemes:

- HTTP authentication schemes (they use the Authorization header):
    - Basic
    - Bearer
    - other HTTP schemes as defined by RFC 7235 and HTTP Authentication Scheme Registry
- API keys in headers, query string or cookies
    - Cookie authentication
- OAuth 2
- OpenID Connect Discovery

"""
logger = ...
NO_VALUE = ...
class AbstractSecurityHandler:
    required_scopes_kw = ...
    client = ...
    security_definition_key: str
    environ_key: str
    def get_fn(self, security_scheme, required_scopes): # -> Callable[..., Coroutine[Any, Any, object | Any]] | None:
        """Returns the handler function"""
        ...
    
    @staticmethod
    def get_auth_header_value(request): # -> tuple[None, None] | tuple[Any, Any]:
        """
        Return Authorization type and value if any.
        If not Authorization, return (None, None)
        Raise OAuthProblem for invalid Authorization header
        """
        ...
    


class BasicSecurityHandler(AbstractSecurityHandler):
    """
    Security Handler for
    - `type: basic` (Swagger 2), and
    - `type: http` and `scheme: basic` (OpenAPI 3)
    """
    security_definition_key = ...
    environ_key = ...
    def check_basic_auth(self, basic_info_func): # -> Callable[..., Coroutine[Any, Any, object | Any]]:
        ...
    


class BearerSecurityHandler(AbstractSecurityHandler):
    """
    Security Handler for HTTP Bearer authentication.
    """
    security_definition_key = ...
    environ_key = ...
    def check_bearer_token(self, token_info_func): # -> Callable[..., Coroutine[Any, Any, object | Any]]:
        ...
    


class ApiKeySecurityHandler(AbstractSecurityHandler):
    """
    Security Handler for API Keys.
    """
    security_definition_key = ...
    environ_key = ...
    def get_fn(self, security_scheme, required_scopes): # -> Callable[..., object | Coroutine[Any, Any, object | Any]] | None:
        ...
    
    def check_api_key(self, api_key_info_func): # -> Callable[..., Coroutine[Any, Any, object | Any]]:
        ...
    
    @staticmethod
    def get_cookie_value(cookies, name): # -> str | None:
        """
        Returns cookie value by its name. `None` if no such value.

        :param cookies: str: cookies raw data
        :param name: str: cookies key
        """
        ...
    


class OAuthSecurityHandler(AbstractSecurityHandler):
    """
    Security Handler for the OAuth security scheme.
    """
    def get_fn(self, security_scheme, required_scopes): # -> Callable[..., object | Coroutine[Any, Any, object | Any]] | None:
        ...
    
    def get_tokeninfo_func(self, security_definition: dict) -> t.Optional[t.Callable]:
        """
        Gets the function for retrieving the token info.
        It is possible to specify a function or a URL. The function variant is
        preferred. If it is not found, the URL variant is used with the
        `get_token_info_remote` function.

        >>> get_tokeninfo_func({'x-tokenInfoFunc': 'foo.bar'})
        '<function foo.bar>'
        """
        ...
    
    @classmethod
    def get_scope_validate_func(cls, security_definition): # -> Any | Callable[..., Any] | None:
        """
        Gets the function for validating the token scopes.
        If it is not found, the default `validate_scope` function is used.

        >>> get_scope_validate_func({'x-scopeValidateFunc': 'foo.bar'})
        '<function foo.bar>'
        """
        ...
    
    @staticmethod
    def validate_scope(required_scopes, token_scopes): # -> bool:
        """
        :param required_scopes: Scopes required to access operation
        :param token_scopes: Scopes granted by authorization server
        :rtype: bool
        """
        ...
    
    def get_token_info_remote(self, token_info_url: str) -> t.Callable:
        """
        Return a function which will call `token_info_url` to retrieve token info.

        Returned function must accept oauth token in parameter.
        It must return a token_info dict in case of success, None otherwise.

        :param token_info_url: URL to get information about the token
        """
        ...
    
    def check_oauth_func(self, token_info_func, scope_validate_func): # -> Callable[..., Coroutine[Any, Any, object | Any]]:
        ...
    


SECURITY_HANDLERS = ...
class SecurityHandlerFactory:
    """
    A factory class for parsing security schemes and returning the appropriate
    security handler.

    By default, it will use the built-in security handlers specified in the
    SECURITY_HANDLERS dict, but you can also pass in your own security handlers
    to override the built-in ones.
    """
    def __init__(self, security_handlers: t.Optional[dict] = ...) -> None:
        ...
    
    def parse_security_scheme(self, security_scheme: dict, required_scopes: t.List[str]) -> t.Optional[t.Callable]:
        """Parses the security scheme and returns the function for verifying it.

        :param security_scheme: The security scheme from the spec.
        :param required_scopes: List of scopes for this security scheme.
        """
        ...
    
    @staticmethod
    async def security_passthrough(request):
        """Used when no security is required for the operation.

        Equivalent OpenAPI snippet:

        .. code-block:: yaml

            /helloworld
              get:
                security: []   # No security
                ...
        """
        ...
    
    @staticmethod
    def verify_none(request): # -> dict[Any, Any]:
        """Used for optional security.

        Equivalent OpenAPI snippet:

        .. code-block:: yaml

            security:
              - {}  # <--
              - myapikey: []
        """
        ...
    
    def verify_multiple_schemes(self, schemes): # -> Callable[..., Coroutine[Any, Any, object | dict[Any, Any]]]:
        """
        Verifies multiple authentication schemes in AND fashion.
        If any scheme fails, the entire authentication fails.

        :param schemes: mapping scheme_name to auth function
        :type schemes: dict
        :rtype: types.FunctionType
        """
        ...
    
    @classmethod
    def verify_security(cls, auth_funcs): # -> Callable[..., Coroutine[Any, Any, None]]:
        ...
    

