"""
This type stub file was generated by pyright.
"""

from saml2 import SamlBase

NAMESPACE = ...
class RequestType_(SamlBase):
    """The urn:oasis:names:tc:SAML:2.0:profiles:SSO:ecp:RequestType element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...
    def __init__(self, issuer=..., idp_list=..., must_understand=..., actor=..., provider_name=..., is_passive=..., text=..., extension_elements=..., extension_attributes=...) -> None:
        ...
    


def request_type__from_string(xml_string): # -> None:
    ...

class ResponseType_(SamlBase):
    """The urn:oasis:names:tc:SAML:2.0:profiles:SSO:ecp:ResponseType element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...
    def __init__(self, must_understand=..., actor=..., assertion_consumer_service_url=..., text=..., extension_elements=..., extension_attributes=...) -> None:
        ...
    


def response_type__from_string(xml_string): # -> None:
    ...

class RelayStateType_(SamlBase):
    """The urn:oasis:names:tc:SAML:2.0:profiles:SSO:ecp:RelayStateType element"""
    c_tag = ...
    c_namespace = ...
    c_value_type = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...
    def __init__(self, must_understand=..., actor=..., text=..., extension_elements=..., extension_attributes=...) -> None:
        ...
    


def relay_state_type__from_string(xml_string): # -> None:
    ...

class Request(RequestType_):
    """The urn:oasis:names:tc:SAML:2.0:profiles:SSO:ecp:Request element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def request_from_string(xml_string): # -> None:
    ...

class Response(ResponseType_):
    """The urn:oasis:names:tc:SAML:2.0:profiles:SSO:ecp:Response element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def response_from_string(xml_string): # -> None:
    ...

class RelayState(RelayStateType_):
    """The urn:oasis:names:tc:SAML:2.0:profiles:SSO:ecp:RelayState element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def relay_state_from_string(xml_string): # -> None:
    ...

ELEMENT_FROM_STRING = ...
ELEMENT_BY_TAG = ...
def factory(tag, **kwargs):
    ...

