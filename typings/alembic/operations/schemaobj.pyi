"""
This type stub file was generated by pyright.
"""

from typing import Any, List, Optional, Sequence, TYPE_CHECKING, Union
from sqlalchemy.sql.schema import CheckConstraint, Column, ForeignKeyConstraint, Index, MetaData, PrimaryKeyConstraint, Table, UniqueConstraint
from ..util import sqla_compat
from sqlalchemy.sql.elements import ColumnElement, TextClause
from sqlalchemy.sql.type_api import TypeEngine
from ..runtime.migration import MigrationContext

if TYPE_CHECKING:
    ...
class SchemaObjects:
    def __init__(self, migration_context: Optional[MigrationContext] = ...) -> None:
        ...
    
    def primary_key_constraint(self, name: Optional[sqla_compat._ConstraintNameDefined], table_name: str, cols: Sequence[str], schema: Optional[str] = ..., **dialect_kw) -> PrimaryKeyConstraint:
        ...
    
    def foreign_key_constraint(self, name: Optional[sqla_compat._ConstraintNameDefined], source: str, referent: str, local_cols: List[str], remote_cols: List[str], onupdate: Optional[str] = ..., ondelete: Optional[str] = ..., deferrable: Optional[bool] = ..., source_schema: Optional[str] = ..., referent_schema: Optional[str] = ..., initially: Optional[str] = ..., match: Optional[str] = ..., **dialect_kw) -> ForeignKeyConstraint:
        ...
    
    def unique_constraint(self, name: Optional[sqla_compat._ConstraintNameDefined], source: str, local_cols: Sequence[str], schema: Optional[str] = ..., **kw) -> UniqueConstraint:
        ...
    
    def check_constraint(self, name: Optional[sqla_compat._ConstraintNameDefined], source: str, condition: Union[str, TextClause, ColumnElement[Any]], schema: Optional[str] = ..., **kw) -> Union[CheckConstraint]:
        ...
    
    def generic_constraint(self, name: Optional[sqla_compat._ConstraintNameDefined], table_name: str, type_: Optional[str], schema: Optional[str] = ..., **kw) -> Any:
        ...
    
    def metadata(self) -> MetaData:
        ...
    
    def table(self, name: str, *columns, **kw) -> Table:
        ...
    
    def column(self, name: str, type_: TypeEngine, **kw) -> Column:
        ...
    
    def index(self, name: Optional[str], tablename: Optional[str], columns: Sequence[Union[str, TextClause, ColumnElement[Any]]], schema: Optional[str] = ..., **kw) -> Index:
        ...
    


