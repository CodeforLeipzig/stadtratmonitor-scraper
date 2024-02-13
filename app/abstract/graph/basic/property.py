import abc
import typing

from . import item


class AbcProperty(item.AbcItem, abc.ABC):
    """a graph property is hold by a graph entity"""

    @property
    @abc.abstractmethod
    def key(self) -> str:
        """get the key from a graph property"""

    @property
    @abc.abstractmethod
    def value(self) -> typing.Any:
        """get the value from a graph property"""

    @property
    @abc.abstractmethod
    def is_primary(self) -> bool:
        """a graph property which should be unique on every graph entity"""

    @abc.abstractmethod
    def __iter__(self) -> typing.Iterable[tuple]:
        """used for dict(graph_property)"""
