import abc
import typing

from .minion import BasicMinion
from .supervisor import BasicSupervisor
from ..abstract.labour import AbcMediator


class BasicMediator(BasicSupervisor,
                    BasicMinion,
                    AbcMediator,
                    abc.ABC):

    def __getitem__[T](self, item: typing.Union[type[T], T, str]) -> T:
        return self.supervisor[item]
