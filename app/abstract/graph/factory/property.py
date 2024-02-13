import abc
import typing

from .. import basic


class AbcPropertyFactory(abc.ABC):
    """a descriptor for graph properties"""

    @property
    @abc.abstractmethod
    def key(self) -> str:
        """the key string used in the graph database"""

    @property
    @abc.abstractmethod
    def is_primary(self) -> str:
        """determines if a produced property should be used as primary key"""

    @abc.abstractmethod
    def __get__(self, instance, owner) -> basic.AbcProperty:
        """produces the graph property"""

    @abc.abstractmethod
    def __set__(self, instance, value):
        """used for write protection"""

    @abc.abstractmethod
    def workflow(self) -> typing.Iterable[typing.Callable]:
        """steps to produce a concrete graph property"""
