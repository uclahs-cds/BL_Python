"""
This type stub file was generated by pyright.
"""

from typing import Optional

def template_to_file(template_file: str, dest: str, output_encoding: str, **kw) -> None:
    ...

def coerce_resource_to_filename(fname: str) -> str:
    """Interpret a filename as either a filesystem location or as a package
    resource.

    Names that are non absolute paths and contain a colon
    are interpreted as resources and coerced to a file location.

    """
    ...

def pyc_file_from_path(path: str) -> Optional[str]:
    """Given a python source path, locate the .pyc."""
    ...

def load_python_file(dir_: str, filename: str): # -> ModuleType:
    """Load a file from the given path as a Python module."""
    ...

def load_module_py(module_id: str, path: str): # -> ModuleType:
    ...

