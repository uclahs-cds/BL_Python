"""
This type stub file was generated by pyright.
"""

"""This module provides methods for PKI operations."""
logger = ...
DEFAULT_CERT_TYPE = ...
def load_pem_x509_certificate(data): # -> Certificate:
    """Load X.509 PEM certificate."""
    ...

def load_der_x509_certificate(data): # -> Certificate:
    """Load X.509 DER certificate."""
    ...

def load_x509_certificate(data, cert_type=...):
    ...

def get_public_bytes_from_cert(cert):
    ...

_x509_loaders = ...