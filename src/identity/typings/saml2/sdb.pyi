"""
This type stub file was generated by pyright.
"""

logger = ...
def context_match(cfilter, cntx): # -> Literal[True]:
    ...

class SessionStorage:
    """In memory storage of session information"""
    def __init__(self) -> None:
        ...
    
    def store_assertion(self, assertion, to_sign): # -> None:
        ...
    
    def get_assertion(self, cid):
        ...
    
    def get_authn_statements(self, name_id, session_index=..., requested_context=...): # -> list[Any]:
        """

        :param name_id:
        :param session_index:
        :param requested_context:
        :return:
        """
        ...
    
    def remove_authn_statements(self, name_id): # -> None:
        ...
    


