import abc

from .minion import BasicMinion
from .supervisor import BasicSupervisor
from ..abstract.labour import AbcMediator


class BasicMediator(BasicSupervisor,
                    BasicMinion,
                    AbcMediator,
                    abc.ABC): ...
