"""
This type stub file was generated by pyright.
"""

"""
This module defines view function decorator to collect UWSGI metrics and expose them via an
endpoint.
"""
HAS_UWSGI_METRICS = ...
class UWSGIMetricsCollector:
    def __init__(self, path, method) -> None:
        ...
    
    @staticmethod
    def is_available(): # -> bool:
        ...
    
    def __call__(self, function): # -> _Wrapped[..., Unknown, (*args: Unknown, **kwargs: Unknown), Unknown]:
        """
        :type function: types.FunctionType
        :rtype: types.FunctionType
        """
        ...
    


