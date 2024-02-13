import abc
import typing

from .entity import AbcGraphEntity


class AbcNode(AbcGraphEntity, abc.ABC):
    @property
    @abc.abstractmethod
    def relations(self) -> typing.Iterable[AbcGraphEntity]:
        """graph nodes can have relations"""
