"""
This type stub file was generated by pyright.
"""

from typing import Any
from connexion.apis.abstract import AbstractAPI
from connexion.lifecycle import ConnexionRequest

"""
This module defines a Flask Connexion API which implements translations between Flask and
Connexion requests / responses.
"""
logger = ...
class FlaskApi(AbstractAPI):
    @staticmethod
    def make_security_handler_factory(pass_context_arg_name): # -> FlaskSecurityHandlerFactory:
        """ Create default SecurityHandlerFactory to create all security check handlers """
        ...
    
    def add_openapi_json(self): # -> None:
        """
        Adds spec json to {base_path}/swagger.json
        or {base_path}/openapi.json (for oas3)
        """
        ...
    
    def add_openapi_yaml(self): # -> None:
        """
        Adds spec yaml to {base_path}/swagger.yaml
        or {base_path}/openapi.yaml (for oas3)
        """
        ...
    
    def add_swagger_ui(self): # -> None:
        """
        Adds swagger ui to {base_path}/ui/
        """
        ...
    
    def add_auth_on_not_found(self, security, security_definitions): # -> None:
        """
        Adds a 404 error handler to authenticate and only expose the 404 status if the security validation pass.
        """
        ...
    
    @classmethod
    def get_response(cls, response, mimetype=..., request=...): # -> Any | None:
        """Gets ConnexionResponse instance for the operation handler
        result. Status Code and Headers for response.  If only body
        data is returned by the endpoint function, then the status
        code will be set to 200 and no headers will be added.

        If the returned object is a flask.Response then it will just
        pass the information needed to recreate it.

        :type response: flask.Response | (flask.Response,) | (flask.Response, int) | (flask.Response, dict) | (flask.Response, int, dict)
        :rtype: ConnexionResponse
        """
        ...
    
    @classmethod
    def get_request(cls, *args: Any, **params: Any) -> ConnexionRequest:
        """Gets ConnexionRequest instance for the operation handler
        result. Status Code and Headers for response.  If only body
        data is returned by the endpoint function, then the status
        code will be set to 200 and no headers will be added.

        If the returned object is a flask.Response then it will just
        pass the information needed to recreate it.

        :rtype: ConnexionRequest
        """
        ...
    


context = ...
class InternalHandlers:
    """
    Flask handlers for internally registered endpoints.
    """
    def __init__(self, base_path, options, specification) -> None:
        ...
    
    def console_ui_home(self): # -> Text:
        """
        Home page of the OpenAPI Console UI.

        :return:
        """
        ...
    
    def console_ui_static_files(self, filename): # -> Response:
        """
        Servers the static files for the OpenAPI Console UI.

        :param filename: Requested file contents.
        :return:
        """
        ...
    
    def get_json_spec(self):
        ...
    
    def get_yaml_spec(self): # -> tuple[str, Literal[200], dict[str, str]]:
        ...
    


