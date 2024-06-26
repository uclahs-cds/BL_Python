"""
This type stub file was generated by pyright.
"""

from saml2 import SamlBase

NAMESPACE = ...
class SPTypeType_(SamlBase):
    """The http://eidas.europa.eu/saml-extensions:SPTypeType element"""
    c_tag = ...
    c_namespace = ...
    c_value_type = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def sp_type_type__from_string(xml_string): # -> None:
    ...

class SPType(SPTypeType_):
    """The http://eidas.europa.eu/saml-extensions:SPType element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def sp_type_from_string(xml_string): # -> None:
    ...

ELEMENT_FROM_STRING = ...
ELEMENT_BY_TAG = ...
def factory(tag, **kwargs):
    ...

