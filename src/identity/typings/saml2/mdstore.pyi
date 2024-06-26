"""
This type stub file was generated by pyright.
"""

logger = ...
classnames = ...
ENTITY_CATEGORY = ...
ENTITY_CATEGORY_SUPPORT = ...
ASSURANCE_CERTIFICATION = ...
SAML_METADATA_CONTENT_TYPE = ...
DEFAULT_FRESHNESS_PERIOD = ...
REQ2SRV = ...
class ToOld(Exception):
    ...


class TooOld(ToOld):
    ...


class SourceNotFound(Exception):
    ...


def load_extensions(): # -> dict[Any, Any]:
    ...

def load_metadata_modules(): # -> dict[str, Any]:
    ...

def metadata_modules(): # -> list[Any]:
    ...

def response_locations(srvs): # -> Generator[Any, None, None]:
    """
    Return the ResponseLocation attributes mapped to the services.

    ArtifactResolutionService, SingleSignOnService and NameIDMappingService MUST omit
    the ResponseLocation attribute. This is enforced here, but metadata with such
    service declarations and such attributes should not have been part of the metadata
    store in the first place.
    """
    ...

def locations(srvs): # -> Generator[Any, None, None]:
    ...

def destinations(srvs): # -> list[Any]:
    ...

def all_locations(srvs): # -> chain[Any]:
    ...

def attribute_requirement(entity_descriptor, index=...): # -> dict[str, list[Any]]:
    ...

def name(ent, langpref=...): # -> None:
    ...

def repack_cert(cert): # -> LiteralString:
    ...

class MetaData:
    def __init__(self, attrc, metadata=..., node_name=..., check_validity=..., security=..., **kwargs) -> None:
        ...
    
    def items(self):
        """
        Returns list of items contained in the storage
        """
        ...
    
    def keys(self):
        """
        Returns keys (identifiers) of items in storage
        """
        ...
    
    def values(self):
        """
        Returns values of items in storage
        """
        ...
    
    def __len__(self):
        """
        Returns number of stored items
        """
        ...
    
    def __contains__(self, item):
        """
        Returns True if the storage contains item
        """
        ...
    
    def __getitem__(self, item):
        """
        Returns the item specified by the key
        """
        ...
    
    def __setitem__(self, key, value):
        """
        Sets a key to a value
        """
        ...
    
    def __delitem__(self, key):
        """
        Removes key from storage
        """
        ...
    
    def do_entity_descriptor(self, entity_descr):
        """
        #FIXME - Add description
        """
        ...
    
    def parse(self, xmlstr):
        """
        #FIXME - Add description
        """
        ...
    
    def load(self, *args, **kwargs): # -> None:
        """
        Loads the metadata
        """
        ...
    
    def service(self, entity_id, typ, service, binding=...):
        """Get me all services with a specified
        entity ID and type, that supports the specified version of binding.

        :param entity_id: The EntityId
        :param typ: Type of service (idp, attribute_authority, ...)
        :param service: which service that is sought for
        :param binding: A binding identifier
        :return: list of service descriptions.
            Or if no binding was specified a list of 2-tuples (binding, srv)
        """
        ...
    
    def ext_service(self, entity_id, typ, service, binding): # -> list[Any] | None:
        ...
    
    def any(self, typ, service, binding=...): # -> dict[Any, Any]:
        """
        Return any entity that matches the specification

        :param typ: Type of entity
        :param service:
        :param binding:
        :return:
        """
        ...
    
    def any2(self, typ, service, binding=...): # -> dict[Any, Any]:
        """

        :param type:
        :param service:
        :param binding:
        :return:
        """
        ...
    
    def bindings(self, entity_id, typ, service):
        """
        Get me all the bindings that are registered for a service entity

        :param entity_id:
        :param service:
        :return:
        """
        ...
    
    def attribute_requirement(self, entity_id, index=...):
        """Returns what attributes the SP requires and which are optional
        if any such demands are registered in the Metadata.

        :param entity_id: The entity id of the SP
        :param index: which of the attribute consumer services its all about
            if index=None then return all attributes expected by all
            attribute_consuming_services.
        :return: 2-tuple, list of required and list of optional attributes
        """
        ...
    
    def subject_id_requirement(self, entity_id):
        """
        Returns what subject identifier the SP requires if any

        :param entity_id: The entity id of the SP
        :type entity_id: str
        :return: RequestedAttribute dict or None
        :rtype: Optional[dict]
        """
        ...
    
    def dumps(self): # -> str:
        ...
    
    def with_descriptor(self, descriptor): # -> dict[Any, Any]:
        """
        Returns any entities with the specified descriptor
        """
        ...
    
    def __str__(self) -> str:
        ...
    
    def construct_source_id(self):
        ...
    
    def entity_categories(self, entity_id): # -> list[Any]:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def certs(self, entity_id, descriptor, use=...): # -> list[Any]:
        """
        Returns certificates for the given Entity
        """
        ...
    


class InMemoryMetaData(MetaData):
    def __init__(self, attrc, metadata=..., node_name=..., check_validity=..., security=..., **kwargs) -> None:
        ...
    
    def items(self): # -> dict_items[Any, Any]:
        ...
    
    def keys(self): # -> dict_keys[Any, Any]:
        ...
    
    def values(self): # -> dict_values[Any, Any]:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def __contains__(self, item): # -> bool:
        ...
    
    def __getitem__(self, item):
        ...
    
    def __setitem__(self, key, value): # -> None:
        ...
    
    def __delitem__(self, key): # -> None:
        ...
    
    def do_entity_descriptor(self, entity_descr): # -> None:
        ...
    
    def parse(self, xmlstr): # -> None:
        ...
    
    def service(self, entity_id, typ, service, binding=...): # -> list[Any] | dict[Any, Any] | None:
        """Get me all services with a specified
        entity ID and type, that supports the specified version of binding.

        :param entity_id: The EntityId
        :param typ: Type of service (idp, attribute_authority, ...)
        :param service: which service that is sought for
        :param binding: A binding identifier
        :return: list of service descriptions.
            Or if no binding was specified a list of 2-tuples (binding, srv)
        """
        ...
    
    def attribute_requirement(self, entity_id, index=...): # -> dict[str, list[Any]]:
        """
        Returns what attributes the SP requires and which are optional
        if any such demands are registered in the Metadata.

        In case the metadata have multiple SPSSODescriptor elements,
        the sum of the required and optional attributes is returned.

        :param entity_id: The entity id of the SP
        :param index: which of the attribute consumer services its all about
            if index=None then return all attributes expected by all
            attribute_consuming_services.
        :return: dict of required and optional list of attributes
        """
        ...
    
    def construct_source_id(self): # -> dict[Any, Any]:
        ...
    
    def signed(self): # -> bool:
        ...
    
    def parse_and_check_signature(self, txt): # -> Literal[True]:
        ...
    


class MetaDataFile(InMemoryMetaData):
    """
    Handles Metadata file on the same machine. The format of the file is
    the SAML Metadata format.
    """
    def __init__(self, attrc, filename=..., cert=..., **kwargs) -> None:
        ...
    
    def get_metadata_content(self): # -> bytes:
        ...
    
    def load(self, *args, **kwargs): # -> Literal[True]:
        ...
    


class MetaDataLoader(MetaDataFile):
    """
    Handles Metadata file loaded by a passed in function.
    The format of the file is the SAML Metadata format.
    """
    def __init__(self, attrc, loader_callable, cert=..., security=..., **kwargs) -> None:
        ...
    
    @staticmethod
    def get_metadata_loader(func): # -> Any:
        ...
    
    def get_metadata_content(self): # -> Any:
        ...
    


class MetaDataExtern(InMemoryMetaData):
    """
    Class that handles metadata store somewhere on the net.
    Accessible by HTTP GET.
    """
    def __init__(self, attrc, url=..., security=..., cert=..., http=..., **kwargs) -> None:
        """
        :params attrc:
        :params url: Location of the metadata
        :params security: SecurityContext()
        :params cert: CertificMDloaderate used to sign the metadata
        :params http:
        """
        ...
    
    def load(self, *args, **kwargs): # -> Literal[True]:
        """Imports metadata by the use of HTTP GET.
        If the fingerprint is known the file will be checked for
        compliance before it is imported.
        """
        ...
    


class MetaDataMD(InMemoryMetaData):
    """
    Handles locally stored metadata, the file format is the text representation
    of the Python representation of the metadata.
    """
    def __init__(self, attrc, filename, **kwargs) -> None:
        ...
    
    def load(self, *args, **kwargs): # -> None:
        ...
    


class MetaDataMDX(InMemoryMetaData):
    """
    Uses the MDQ protocol to fetch entity information.
    The protocol is defined at:
    https://datatracker.ietf.org/doc/draft-young-md-query-saml/
    """
    @staticmethod
    def sha1_entity_transform(entity_id): # -> str:
        ...
    
    def __init__(self, url=..., security=..., cert=..., entity_transform=..., freshness_period=..., http_client_timeout=..., **kwargs) -> None:
        """
        :params url: mdx service url
        :params security: SecurityContext()
        :params cert: certificate used to check signature of signed metadata
        :params entity_transform: function transforming (e.g. base64,
        sha1 hash or URL quote
        hash) the entity id. It is applied to the entity id before it is
        concatenated with the request URL sent to the MDX server. Defaults to
        sha1 transformation.
        :params freshness_period: a duration in the format described at
        https://www.w3.org/TR/xmlschema-2/#duration
        :params http_client_timeout: timeout of http requests
        """
        ...
    
    def load(self, *args, **kwargs): # -> None:
        ...
    
    def __getitem__(self, item):
        ...
    
    def single_sign_on_service(self, entity_id, binding=..., typ=...): # -> list[Any] | dict[Any, Any] | None:
        ...
    


class MetadataStore(MetaData):
    def __init__(self, attrc, config, ca_certs=..., check_validity=..., disable_ssl_certificate_validation=..., filter=..., http_client_timeout=...) -> None:
        """
        :params attrc:
        :params config: Config()
        :params ca_certs:
        :params disable_ssl_certificate_validation:
        """
        ...
    
    def load(self, *args, **kwargs): # -> None:
        ...
    
    def reload(self, spec): # -> None:
        ...
    
    def imp(self, spec): # -> None:
        ...
    
    def service(self, entity_id, typ, service, binding=...):
        ...
    
    def extension(self, entity_id, typ, service): # -> list[Any] | None:
        ...
    
    def ext_service(self, entity_id, typ, service, binding=...):
        ...
    
    def single_sign_on_service(self, entity_id, binding=..., typ=...):
        ...
    
    def name_id_mapping_service(self, entity_id, binding=..., typ=...):
        ...
    
    def authn_query_service(self, entity_id, binding=..., typ=...):
        ...
    
    def attribute_service(self, entity_id, binding=..., typ=...):
        ...
    
    def authz_service(self, entity_id, binding=..., typ=...):
        ...
    
    def assertion_id_request_service(self, entity_id, binding=..., typ=...):
        ...
    
    def single_logout_service(self, entity_id, binding=..., typ=...):
        ...
    
    def manage_name_id_service(self, entity_id, binding=..., typ=...):
        ...
    
    def artifact_resolution_service(self, entity_id, binding=..., typ=...):
        ...
    
    def assertion_consumer_service(self, entity_id, binding=..., _=...):
        ...
    
    def attribute_consuming_service(self, entity_id, binding=..., _=...):
        ...
    
    def discovery_response(self, entity_id, binding=..., _=...):
        ...
    
    def attribute_requirement(self, entity_id, index=...): # -> None:
        ...
    
    def subject_id_requirement(self, entity_id): # -> list[Any] | list[dict[str, str]]:
        ...
    
    def keys(self): # -> list[Any]:
        ...
    
    def __getitem__(self, item):
        ...
    
    def __setitem__(self, key, value): # -> None:
        ...
    
    def entities(self): # -> int:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def with_descriptor(self, descriptor): # -> dict[Any, Any]:
        ...
    
    def name(self, entity_id, langpref=...): # -> None:
        ...
    
    def vo_members(self, entity_id): # -> list[Any]:
        ...
    
    def entity_categories(self, entity_id):
        """
        Get a list of entity categories for an entity id.

        :param entity_id: Entity id
        :return: Entity categories

        :type entity_id: string
        :rtype: [string]
        """
        ...
    
    def supported_entity_categories(self, entity_id):
        """
        Get a list of entity category support for an entity id.

        :param entity_id: Entity id
        :return: Entity category support

        :type entity_id: string
        :rtype: [string]
        """
        ...
    
    def assurance_certifications(self, entity_id): # -> Generator[Any, None, None]:
        ...
    
    def entity_attributes(self, entity_id): # -> dict[Any, Any]:
        """
        Get all entity attributes for an entry in the metadata.

        Example return data:

        {'http://macedir.org/entity-category': ['something', 'something2'],
         'http://example.org/saml-foo': ['bar']}

        :param entity_id: Entity id
        :return: dict with keys and value-lists from metadata

        :type entity_id: string
        :rtype: dict
        """
        ...
    
    def supported_algorithms(self, entity_id): # -> dict[str, list[Any]]:
        """
        Get all supported algorithms for an entry in the metadata.

        Example return data:

        {'digest_methods': ['http://www.w3.org/2001/04/xmldsig-more#sha224', 'http://www.w3.org/2001/04/xmlenc#sha256'],
         'signing_methods': ['http://www.w3.org/2001/04/xmldsig-more#rsa-sha256']}

        :param entity_id: Entity id
        :return: dict with keys and value-lists from metadata

        :type entity_id: string
        :rtype: dict
        """
        ...
    
    def registration_info(self, entity_id): # -> dict[str, Any]:
        """
        Get all registration info for an entry in the metadata.

        Example return data:

        res = {
            'registration_authority': 'http://www.example.com',
            'registration_instant': '2013-06-15T18:15:03Z',
            'registration_policy': {
                'en': 'http://www.example.com/policy.html',
                'sv': 'http://www.example.com/sv/policy.html',
            }
        }

        :param entity_id: Entity id
        :return: dict with keys and value-lists from metadata

        :type entity_id: string
        :rtype: dict
        """
        ...
    
    def registration_info_typ(self, entity_id, typ): # -> Generator[dict[str, Any], None, None]:
        ...
    
    def sbibmd_scopes(self, entity_id, typ=...): # -> chain[dict[str, Any]]:
        ...
    
    def shibmd_scopes(self, entity_id, typ=...): # -> chain[dict[str, Any]]:
        ...
    
    def mdui_uiinfo(self, entity_id): # -> Generator[Any, None, None]:
        ...
    
    def mdui_uiinfo_i18n_element_cls(self, entity_id, langpref, element_cls): # -> Generator[Any, None, None]:
        ...
    
    def mdui_uiinfo_i18n_element_key(self, entity_id, langpref, element_key): # -> Generator[Any, None, None]:
        ...
    
    def mdui_uiinfo_display_name(self, entity_id, langpref=...): # -> Generator[Any, None, None]:
        ...
    
    def mdui_uiinfo_description(self, entity_id, langpref=...): # -> Generator[Any, None, None]:
        ...
    
    def mdui_uiinfo_information_url(self, entity_id, langpref=...): # -> Generator[Any, None, None]:
        ...
    
    def mdui_uiinfo_privacy_statement_url(self, entity_id, langpref=...): # -> Generator[Any, None, None]:
        ...
    
    def mdui_uiinfo_logo(self, entity_id, width=..., height=...): # -> Generator[Any, None, None]:
        ...
    
    def contact_person_data(self, entity_id, contact_type=...): # -> Generator[dict[str, Any], None, None]:
        ...
    
    def bindings(self, entity_id, typ, service): # -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def construct_source_id(self): # -> dict[Any, Any]:
        ...
    
    def items(self): # -> dict_items[Any, Any]:
        ...
    
    def service_providers(self): # -> list[Any]:
        ...
    
    def identity_providers(self): # -> list[Any]:
        ...
    
    def attribute_authorities(self): # -> list[Any]:
        ...
    
    def dumps(self, format=...): # -> str | None:
        """
        Dumps the content in standard metadata format or the pysaml2 metadata
        format

        :param format: Which format to dump in
        :return: a string
        """
        ...
    


