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
    def __getitem__[T](self, item: typing.Union[type[T], T, str]) -> T:
        """a supervisor has supervision, so it can find other things"""
        ...

    @abc.abstractmethod
    def get_item[T](self, item: typing.Union[type[T], T, str]) -> T:
        """a supervisor has supervision, so it can find other things"""
        ...
