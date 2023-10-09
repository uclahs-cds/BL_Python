"""
This type stub file was generated by pyright.
"""

import json
import logging
import sys
import uuid
import traceback
import json_logging.framework.flask as flask_support
import json_logging.framework.quart as quart_support
import json_logging.framework.connexion as connexion_support
import json_logging.framework.fastapi as fastapi_support
from datetime import datetime
from json_logging import util
from json_logging.framework_base import AppRequestInstrumentationConfigurator, FrameworkConfigurator, RequestAdapter, ResponseAdapter
from json_logging.util import get_library_logger, is_env_var_toggle
from json_logging.framework.sanic import SanicAppConfigurator, SanicAppRequestInstrumentationConfigurator, SanicRequestAdapter, SanicResponseAdapter

CORRELATION_ID_GENERATOR = ...
ENABLE_JSON_LOGGING = ...
if is_env_var_toggle("ENABLE_JSON_LOGGING"):
    ENABLE_JSON_LOGGING = ...
ENABLE_JSON_LOGGING_DEBUG = ...
EMPTY_VALUE = ...
CREATE_CORRELATION_ID_IF_NOT_EXISTS = ...
JSON_SERIALIZER = ...
CORRELATION_ID_HEADERS = ...
COMPONENT_ID = ...
COMPONENT_NAME = ...
COMPONENT_INSTANCE_INDEX = ...
_framework_support_map = ...
_current_framework = ...
_logger = ...
_request_util = ...
_default_formatter = ...
def get_correlation_id(request=...): # -> str:
    """
    Get current request correlation-id. If one is not present, a new one might be generated
    depends on CREATE_CORRELATION_ID_IF_NOT_EXISTS setting value.

    :return: correlation-id string
    """
    ...

def register_framework_support(name, app_configurator, app_request_instrumentation_configurator, request_adapter_class, response_adapter_class): # -> None:
    """
    register support for a framework

    :param name: name of framework
    :param app_configurator: app pre-configurator class
    :param app_request_instrumentation_configurator: app configurator class
    :param request_adapter_class: request adapter class
    :param response_adapter_class: response adapter class
    """
    ...

def config_root_logger(): # -> None:
    """
        You must call this if you are using root logger.
        Make all root logger' handlers produce JSON format
        & remove duplicate handlers for request instrumentation logging.
        Please made sure that you call this after you called "logging.basicConfig() or logging.getLogger()
    """
    ...

def init_non_web(*args, **kw): # -> None:
    ...

def init_request_instrument(app=..., custom_formatter=..., exclude_url_patterns=...): # -> None:
    """
    Configure the request instrumentation logging configuration for given web app. Must be called after init method

    If **custom_formatter** is passed, it will use this formatter over the default.

    :param app: current web application instance
    :param custom_formatter: formatter to override default JSONRequestLogFormatter.
    """
    ...

def get_request_logger():
    ...

class RequestInfo(dict):
    """
        class that keep HTTP request information for request instrumentation logging
    """
    def __init__(self, request, **kwargs) -> None:
        ...
    
    def update_response_status(self, response): # -> None:
        """
        update response information into this object, must be called before invoke request logging statement
        :param response:
        """
        ...
    


class BaseJSONFormatter(logging.Formatter):
    """
       Base class for JSON formatters
    """
    base_object_common = ...
    def __init__(self, *args, **kw) -> None:
        ...
    
    def format(self, record): # -> str:
        ...
    


class JSONRequestLogFormatter(BaseJSONFormatter):
    """
       Formatter for HTTP request instrumentation logging
    """
    ...


class JSONLogFormatter(BaseJSONFormatter):
    """
    Formatter for non-web application log
    """
    def get_exc_fields(self, record): # -> dict[str, str | Unknown]:
        ...
    
    @classmethod
    def format_exception(cls, exc_info): # -> str:
        ...
    


class JSONLogWebFormatter(JSONLogFormatter):
    """
    Formatter for web application log
    """
    ...


def init_flask(custom_formatter=..., enable_json=...): # -> None:
    ...

def init_sanic(custom_formatter=..., enable_json=...): # -> None:
    ...

def init_quart(custom_formatter=..., enable_json=...): # -> None:
    ...

def init_connexion(custom_formatter=..., enable_json=...): # -> None:
    ...

if fastapi_support.is_fastapi_present():
    ...
def init_fastapi(custom_formatter=..., enable_json=...): # -> None:
    ...
