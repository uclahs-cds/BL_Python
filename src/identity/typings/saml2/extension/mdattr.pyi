"""
This type stub file was generated by pyright.
"""

from saml2 import SamlBase

NAMESPACE = ...
class EntityAttributesType_(SamlBase):
    """The urn:oasis:names:tc:SAML:metadata:attribute:EntityAttributesType element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...
    def __init__(self, attribute=..., assertion=..., text=..., extension_elements=..., extension_attributes=...) -> None:
        ...
    


def entity_attributes_type__from_string(xml_string): # -> None:
    ...

class EntityAttributes(EntityAttributesType_):
    """The urn:oasis:names:tc:SAML:metadata:attribute:EntityAttributes element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def entity_attributes_from_string(xml_string): # -> None:
    ...

ELEMENT_FROM_STRING = ...
ELEMENT_BY_TAG = ...
def factory(tag, **kwargs):
    ...

