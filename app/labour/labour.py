import abc
import typing

from ..almanac.status import STATUS
from ..abstract.labour import AbcLabour
from ..abstract.config import AbcConfig


def number_generator():
    i = 0
    while True:
        yield i
        i += 1


class BasicLabour(AbcLabour, abc.ABC):
    _run_cmd: bool = False
    _status: STATUS.INITIALIZED

    _config_store: typing.Mapping
    _number: int
    _number_generator: typing.Generator[int, None, None]

    async def __call__(self):
        self._run_cmd = True

        while self._run_cmd:
            self._status = STATUS.IDLE
            await self._work()

        self._status = STATUS.STOPPED

    @property
    def name(self) -> str:
        return f'{self.BADGE}_{self._number}'

    @property
    def config(self) -> AbcConfig:
        return self._config_store[self]

    @abc.abstractmethod
    async def _work(self) -> None: ...

