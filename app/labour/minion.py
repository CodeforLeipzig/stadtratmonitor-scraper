import abc

from ..abstract.labour import AbcMinion, AbcSupervisor
from .labour import BasicLabour


class BasicMinion(BasicLabour, AbcMinion, abc.ABC):
    _supervisor: AbcSupervisor

    @property
    def supervisor(self) -> AbcSupervisor:
        return self._supervisor

    @property
    def status(self) -> str:
        return self._status

    def stop(self) -> None:
        self._run_cmd = False
