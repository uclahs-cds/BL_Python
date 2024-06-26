"""
This type stub file was generated by pyright.
"""

import saml2
from saml2 import SamlBase, xmldsig as ds

NAMESPACE = ...
class KeySizeType_(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:KeySizeType element"""
    c_tag = ...
    c_namespace = ...
    c_value_type = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def key_size_type__from_string(xml_string): # -> None:
    ...

class CipherValue(SamlBase):
    c_tag = ...
    c_namespace = ...
    c_value_type = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def cipher_value_from_string(xml_string): # -> None:
    ...

class TransformsType_(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:TransformsType element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...
    def __init__(self, transform=..., text=..., extension_elements=..., extension_attributes=...) -> None:
        ...
    


def transforms_type__from_string(xml_string): # -> None:
    ...

class KA_Nonce(SamlBase):
    c_tag = ...
    c_namespace = ...
    c_value_type = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def k_a__nonce_from_string(xml_string): # -> None:
    ...

class OriginatorKeyInfo(ds.KeyInfo):
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def originator_key_info_from_string(xml_string): # -> None:
    ...

class RecipientKeyInfo(ds.KeyInfo):
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def recipient_key_info_from_string(xml_string): # -> None:
    ...

class AgreementMethodType_(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:AgreementMethodType element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...
    def __init__(self, k_a__nonce=..., originator_key_info=..., recipient_key_info=..., algorithm=..., text=..., extension_elements=..., extension_attributes=...) -> None:
        ...
    


def agreement_method_type__from_string(xml_string): # -> None:
    ...

class ReferenceType_(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:ReferenceType element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...
    def __init__(self, uri=..., text=..., extension_elements=..., extension_attributes=...) -> None:
        ...
    


def reference_type__from_string(xml_string): # -> None:
    ...

class EncryptionPropertyType_(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:EncryptionPropertyType element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...
    def __init__(self, target=..., id=..., text=..., extension_elements=..., extension_attributes=...) -> None:
        ...
    


def encryption_property_type__from_string(xml_string): # -> None:
    ...

class KeySize(KeySizeType_):
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def key_size_from_string(xml_string): # -> None:
    ...

class OAEPparams(SamlBase):
    c_tag = ...
    c_namespace = ...
    c_value_type = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def oae_pparams_from_string(xml_string): # -> None:
    ...

class EncryptionMethodType_(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:EncryptionMethodType element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...
    def __init__(self, key_size=..., oae_pparams=..., algorithm=..., text=..., extension_elements=..., extension_attributes=...) -> None:
        ...
    


def encryption_method_type__from_string(xml_string): # -> None:
    ...

class Transforms(TransformsType_):
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def transforms_from_string(xml_string): # -> None:
    ...

class CipherReferenceType_(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:CipherReferenceType element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...
    def __init__(self, transforms=..., uri=..., text=..., extension_elements=..., extension_attributes=...) -> None:
        ...
    


def cipher_reference_type__from_string(xml_string): # -> None:
    ...

class EncryptionMethod(EncryptionMethodType_):
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def encryption_method_from_string(xml_string): # -> None:
    ...

class AgreementMethod(AgreementMethodType_):
    """The http://www.w3.org/2001/04/xmlenc#:AgreementMethod element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def agreement_method_from_string(xml_string): # -> None:
    ...

class DataReference(ReferenceType_):
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def data_reference_from_string(xml_string): # -> None:
    ...

class KeyReference(ReferenceType_):
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def key_reference_from_string(xml_string): # -> None:
    ...

class ReferenceList(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:ReferenceList element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...
    def __init__(self, data_reference=..., key_reference=..., text=..., extension_elements=..., extension_attributes=...) -> None:
        ...
    


def reference_list_from_string(xml_string): # -> None:
    ...

class EncryptionProperty(EncryptionPropertyType_):
    """The http://www.w3.org/2001/04/xmlenc#:EncryptionProperty element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def encryption_property_from_string(xml_string): # -> None:
    ...

class CipherReference(CipherReferenceType_):
    """The http://www.w3.org/2001/04/xmlenc#:CipherReference element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def cipher_reference_from_string(xml_string): # -> None:
    ...

class EncryptionPropertiesType_(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:EncryptionPropertiesType element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...
    def __init__(self, encryption_property=..., id=..., text=..., extension_elements=..., extension_attributes=...) -> None:
        ...
    


def encryption_properties_type__from_string(xml_string): # -> None:
    ...

class CipherDataType_(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:CipherDataType element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...
    def __init__(self, cipher_value=..., cipher_reference=..., text=..., extension_elements=..., extension_attributes=...) -> None:
        ...
    


def cipher_data_type__from_string(xml_string): # -> None:
    ...

class EncryptionProperties(EncryptionPropertiesType_):
    """The http://www.w3.org/2001/04/xmlenc#:EncryptionProperties element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def encryption_properties_from_string(xml_string): # -> None:
    ...

class CipherData(CipherDataType_):
    """The http://www.w3.org/2001/04/xmlenc#:CipherData element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def cipher_data_from_string(xml_string): # -> None:
    ...

class EncryptedType_(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:EncryptedType element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...
    def __init__(self, encryption_method=..., key_info=..., cipher_data=..., encryption_properties=..., id=..., type=..., mime_type=..., encoding=..., text=..., extension_elements=..., extension_attributes=...) -> None:
        ...
    


class EncryptedDataType_(EncryptedType_):
    """The http://www.w3.org/2001/04/xmlenc#:EncryptedDataType element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def encrypted_data_type__from_string(xml_string): # -> None:
    ...

class CarriedKeyName(SamlBase):
    c_tag = ...
    c_namespace = ...
    c_value_type = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def carried_key_name_from_string(xml_string): # -> None:
    ...

class EncryptedKeyType_(EncryptedType_):
    """The http://www.w3.org/2001/04/xmlenc#:EncryptedKeyType element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...
    def __init__(self, reference_list=..., carried_key_name=..., recipient=..., encryption_method=..., key_info=..., cipher_data=..., encryption_properties=..., id=..., type=..., mime_type=..., encoding=..., text=..., extension_elements=..., extension_attributes=...) -> None:
        ...
    


def encrypted_key_type__from_string(xml_string): # -> None:
    ...

class EncryptedData(EncryptedDataType_):
    """The http://www.w3.org/2001/04/xmlenc#:EncryptedData element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def encrypted_data_from_string(xml_string): # -> None:
    ...

class EncryptedKey(EncryptedKeyType_):
    """The http://www.w3.org/2001/04/xmlenc#:EncryptedKey element"""
    c_tag = ...
    c_namespace = ...
    c_children = ...
    c_attributes = ...
    c_child_order = ...
    c_cardinality = ...


def encrypted_key_from_string(xml_string): # -> None:
    ...

ELEMENT_FROM_STRING = ...
ELEMENT_BY_TAG = ...
def factory(tag, **kwargs):
    ...

