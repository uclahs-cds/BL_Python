"""
This type stub file was generated by pyright.
"""

"""
This module defines a SecureOperation class, which implements the security handler for an operation.
"""
logger = ...
DEFAULT_MIMETYPE = ...
class SecureOperation:
    def __init__(self, api, security, security_schemes) -> None:
        """
        :param security: list of security rules the application uses by default
        :type security: list
        :param security_definitions: `Security Definitions Object
            <https://github.com/swagger-api/swagger-spec/blob/master/versions/2.0.md#security-definitions-object>`_
        :type security_definitions: dict
        """
        ...
    
    @property
    def api(self): # -> Unknown:
        ...
    
    @property
    def security(self): # -> Unknown:
        ...
    
    @property
    def security_schemes(self): # -> Unknown:
        ...
    
    @property
    def security_decorator(self): # -> partial[Unknown]:
        """
        Gets the security decorator for operation

        From Swagger Specification:

        **Security Definitions Object**

        A declaration of the security schemes available to be used in the specification.

        This does not enforce the security schemes on the operations and only serves to provide the relevant details
        for each scheme.


        **Operation Object -> security**

        A declaration of which security schemes are applied for this operation. The list of values describes alternative
        security schemes that can be used (that is, there is a logical OR between the security requirements).
        This definition overrides any declared top-level security. To remove a top-level security declaration,
        an empty array can be used.


        **Security Requirement Object**

        Lists the required security schemes to execute this operation. The object can have multiple security schemes
        declared in it which are all required (that is, there is a logical AND between the schemes).

        The name used for each property **MUST** correspond to a security scheme declared in the Security Definitions.

        :rtype: types.FunctionType
        """
        ...
    
    def get_mimetype(self): # -> Literal['application/json']:
        ...
    


