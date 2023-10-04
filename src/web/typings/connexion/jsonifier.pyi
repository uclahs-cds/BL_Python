"""
This type stub file was generated by pyright.
"""

import json

"""
This module centralizes all functionality related to json encoding and decoding in Connexion.
"""
class JSONEncoder(json.JSONEncoder):
    """The default Connexion JSON encoder. Handles extra types compared to the
    built-in :class:`json.JSONEncoder`.

    -   :class:`datetime.datetime` and :class:`datetime.date` are
        serialized to :rfc:`822` strings. This is the same as the HTTP
        date format.
    -   :class:`uuid.UUID` is serialized to a string.
    """
    def default(self, o): # -> str | Any:
        ...
    


class Jsonifier:
    """
    Central point to serialize and deserialize to/from JSon in Connexion.
    """
    def __init__(self, json_=..., **kwargs) -> None:
        """
        :param json_: json library to use. Must have loads() and dumps() method  # NOQA
        :param kwargs: default arguments to pass to json.dumps()
        """
        ...
    
    def dumps(self, data, **kwargs): # -> str:
        """ Central point where JSON serialization happens inside
        Connexion.
        """
        ...
    
    def loads(self, data): # -> Any | str | None:
        """ Central point where JSON deserialization happens inside
        Connexion.
        """
        ...
    


