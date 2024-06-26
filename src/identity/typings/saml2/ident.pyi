"""
This type stub file was generated by pyright.
"""

from saml2 import SAMLError

__author__ = ...
logger = ...
ATTR = ...
class Unknown(SAMLError):
    ...


def code(item): # -> LiteralString:
    """
    Turn a NameID class instance into a quoted string of comma separated
    attribute,value pairs. The attribute names are replaced with digits.
    Depends on knowledge on the specific order of the attributes for the
    class that is used.

    :param item: The class instance
    :return: A quoted string
    """
    ...

def code_binary(item): # -> bytes:
    """
    Return a binary 'code' suitable for hashing.
    """
    ...

def decode(txt): # -> NameID:
    """Turns a coded string by code() into a NameID class instance.

    :param txt: The coded string
    """
    ...

class IdentDB:
    """A class that handles identifiers of entities
    Keeps a list of all nameIDs returned per SP
    """
    def __init__(self, db, domain=..., name_qualifier=...) -> None:
        ...
    
    def create_id(self, nformat, name_qualifier=..., sp_name_qualifier=...): # -> str:
        ...
    
    def store(self, ident, name_id): # -> None:
        """

        :param ident: user identifier
        :param name_id: NameID instance
        """
        ...
    
    def remove_remote(self, name_id): # -> None:
        """
        Remove a NameID to userID mapping

        :param name_id: NameID instance
        """
        ...
    
    def remove_local(self, sid): # -> None:
        ...
    
    def get_nameid(self, userid, nformat, sp_name_qualifier, name_qualifier): # -> NameID:
        ...
    
    def find_nameid(self, userid, **kwargs): # -> list[Any]:
        """
        Find a set of NameID's that matches the search criteria.

        :param userid: User id
        :param kwargs: The search filter a set of attribute/value pairs
        :return: a list of NameID instances
        """
        ...
    
    def nim_args(self, local_policy=..., sp_name_qualifier=..., name_id_policy=..., name_qualifier=...): # -> dict[str, Any]:
        """

        :param local_policy:
        :param sp_name_qualifier:
        :param name_id_policy:
        :param name_qualifier:
        :return:
        """
        ...
    
    def construct_nameid(self, userid, local_policy=..., sp_name_qualifier=..., name_id_policy=..., name_qualifier=...): # -> NameID:
        """Returns a name_id for the userid. How the name_id is
        constructed depends on the context.

        :param local_policy: The policy the server is configured to follow
        :param userid: The local permanent identifier of the object
        :param sp_name_qualifier: The 'user'/-s of the name_id
        :param name_id_policy: The policy the server on the other side wants
            us to follow.
        :param name_qualifier: A domain qualifier
        :return: NameID instance precursor
        """
        ...
    
    def transient_nameid(self, userid, sp_name_qualifier=..., name_qualifier=...): # -> NameID:
        ...
    
    def persistent_nameid(self, userid, sp_name_qualifier=..., name_qualifier=...): # -> NameID:
        ...
    
    def find_local_id(self, name_id): # -> Any | None:
        """
        Only find persistent IDs

        :param name_id:
        :return:
        """
        ...
    
    def match_local_id(self, userid, sp_name_qualifier, name_qualifier):
        ...
    
    def handle_name_id_mapping_request(self, name_id, name_id_policy): # -> NameID:
        """

        :param name_id: The NameID that specifies the principal
        :param name_id_policy: The NameIDPolicy of the requester
        :return: If an old name_id exists that match the name-id policy
            that is return otherwise if a new one can be created it
            will be and returned. If no old matching exists and a new
            is not allowed to be created None is returned.
        """
        ...
    
    def handle_manage_name_id_request(self, name_id, new_id=..., new_encrypted_id=..., terminate=...):
        """
        Requests from the SP is about the SPProvidedID attribute.
        So this is about adding,replacing and removing said attribute.

        :param name_id: NameID instance
        :param new_id: NewID instance
        :param new_encrypted_id: NewEncryptedID instance
        :param terminate: Terminate instance
        :return: The modified name_id
        """
        ...
    
    def close(self): # -> None:
        ...
    
    def sync(self): # -> None:
        ...
    


