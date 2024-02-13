import abc
import typing

from .item import AbcItem
from .property import AbcProperty


class AbcGraphEntity(AbcItem, abc.ABC):
    """a graph entity is a node or a relation"""

    @property
    @abc.abstractmethod
    def labels(self) -> typing.Iterable[str]:
        """graph relations are normally labeled with a type, it´s simpler to call both a label"""

    @property
    @abc.abstractmethod
    def properties(self) -> typing.Iterable[AbcProperty]:
        """all properties from a graph object"""

    @property
    @abc.abstractmethod
    def primaries(self) -> typing.Iterable[AbcProperty]:
        """only properties labeled as primary key"""

    @property
    @abc.abstractmethod
    def non_primaries(self) -> typing.Iterable[AbcProperty]:
        """only properties not labeled as primary key"""

    @property
    @abc.abstractmethod
    def is_valid(self) -> bool:
        """determines if an object is fully loaded"""

    @abc.abstractmethod
    def cypher(self, cypher) -> object:
        """create cypher representation"""
