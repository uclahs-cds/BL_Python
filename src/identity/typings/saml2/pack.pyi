"""
This type stub file was generated by pyright.
"""

"""Contains classes and functions that are necessary to implement
different bindings.

Bindings normally consists of three parts:
- rules about what to send
- how to package the information
- which protocol to use
"""
logger = ...
NAMESPACE = ...
HTML_INPUT_ELEMENT_SPEC = ...
HTML_FORM_SPEC = ...
def http_form_post_message(message, location, relay_state=..., typ=..., **kwargs): # -> dict[str, Any]:
    """The HTTP POST binding defines a mechanism by which SAML protocol
    messages may be transmitted within the base64-encoded content of a
    HTML form control.

    :param message: The message
    :param location: Where the form should be posted to
    :param relay_state: for preserving and conveying state information
    :return: A tuple containing header information and a HTML message.
    """
    ...

def http_post_message(message, relay_state=..., typ=..., **kwargs): # -> dict[str, Any]:
    """

    :param message: The message
    :param relay_state: for preserving and conveying state information
    :return: A tuple containing header information and a HTML message.
    """
    ...

def http_redirect_message(message, location, relay_state=..., typ=..., sigalg=..., sign=..., backend=...): # -> dict[str, Any]:
    """The HTTP Redirect binding defines a mechanism by which SAML protocol
    messages can be transmitted within URL parameters.
    Messages are encoded for use with this binding using a URL encoding
    technique, and transmitted using the HTTP GET method.

    The DEFLATE Encoding is used in this function.

    :param message: The message
    :param location: Where the message should be posted to
    :param relay_state: for preserving and conveying state information
    :param typ: What type of message it is SAMLRequest/SAMLResponse/SAMLart
    :param sigalg: Which algorithm the signature function will use to sign
        the message
    :param sign: Whether the message should be signed
    :return: A tuple containing header information and a HTML message.
    """
    ...

DUMMY_NAMESPACE = ...
PREFIX = ...
def make_soap_enveloped_saml_thingy(thingy, header_parts=...): # -> str | Any:
    """Returns a soap envelope containing a SAML request
    as a text string.

    :param thingy: The SAML thingy
    :return: The SOAP envelope as a string
    """
    ...

def http_soap_message(message): # -> dict[str, Any]:
    ...

def http_paos(message, extra=...): # -> dict[str, Any]:
    ...

def parse_soap_enveloped_saml(text, body_class, header_class=...): # -> tuple[Any | None, dict[Any, Any]]:
    """Parses a SOAP enveloped SAML thing and returns header parts and body

    :param text: The SOAP object as XML
    :return: header parts and body as saml.samlbase instances
    """
    ...

PACKING = ...
def packager(identifier):
    ...

def factory(binding, message, location, relay_state=..., typ=..., **kwargs):
    ...

