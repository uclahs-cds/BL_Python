"""
This type stub file was generated by pyright.
"""

import sys
from saml2 import SAMLError

""" Functions connected to signing and verifying.
Based on the use of xmlsec1 binaries and not the python xmlsec module.
"""
if sys.version_info[: 2] >= (3, 9):
    ...
else:
    ...
logger = ...
SIG = ...
RSA_1_5 = ...
TRIPLE_DES_CBC = ...
RSA_OAEP_MGF1P = ...
class SigverError(SAMLError):
    ...


class CertificateTooOld(SigverError):
    ...


class XmlsecError(SigverError):
    ...


class MissingKey(SigverError):
    ...


class DecryptError(XmlsecError):
    ...


class EncryptError(XmlsecError):
    ...


class SignatureError(XmlsecError):
    ...


class BadSignature(SigverError):
    """The signature is invalid."""
    ...


def get_pem_wrapped_unwrapped(cert): # -> tuple[str, str]:
    ...

def rm_xmltag(statement):
    ...

def signed(item): # -> bool:
    """
    Is any part of the document signed ?

    :param item: A Samlbase instance
    :return: True if some part of it is signed
    """
    ...

def get_xmlsec_binary(paths=...): # -> str:
    """
    Tries to find the xmlsec1 binary.

    :param paths: Non-system path paths which should be searched when
        looking for xmlsec1
    :return: full name of the xmlsec1 binary found. If no binaries are
        found then an exception is raised.
    """
    ...

NODE_NAME = ...
ENC_NODE_NAME = ...
ENC_KEY_CLASS = ...
def signed_instance_factory(instance, seccont, elements_to_sign=...):
    """

    :param instance: The instance to be signed or not
    :param seccont: The security context
    :param elements_to_sign: Which parts if any that should be signed
    :return: A class instance if not signed otherwise a string
    """
    ...

def make_temp(content, suffix=..., decode=..., delete_tmpfiles=...): # -> _TemporaryFileWrapper[bytes]:
    """
    Create a temporary file with the given content.

    This is needed by xmlsec in some cases where only strings exist when files
    are expected.

    :param content: The information to be placed in the file
    :param suffix: The temporary file might have to have a specific
        suffix in certain circumstances.
    :param decode: The input content might be base64 coded. If so it
        must, in some cases, be decoded before being placed in the file.
    :param delete_tmpfiles: Whether to keep the tmp files or delete them when they are
        no longer in use
    :return: 2-tuple with file pointer ( so the calling function can
        close the file) and filename (which is for instance needed by the
        xmlsec function).
    """
    ...

def split_len(seq, length): # -> list[Any]:
    ...

M2_TIME_FORMAT = ...
def to_time(_time): # -> float:
    ...

def active_cert(key): # -> Literal[False]:
    """
    Verifies that a key is active that is present time is after not_before
    and before not_after.

    :param key: The Key
    :return: True if the key is active else False
    """
    ...

def cert_from_key_info(key_info, ignore_age=...): # -> list[Any]:
    """Get all X509 certs from a KeyInfo instance. Care is taken to make sure
    that the certs are continues sequences of bytes.

    All certificates appearing in an X509Data element MUST relate to the
    validation key by either containing it or being part of a certification
    chain that terminates in a certificate containing the validation key.

    :param key_info: The KeyInfo instance
    :return: A possibly empty list of certs
    """
    ...

def cert_from_key_info_dict(key_info, ignore_age=...): # -> list[Any]:
    """Get all X509 certs from a KeyInfo dictionary. Care is taken to make sure
    that the certs are continues sequences of bytes.

    All certificates appearing in an X509Data element MUST relate to the
    validation key by either containing it or being part of a certification
    chain that terminates in a certificate containing the validation key.

    :param key_info: The KeyInfo dictionary
    :return: A possibly empty list of certs in their text representation
    """
    ...

def cert_from_instance(instance): # -> list[Any]:
    """Find certificates that are part of an instance

    :param instance: An instance
    :return: possible empty list of certificates
    """
    ...

def extract_rsa_key_from_x509_cert(pem): # -> CertificatePublicKeyTypes:
    ...

def pem_format(key): # -> bytes:
    ...

def import_rsa_key_from_file(filename): # -> PrivateKeyTypes:
    ...

def parse_xmlsec_verify_output(output, version=...): # -> Literal[True]:
    """Parse the output from xmlsec to try to find out if the
    command was successfull or not.

    :param output: The output from Popen
    :return: A boolean; True if the command was a success otherwise False
    """
    ...

def sha1_digest(msg): # -> bytes:
    ...

class Signer:
    """Abstract base class for signing algorithms."""
    def __init__(self, key) -> None:
        ...
    
    def sign(self, msg, key):
        """Sign ``msg`` with ``key`` and return the signature."""
        ...
    
    def verify(self, msg, sig, key):
        """Return True if ``sig`` is a valid signature for ``msg``."""
        ...
    


class RSASigner(Signer):
    def __init__(self, digest, key=...) -> None:
        ...
    
    def sign(self, msg, key=...):
        ...
    
    def verify(self, msg, sig, key=...): # -> bool:
        ...
    


SIGNER_ALGS = ...
REQ_ORDER = ...
RESP_ORDER = ...
class RSACrypto:
    def __init__(self, key) -> None:
        ...
    
    def get_signer(self, sigalg, sigkey=...): # -> RSASigner | None:
        ...
    


def verify_redirect_signature(saml_msg, crypto, cert=..., sigkey=...): # -> bool | None:
    """

    :param saml_msg: A dictionary with strings as values, *NOT* lists as
    produced by parse_qs.
    :param cert: A certificate to use when verifying the signature
    :return: True, if signature verified
    """
    ...

class CryptoBackend:
    @property
    def version(self):
        ...
    
    @property
    def version_nums(self): # -> tuple[int, ...] | tuple[Literal[0], Literal[0], Literal[0]]:
        ...
    
    def encrypt(self, text, recv_key, template, key_type):
        ...
    
    def encrypt_assertion(self, statement, enc_key, template, key_type, node_xpath):
        ...
    
    def decrypt(self, enctext, key_file):
        ...
    
    def sign_statement(self, statement, node_name, key_file, node_id):
        ...
    
    def validate_signature(self, enctext, cert_file, cert_type, node_name, node_id):
        ...
    


ASSERT_XPATH = ...
class CryptoBackendXmlSec1(CryptoBackend):
    """
    CryptoBackend implementation using external binary 1 to sign
    and verify XML documents.
    """
    __DEBUG = ...
    def __init__(self, xmlsec_binary, delete_tmpfiles=..., **kwargs) -> None:
        ...
    
    @property
    def version(self): # -> str:
        ...
    
    def encrypt(self, text, recv_key, template, session_key_type, xpath=...): # -> bytes:
        """

        :param text: The text to be compiled
        :param recv_key: Filename of a file where the key resides
        :param template: Filename of a file with the pre-encryption part
        :param session_key_type: Type and size of a new session key
            'des-192' generates a new 192 bits DES key for DES3 encryption
        :param xpath: What should be encrypted
        :return:
        """
        ...
    
    def encrypt_assertion(self, statement, enc_key, template, key_type=..., node_xpath=..., node_id=...): # -> str:
        """
        Will encrypt an assertion

        :param statement: A XML document that contains the assertion to encrypt
        :param enc_key: File name of a file containing the encryption key
        :param template: A template for the encryption part to be added.
        :param key_type: The type of session key to use.
        :return: The encrypted text
        """
        ...
    
    def decrypt(self, enctext, key_file): # -> str:
        """

        :param enctext: XML document containing an encrypted part
        :param key_file: The key to use for the decryption
        :return: The decrypted document
        """
        ...
    
    def sign_statement(self, statement, node_name, key_file, node_id): # -> str:
        """
        Sign an XML statement.

        :param statement: The statement to be signed
        :param node_name: string like 'urn:oasis:names:...:Assertion'
        :param key_file: The file where the key can be found
        :param node_id:
        :return: The signed statement
        """
        ...
    
    def validate_signature(self, signedtext, cert_file, cert_type, node_name, node_id): # -> Literal[True]:
        """
        Validate signature on XML document.

        :param signedtext: The XML document as a string
        :param cert_file: The public key that was used to sign the document
        :param cert_type: The file type of the certificate
        :param node_name: The name of the class that is signed
        :param node_id: The identifier of the node
        :return: Boolean True if the signature was correct otherwise False.
        """
        ...
    


class CryptoBackendXMLSecurity(CryptoBackend):
    """
    CryptoBackend implementation using pyXMLSecurity to sign and verify
    XML documents.

    Encrypt and decrypt is currently unsupported by pyXMLSecurity.

    pyXMLSecurity uses lxml (libxml2) to parse XML data, but otherwise
    try to get by with native Python code. It does native Python RSA
    signatures, or alternatively PyKCS11 to offload cryptographic work
    to an external PKCS#11 module.
    """
    def __init__(self) -> None:
        ...
    
    @property
    def version(self): # -> Literal['0.0.0']:
        ...
    
    def sign_statement(self, statement, node_name, key_file, node_id): # -> str:
        """
        Sign an XML statement.

        The parameters actually used in this CryptoBackend
        implementation are :

        :param statement: XML as string
        :param node_name: Name of the node to sign
        :param key_file: xmlsec key_spec string(), filename,
            'pkcs11://' URI or PEM data
        :returns: Signed XML as string
        """
        ...
    
    def validate_signature(self, signedtext, cert_file, cert_type, node_name, node_id): # -> Literal[False]:
        """
        Validate signature on XML document.

        The parameters actually used in this CryptoBackend
        implementation are :

        :param signedtext: The signed XML data as string
        :param cert_file: xmlsec key_spec string(), filename,
            'pkcs11://' URI or PEM data
        :param cert_type: string, must be 'pem' for now
        :returns: True on successful validation, False otherwise
        """
        ...
    


def security_context(conf): # -> SecurityContext | None:
    """Creates a security context based on the configuration

    :param conf: The configuration, this is a Config instance
    :return: A SecurityContext instance
    """
    ...

def encrypt_cert_from_item(item): # -> str | None:
    ...

class CertHandlerExtra:
    def __init__(self) -> None:
        ...
    
    def use_generate_cert_func(self):
        ...
    
    def generate_cert(self, generate_cert_info, root_cert_string, root_key_string):
        ...
    
    def use_validate_cert_func(self):
        ...
    
    def validate_cert(self, cert_str, root_cert_string, root_key_string):
        ...
    


class CertHandler:
    def __init__(self, security_context, cert_file=..., cert_type=..., key_file=..., key_type=..., generate_cert_info=..., cert_handler_extra_class=..., tmp_cert_file=..., tmp_key_file=..., verify_cert=...) -> None:
        """
        Initiates the class for handling certificates. Enables the certificates
        to either be a single certificate as base functionality or makes it
        possible to generate a new certificate for each call to the function.

        :param security_context:
        :param cert_file:
        :param cert_type:
        :param key_file:
        :param key_type:
        :param generate_cert_info:
        :param cert_handler_extra_class:
        :param tmp_cert_file:
        :param tmp_key_file:
        :param verify_cert:
        """
        ...
    
    def verify_cert(self, cert_file): # -> bool:
        ...
    
    def generate_cert(self): # -> bool:
        ...
    
    def update_cert(self, active=..., client_crt=...): # -> None:
        ...
    


class SecurityContext:
    my_cert = ...
    def __init__(self, crypto, key_file=..., key_type=..., cert_file=..., cert_type=..., metadata=..., template=..., encrypt_key_type=..., only_use_keys_in_metadata=..., cert_handler_extra_class=..., generate_cert_info=..., tmp_cert_file=..., tmp_key_file=..., validate_certificate=..., enc_key_files=..., enc_key_type=..., encryption_keypairs=..., enc_cert_type=..., sec_backend=..., delete_tmpfiles=...) -> None:
        ...
    
    def correctly_signed(self, xml, must=...):
        ...
    
    def encrypt(self, text, recv_key=..., template=..., key_type=...):
        """
        xmlsec encrypt --pubkey-pem pub-userkey.pem
            --session-key aes128-cbc --xml-data doc-plain.xml
            --output doc-encrypted.xml session-key-template.xml

        :param text: Text to encrypt
        :param recv_key: A file containing the receivers public key
        :param template: A file containing the XMLSEC template
        :param key_type: The type of session key to use
        :result: An encrypted XML text
        """
        ...
    
    def encrypt_assertion(self, statement, enc_key, template, key_type=..., node_xpath=...):
        """
        Will encrypt an assertion

        :param statement: A XML document that contains the assertion to encrypt
        :param enc_key: File name of a file containing the encryption key
        :param template: A template for the encryption part to be added.
        :param key_type: The type of session key to use.
        :return: The encrypted text
        """
        ...
    
    def decrypt_keys(self, enctext, keys=...):
        """Decrypting an encrypted text by the use of a private key.

        :param enctext: The encrypted text as a string
        :param keys: Keys to try to decrypt enctext with
        :return: The decrypted text
        """
        ...
    
    def decrypt(self, enctext, key_file=...):
        """Decrypting an encrypted text by the use of a private key.

        :param enctext: The encrypted text as a string
        :return: The decrypted text
        """
        ...
    
    def verify_signature(self, signedtext, cert_file=..., cert_type=..., node_name=..., node_id=...):
        """Verifies the signature of a XML document.

        :param signedtext: The XML document as a string
        :param cert_file: The public key that was used to sign the document
        :param cert_type: The file type of the certificate
        :param node_name: The name of the class that is signed
        :param node_id: The identifier of the node
        :return: Boolean True if the signature was correct otherwise False.
        """
        ...
    
    def check_signature(self, item, node_name=..., origdoc=..., must=..., issuer=...):
        """

        :param item: Parsed entity
        :param node_name: The name of the node/class/element that is signed
        :param origdoc: The original XML string
        :param must:
        :return:
        """
        ...
    
    def correctly_signed_message(self, decoded_xml, msgtype, must=..., origdoc=..., only_valid_cert=...): # -> Any:
        """Check if a request is correctly signed, if we have metadata for
        the entity that sent the info use that, if not use the key that are in
        the message if any.

        :param decoded_xml: The SAML message as an XML infoset (a string)
        :param msgtype: SAML protocol message type
        :param must: Whether there must be a signature
        :param origdoc:
        :return:
        """
        ...
    
    def correctly_signed_authn_request(self, decoded_xml, must=..., origdoc=..., only_valid_cert=..., **kwargs): # -> Any:
        ...
    
    def correctly_signed_authn_query(self, decoded_xml, must=..., origdoc=..., only_valid_cert=..., **kwargs): # -> Any:
        ...
    
    def correctly_signed_logout_request(self, decoded_xml, must=..., origdoc=..., only_valid_cert=..., **kwargs): # -> Any:
        ...
    
    def correctly_signed_logout_response(self, decoded_xml, must=..., origdoc=..., only_valid_cert=..., **kwargs): # -> Any:
        ...
    
    def correctly_signed_attribute_query(self, decoded_xml, must=..., origdoc=..., only_valid_cert=..., **kwargs): # -> Any:
        ...
    
    def correctly_signed_authz_decision_query(self, decoded_xml, must=..., origdoc=..., only_valid_cert=..., **kwargs): # -> Any:
        ...
    
    def correctly_signed_authz_decision_response(self, decoded_xml, must=..., origdoc=..., only_valid_cert=..., **kwargs): # -> Any:
        ...
    
    def correctly_signed_name_id_mapping_request(self, decoded_xml, must=..., origdoc=..., only_valid_cert=..., **kwargs): # -> Any:
        ...
    
    def correctly_signed_name_id_mapping_response(self, decoded_xml, must=..., origdoc=..., only_valid_cert=..., **kwargs): # -> Any:
        ...
    
    def correctly_signed_artifact_request(self, decoded_xml, must=..., origdoc=..., only_valid_cert=..., **kwargs): # -> Any:
        ...
    
    def correctly_signed_artifact_response(self, decoded_xml, must=..., origdoc=..., only_valid_cert=..., **kwargs): # -> Any:
        ...
    
    def correctly_signed_manage_name_id_request(self, decoded_xml, must=..., origdoc=..., only_valid_cert=..., **kwargs): # -> Any:
        ...
    
    def correctly_signed_manage_name_id_response(self, decoded_xml, must=..., origdoc=..., only_valid_cert=..., **kwargs): # -> Any:
        ...
    
    def correctly_signed_assertion_id_request(self, decoded_xml, must=..., origdoc=..., only_valid_cert=..., **kwargs): # -> Any:
        ...
    
    def correctly_signed_assertion_id_response(self, decoded_xml, must=..., origdoc=..., only_valid_cert=..., **kwargs): # -> Any:
        ...
    
    def correctly_signed_response(self, decoded_xml, must=..., origdoc=..., only_valid_cert=..., require_response_signature=..., **kwargs):
        """Check if a instance is correctly signed, if we have metadata for
        the IdP that sent the info use that, if not use the key that are in
        the message if any.

        :param decoded_xml: The SAML message as a XML string
        :param must: Whether there must be a signature
        :param origdoc:
        :param only_valid_cert:
        :param require_response_signature:
        :return: None if the signature can not be verified otherwise an instance
        """
        ...
    
    def sign_statement_using_xmlsec(self, statement, **kwargs):
        """Deprecated function. See sign_statement()."""
        ...
    
    def sign_statement(self, statement, node_name, key=..., key_file=..., node_id=...):
        """Sign a SAML statement.

        :param statement: The statement to be signed
        :param node_name: string like 'urn:oasis:names:...:Assertion'
        :param key: The key to be used for the signing, either this or
        :param key_file: The file where the key can be found
        :param node_id:
        :return: The signed statement
        """
        ...
    
    def sign_assertion(self, statement, **kwargs):
        """Sign a SAML assertion.

        See sign_statement() for the kwargs.

        :param statement: The statement to be signed
        :return: The signed statement
        """
        ...
    
    def sign_attribute_query_using_xmlsec(self, statement, **kwargs):
        """Deprecated function. See sign_attribute_query()."""
        ...
    
    def sign_attribute_query(self, statement, **kwargs):
        """Sign a SAML attribute query.

        See sign_statement() for the kwargs.

        :param statement: The statement to be signed
        :return: The signed statement
        """
        ...
    
    def multiple_signatures(self, statement, to_sign, key=..., key_file=..., sign_alg=..., digest_alg=...):
        """
        Sign multiple parts of a statement

        :param statement: The statement that should be sign, this is XML text
        :param to_sign: A list of (items, id) tuples that specifies what to sign
        :param key: A key that should be used for doing the signing
        :param key_file: A file that contains the key to be used
        :return: A possibly multiple signed statement
        """
        ...
    


def pre_signature_part(ident, public_key=..., identifier=..., digest_alg=..., sign_alg=...): # -> Signature:
    """
    If an assertion is to be signed the signature part has to be preset
    with which algorithms to be used, this function returns such a
    preset part.

    :param ident: The identifier of the assertion, so you know which assertion
        was signed
    :param public_key: The base64 part of a PEM file
    :param identifier:
    :return: A preset signature part
    """
    ...

def pre_encryption_part(*, msg_enc=..., key_enc=..., key_name=..., encrypted_key_id=..., encrypted_data_id=..., encrypt_cert=...): # -> EncryptedData:
    ...

def pre_encrypt_assertion(response):
    """
    Move the assertion to within a encrypted_assertion
    :param response: The response with one assertion
    :return: The response but now with the assertion within an
        encrypted_assertion.
    """
    ...

if __name__ == "__main__":
    parser = ...
    args = ...
