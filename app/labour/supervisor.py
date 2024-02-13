import abc
import typing

from ..abstract.labour import AbcSupervisor, AbcLabour
from ..almanac.status import STATUS

from .labour import BasicLabour


class BasicSupervisor(BasicLabour, AbcSupervisor, abc.ABC):
    _minions: typing.Iterable[AbcLabour]

    @property
    def minions(self) -> typing.Iterable[AbcLabour]:
        yield from self._minions

    @property
    def status(self) -> str:
        if self._status is STATUS.IDLE:
            for minion in self._minions:
                if minion.status is STATUS.BUSY:
                    return STATUS.BUSY
        return self._status

    def stop(self) -> None:
        for minion in self._minions:
            minion.stop()
        self._run_cmd = False
