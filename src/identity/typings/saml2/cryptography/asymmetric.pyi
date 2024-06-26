"""
This type stub file was generated by pyright.
"""

import cryptography.hazmat.primitives.hashes as _hashes

"""This module provides methods for asymmetric cryptography."""
def load_pem_private_key(data, password=...): # -> PrivateKeyTypes:
    """Load RSA PEM certificate."""
    ...

def key_sign(rsakey, message, digest):
    """Sign the given message with the RSA key."""
    ...

def key_verify(rsakey, signature, message, digest): # -> bool:
    """Verify the given signature with the RSA key."""
    ...

hashes = _hashes
