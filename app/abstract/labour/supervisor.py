import abc
import typing

from .labour import AbcLabour


class AbcSupervisor(AbcLabour, abc.ABC):
    @property
    @abc.abstractmethod
    def minions(self) -> typing.Iterable[AbcLabour]:
        """something to supervise"""
        ...

    @abc.abstractmethod
    def __getitem__(self, item) -> AbcLabour:
        """a supervisor has supervision, so it can find other things"""
        ...

