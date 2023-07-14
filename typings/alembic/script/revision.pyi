"""
This type stub file was generated by pyright.
"""

from typing import Any, Callable, Collection, Dict, FrozenSet, Iterable, Iterator, Optional, Sequence, Set, TYPE_CHECKING, Tuple, TypeVar, Union, overload
from .. import util

if TYPE_CHECKING:
    ...
_RevIdType = Union[str, Sequence[str]]
_RevisionIdentifierType = Union[str, Tuple[str, ...], None]
_RevisionOrStr = Union["Revision", str]
_RevisionOrBase = Union["Revision", "Literal['base']"]
_InterimRevisionMapType = Dict[str, "Revision"]
_RevisionMapType = Dict[Union[None, str, Tuple[()]], Optional["Revision"]]
_T = TypeVar("_T", bound=Union[str, "Revision"])
_relative_destination = ...
_revision_illegal_chars = ...
class RevisionError(Exception):
    ...


class RangeNotAncestorError(RevisionError):
    def __init__(self, lower: _RevisionIdentifierType, upper: _RevisionIdentifierType) -> None:
        ...
    


class MultipleHeads(RevisionError):
    def __init__(self, heads: Sequence[str], argument: Optional[str]) -> None:
        ...
    


class ResolutionError(RevisionError):
    def __init__(self, message: str, argument: str) -> None:
        ...
    


class CycleDetected(RevisionError):
    kind = ...
    def __init__(self, revisions: Sequence[str]) -> None:
        ...
    


class DependencyCycleDetected(CycleDetected):
    kind = ...
    def __init__(self, revisions: Sequence[str]) -> None:
        ...
    


class LoopDetected(CycleDetected):
    kind = ...
    def __init__(self, revision: str) -> None:
        ...
    


class DependencyLoopDetected(DependencyCycleDetected, LoopDetected):
    kind = ...
    def __init__(self, revision: Sequence[str]) -> None:
        ...
    


class RevisionMap:
    """Maintains a map of :class:`.Revision` objects.

    :class:`.RevisionMap` is used by :class:`.ScriptDirectory` to maintain
    and traverse the collection of :class:`.Script` objects, which are
    themselves instances of :class:`.Revision`.

    """
    def __init__(self, generator: Callable[[], Iterable[Revision]]) -> None:
        """Construct a new :class:`.RevisionMap`.

        :param generator: a zero-arg callable that will generate an iterable
         of :class:`.Revision` instances to be used.   These are typically
         :class:`.Script` subclasses within regular Alembic use.

        """
        ...
    
    @util.memoized_property
    def heads(self) -> Tuple[str, ...]:
        """All "head" revisions as strings.

        This is normally a tuple of length one,
        unless unmerged branches are present.

        :return: a tuple of string revision numbers.

        """
        ...
    
    @util.memoized_property
    def bases(self) -> Tuple[str, ...]:
        """All "base" revisions as strings.

        These are revisions that have a ``down_revision`` of None,
        or empty tuple.

        :return: a tuple of string revision numbers.

        """
        ...
    
    def add_revision(self, revision: Revision, _replace: bool = ...) -> None:
        """add a single revision to an existing map.

        This method is for single-revision use cases, it's not
        appropriate for fully populating an entire revision map.

        """
        ...
    
    def get_current_head(self, branch_label: Optional[str] = ...) -> Optional[str]:
        """Return the current head revision.

        If the script directory has multiple heads
        due to branching, an error is raised;
        :meth:`.ScriptDirectory.get_heads` should be
        preferred.

        :param branch_label: optional branch name which will limit the
         heads considered to those which include that branch_label.

        :return: a string revision number.

        .. seealso::

            :meth:`.ScriptDirectory.get_heads`

        """
        ...
    
    def get_revisions(self, id_: Union[str, Collection[Optional[str]], None]) -> Tuple[Optional[_RevisionOrBase], ...]:
        """Return the :class:`.Revision` instances with the given rev id
        or identifiers.

        May be given a single identifier, a sequence of identifiers, or the
        special symbols "head" or "base".  The result is a tuple of one
        or more identifiers, or an empty tuple in the case of "base".

        In the cases where 'head', 'heads' is requested and the
        revision map is empty, returns an empty tuple.

        Supports partial identifiers, where the given identifier
        is matched against all identifiers that start with the given
        characters; if there is exactly one match, that determines the
        full revision.

        """
        ...
    
    def get_revision(self, id_: Optional[str]) -> Optional[Revision]:
        """Return the :class:`.Revision` instance with the given rev id.

        If a symbolic name such as "head" or "base" is given, resolves
        the identifier into the current head or base revision.  If the symbolic
        name refers to multiples, :class:`.MultipleHeads` is raised.

        Supports partial identifiers, where the given identifier
        is matched against all identifiers that start with the given
        characters; if there is exactly one match, that determines the
        full revision.

        """
        ...
    
    def filter_for_lineage(self, targets: Iterable[_T], check_against: Optional[str], include_dependencies: bool = ...) -> Tuple[_T, ...]:
        ...
    
    def iterate_revisions(self, upper: _RevisionIdentifierType, lower: _RevisionIdentifierType, implicit_base: bool = ..., inclusive: bool = ..., assert_relative_length: bool = ..., select_for_downgrade: bool = ...) -> Iterator[Revision]:
        """Iterate through script revisions, starting at the given
        upper revision identifier and ending at the lower.

        The traversal uses strictly the `down_revision`
        marker inside each migration script, so
        it is a requirement that upper >= lower,
        else you'll get nothing back.

        The iterator yields :class:`.Revision` objects.

        """
        ...
    


class Revision:
    """Base class for revisioned objects.

    The :class:`.Revision` class is the base of the more public-facing
    :class:`.Script` object, which represents a migration script.
    The mechanics of revision management and traversal are encapsulated
    within :class:`.Revision`, while :class:`.Script` applies this logic
    to Python files in a version directory.

    """
    nextrev: FrozenSet[str] = ...
    _all_nextrev: FrozenSet[str] = ...
    revision: str = ...
    down_revision: Optional[_RevIdType] = ...
    dependencies: Optional[_RevIdType] = ...
    branch_labels: Set[str] = ...
    _resolved_dependencies: Tuple[str, ...]
    _normalized_resolved_dependencies: Tuple[str, ...]
    @classmethod
    def verify_rev_id(cls, revision: str) -> None:
        ...
    
    def __init__(self, revision: str, down_revision: Optional[Union[str, Tuple[str, ...]]], dependencies: Optional[Union[str, Tuple[str, ...]]] = ..., branch_labels: Optional[Union[str, Tuple[str, ...]]] = ...) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def add_nextrev(self, revision: Revision) -> None:
        ...
    
    @property
    def is_head(self) -> bool:
        """Return True if this :class:`.Revision` is a 'head' revision.

        This is determined based on whether any other :class:`.Script`
        within the :class:`.ScriptDirectory` refers to this
        :class:`.Script`.   Multiple heads can be present.

        """
        ...
    
    @property
    def is_base(self) -> bool:
        """Return True if this :class:`.Revision` is a 'base' revision."""
        ...
    
    @property
    def is_branch_point(self) -> bool:
        """Return True if this :class:`.Script` is a branch point.

        A branchpoint is defined as a :class:`.Script` which is referred
        to by more than one succeeding :class:`.Script`, that is more
        than one :class:`.Script` has a `down_revision` identifier pointing
        here.

        """
        ...
    
    @property
    def is_merge_point(self) -> bool:
        """Return True if this :class:`.Script` is a merge point."""
        ...
    


@overload
def tuple_rev_as_scalar(rev: Optional[Sequence[str]]) -> Optional[Union[str, Sequence[str]]]:
    ...

@overload
def tuple_rev_as_scalar(rev: Optional[Sequence[Optional[str]]]) -> Optional[Union[Optional[str], Sequence[Optional[str]]]]:
    ...

def tuple_rev_as_scalar(rev): # -> None:
    ...

def is_revision(rev: Any) -> Revision:
    ...

