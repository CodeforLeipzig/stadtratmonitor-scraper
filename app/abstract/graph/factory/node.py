import abc

from .. import basic


class AbcNodeFactory(abc.ABC):
    """a descriptor for graph nodes"""

    @property
    @abc.abstractmethod
    def node_cls(self) -> type:
        """determines class type for produced graph relations"""

    @property
    @abc.abstractmethod
    def node_labels(self) -> str:
        """determines relation type for graph relations"""

    @abc.abstractmethod
    def __get__(self, instance, owner) -> basic.AbcProperty:
        """produces the graph property"""

    @abc.abstractmethod
    def __set__(self, instance, value):
        """used for write protection"""
