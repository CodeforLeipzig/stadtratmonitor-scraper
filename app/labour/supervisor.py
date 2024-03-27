import abc
import typing

from ..abstract.labour import AbcSupervisor, AbcLabour
from app.almanac.status import Status

from .labour import BasicLabour


class BasicSupervisor(BasicLabour, AbcSupervisor, abc.ABC):
    __registered_types: list

    def __init_subclass__(cls, **kwargs):
        cls.__registered_types = []
        super().__init_subclass__(**kwargs)

    def __init__(self, *args):
        self.__minions: typing.Iterable[AbcLabour] = list(self.init_minions(self.__registered_types))
        super().__init__(*args)

    @classmethod
    def register(cls, minion_type):
        cls.__registered_types.append(minion_type)

    @abc.abstractmethod
    def __getitem__[T](self, item: typing.Union[type[T], T, str]) -> T: ...

    @abc.abstractmethod
    def init_minions(self, *minion_types) -> typing.Iterable[AbcLabour]: ...

    @property
    def minions(self) -> typing.Iterable[AbcLabour]:
        yield from self.__minions

    @property
    def status(self) -> Status:
        for minion in self.__minions:
            if minion.status.is_busy():
                return minion.status
        return super().status

    def stop(self) -> None:
        for minion in self.__minions:
            minion.stop()
        super().stop()
