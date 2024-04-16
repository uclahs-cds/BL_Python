"""
This type stub file was generated by pyright.
"""

"""
Contains classes and functions that a SAML2.0 Service Provider (SP) may use
to do attribute aggregation.
"""
logger = ...
DEFAULT_BINDING = ...
class AttributeResolver:
    def __init__(self, saml2client, metadata=..., config=...) -> None:
        ...
    
    def extend(self, name_id, issuer, vo_members): # -> list[Any]:
        """
        :param name_id: The identifier by which the subject is know
            among all the participents of the VO
        :param issuer: Who am I the poses the query
        :param vo_members: The entity IDs of the IdP who I'm going to ask
            for extra attributes
        :return: A dictionary with all the collected information about the
            subject
        """
        ...
    

