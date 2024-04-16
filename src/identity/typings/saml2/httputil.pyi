"""
This type stub file was generated by pyright.
"""

from typing import Optional

__author__ = ...
logger = ...
class Response:
    _template: Optional[str] = ...
    _status = ...
    _content_type = ...
    _mako_template = ...
    _mako_lookup = ...
    def __init__(self, message=..., **kwargs) -> None:
        ...
    
    def __call__(self, environ, start_response, **kwargs):
        ...
    
    def add_header(self, ava): # -> None:
        """
        Does *NOT* replace a header of the same type, just adds a new
        :param ava: (type, value) tuple
        """
        ...
    
    def reply(self, **kwargs):
        ...
    


class Created(Response):
    _status = ...


class Redirect(Response):
    _template = ...
    _status = ...
    def __call__(self, environ, start_response, **kwargs):
        ...
    


class SeeOther(Response):
    _template = ...
    _status = ...
    def __call__(self, environ, start_response, **kwargs):
        ...
    


class Forbidden(Response):
    _status = ...
    _template = ...


class BadRequest(Response):
    _status = ...
    _template = ...


class Unauthorized(Response):
    _status = ...
    _template = ...


class NotFound(Response):
    _status = ...


class NotAcceptable(Response):
    _status = ...


class ServiceError(Response):
    _status = ...


class NotImplemented(Response):
    _status = ...
    template = ...


class BadGateway(Response):
    _status = ...


class HttpParameters:
    """GET or POST signature parameters for Redirect or POST-SimpleSign bindings
    because they are not contained in XML unlike the POST binding
    """
    signature = ...
    sigalg = ...
    def __init__(self, dict) -> None:
        ...
    


def extract(environ, empty=..., err=...): # -> dict[str, list[str]]:
    """Extracts strings in form data and returns a dict.

    :param environ: WSGI environ
    :param empty: Stops on empty fields (default: Fault)
    :param err: Stops on errors in fields (default: Fault)
    """
    ...

def geturl(environ, query=..., path=..., use_server_name=...): # -> str:
    """Rebuilds a request URL (from PEP 333).
    You may want to chose to use the environment variables
    server_name and server_port instead of http_host in some case.
    The parameter use_server_name allows you to chose.

    :param query: Is QUERY_STRING included in URI (default: True)
    :param path: Is path included in URI (default: True)
    :param use_server_name: If SERVER_NAME/_HOST should be used instead of
        HTTP_HOST
    """
    ...

def getpath(environ): # -> str:
    """Builds a path."""
    ...

def get_post(environ):
    ...

def get_response(environ, start_response):
    ...

def unpack_redirect(environ): # -> dict[Any, Any] | None:
    ...

def unpack_post(environ): # -> dict[Any, Any]:
    ...

def unpack_soap(environ): # -> dict[str, Any] | None:
    ...

def unpack_artifact(environ): # -> dict[Any, Any] | None:
    ...

def unpack_any(environ): # -> tuple[dict[Any, Any] | dict[str, Any] | None, Literal['urn:oasis:names:tc:SAML:2.0:bindings:URI', 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact', 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect', 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST', 'urn:oasis:names:tc:SAML:2.0:bindings:SOAP']]:
    ...

def cookie_signature(seed, *parts): # -> str:
    """Generates a cookie signature."""
    ...

def make_cookie(name, load, seed, expire=..., domain=..., path=..., timestamp=...): # -> tuple[str, ...]:
    """
    Create and return a cookie

    :param name: Cookie name
    :param load: Cookie load
    :param seed: A seed for the HMAC function
    :param expire: Number of minutes before this cookie goes stale
    :param domain: The domain of the cookie
    :param path: The path specification for the cookie
    :return: A tuple to be added to headers
    """
    ...

def parse_cookie(name, seed, kaka): # -> tuple[str, str] | None:
    """Parses and verifies a cookie value

    :param seed: A seed used for the HMAC signature
    :param kaka: The cookie
    :return: A tuple consisting of (payload, timestamp)
    """
    ...

def cookie_parts(name, kaka): # -> list[str] | None:
    ...
