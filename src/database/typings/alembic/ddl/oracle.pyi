"""
This type stub file was generated by pyright.
"""

from typing import Any, TYPE_CHECKING
from .base import AddColumn, ColumnComment, ColumnDefault, ColumnName, ColumnNullable, ColumnType, IdentityColumnDefault, RenameTable
from .impl import DefaultImpl
from ..util.sqla_compat import compiles
from sqlalchemy.dialects.oracle.base import OracleDDLCompiler
from sqlalchemy.sql.schema import Column

if TYPE_CHECKING:
    ...
class OracleImpl(DefaultImpl):
    __dialect__ = ...
    transactional_ddl = ...
    batch_separator = ...
    command_terminator = ...
    type_synonyms = ...
    identity_attrs_ignore = ...
    def __init__(self, *arg, **kw) -> None:
        ...
    
    def compare_server_default(self, inspector_column, metadata_column, rendered_metadata_default, rendered_inspector_default): # -> bool:
        ...
    
    def emit_begin(self) -> None:
        ...
    
    def emit_commit(self) -> None:
        ...
    


@compiles(AddColumn, "oracle")
def visit_add_column(element: AddColumn, compiler: OracleDDLCompiler, **kw) -> str:
    ...

@compiles(ColumnNullable, "oracle")
def visit_column_nullable(element: ColumnNullable, compiler: OracleDDLCompiler, **kw) -> str:
    ...

@compiles(ColumnType, "oracle")
def visit_column_type(element: ColumnType, compiler: OracleDDLCompiler, **kw) -> str:
    ...

@compiles(ColumnName, "oracle")
def visit_column_name(element: ColumnName, compiler: OracleDDLCompiler, **kw) -> str:
    ...

@compiles(ColumnDefault, "oracle")
def visit_column_default(element: ColumnDefault, compiler: OracleDDLCompiler, **kw) -> str:
    ...

@compiles(ColumnComment, "oracle")
def visit_column_comment(element: ColumnComment, compiler: OracleDDLCompiler, **kw) -> str:
    ...

@compiles(RenameTable, "oracle")
def visit_rename_table(element: RenameTable, compiler: OracleDDLCompiler, **kw) -> str:
    ...

def alter_column(compiler: OracleDDLCompiler, name: str) -> str:
    ...

def add_column(compiler: OracleDDLCompiler, column: Column[Any], **kw) -> str:
    ...

@compiles(IdentityColumnDefault, "oracle")
def visit_identity_column(element: IdentityColumnDefault, compiler: OracleDDLCompiler, **kw): # -> str:
    ...

