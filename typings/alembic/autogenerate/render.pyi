"""
This type stub file was generated by pyright.
"""

from typing import List, TYPE_CHECKING
from sqlalchemy.sql.elements import conv
from ..operations import ops
from alembic.autogenerate.api import AutogenContext

if TYPE_CHECKING:
    ...
MAX_PYTHON_ARGS = ...
renderers = ...
def render_op(autogen_context: AutogenContext, op: ops.MigrateOperation) -> List[str]:
    ...

def render_op_text(autogen_context: AutogenContext, op: ops.MigrateOperation) -> str:
    ...

class _f_name:
    def __init__(self, prefix: str, name: conv) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    


_constraint_renderers = ...
renderers = ...
