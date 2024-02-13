import abc

from .entity import AbcGraphEntity


class AbcRelation(AbcGraphEntity, abc.ABC):
    @property
    @abc.abstractmethod
    def source(self) -> AbcGraphEntity:
        """graph relations have one source node"""

    @property
    @abc.abstractmethod
    def target(self) -> AbcGraphEntity:
        """graph relations have one target node"""
