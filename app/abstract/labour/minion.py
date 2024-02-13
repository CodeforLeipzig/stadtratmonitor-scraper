import abc

from .labour import AbcLabour
from .supervisor import AbcSupervisor


class AbcMinion(AbcLabour, abc.ABC):
    @property
    @abc.abstractmethod
    def supervisor(self) -> AbcSupervisor:
        """having a supervisor is what a minion makes a minion"""
        ...
