"""
This type stub file was generated by pyright.
"""

logger = ...
class VirtualOrg:
    def __init__(self, sp, vorg, cnf) -> None:
        ...
    
    def members_to_ask(self, name_id): # -> list[Any]:
        """Find the member of the Virtual Organization that I haven't already
        spoken too
        """
        ...
    
    def get_common_identifier(self, name_id): # -> None:
        ...
    
    def do_aggregation(self, name_id): # -> bool:
        ...
    


