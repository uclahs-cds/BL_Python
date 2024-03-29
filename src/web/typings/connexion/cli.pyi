"""
This type stub file was generated by pyright.
"""

import argparse
import typing as t
from connexion.apps import AbstractApp

"""
This module defines a command-line interface (CLI) that runs an OpenAPI specification to be a
starting point for developing your API with Connexion.
"""
logger = ...
FLASK_APP = ...
ASYNC_APP = ...
AVAILABLE_APPS = ...
def run(app: AbstractApp, args: argparse.Namespace): # -> None:
    ...

parser = ...
subparsers = ...
run_parser = ...
def create_app(args: t.Optional[argparse.Namespace] = ...) -> AbstractApp:
    """Runs a server compliant with a OpenAPI/Swagger Specification file."""
    ...

def main(argv: t.Optional[t.List[str]] = ...) -> None:
    ...

