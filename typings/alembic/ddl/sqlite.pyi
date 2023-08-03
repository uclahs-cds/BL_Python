"""
This type stub file was generated by pyright.
"""

from typing import Any, Dict, Optional, TYPE_CHECKING, Union
from sqlalchemy.ext.compiler import compiles
from .base import RenameTable
from .impl import DefaultImpl
from sqlalchemy.engine.reflection import Inspector
from sqlalchemy.sql.compiler import DDLCompiler
from sqlalchemy.sql.elements import Cast, ClauseElement
from sqlalchemy.sql.schema import Column, Constraint, Table
from sqlalchemy.sql.type_api import TypeEngine
from ..operations.batch import BatchOperationsImpl

if TYPE_CHECKING:
    ...
class SQLiteImpl(DefaultImpl):
    __dialect__ = ...
    transactional_ddl = ...
    def requires_recreate_in_batch(self, batch_op: BatchOperationsImpl) -> bool:
        """Return True if the given :class:`.BatchOperationsImpl`
        would need the table to be recreated and copied in order to
        proceed.

        Normally, only returns True on SQLite when operations other
        than add_column are present.

        """
        ...
    
    def add_constraint(self, const: Constraint): # -> None:
        ...
    
    def drop_constraint(self, const: Constraint): # -> None:
        ...
    
    def compare_server_default(self, inspector_column: Column[Any], metadata_column: Column[Any], rendered_metadata_default: Optional[str], rendered_inspector_default: Optional[str]) -> bool:
        ...
    
    def autogen_column_reflect(self, inspector: Inspector, table: Table, column_info: Dict[str, Any]) -> None:
        ...
    
    def render_ddl_sql_expr(self, expr: ClauseElement, is_server_default: bool = ..., **kw) -> str:
        ...
    
    def cast_for_batch_migrate(self, existing: Column[Any], existing_transfer: Dict[str, Union[TypeEngine, Cast]], new_type: TypeEngine) -> None:
        ...
    
    def correct_for_autogen_constraints(self, conn_unique_constraints, conn_indexes, metadata_unique_constraints, metadata_indexes): # -> None:
        ...
    


@compiles(RenameTable, "sqlite")
def visit_rename_table(element: RenameTable, compiler: DDLCompiler, **kw) -> str:
    ...

