import abc
import typing
from contextlib import contextmanager

from app.almanac.status import Status
from app.abstract.labour import AbcLabour
from app.config import Configstore, ConfigType


registered_labours = []


def number_generator():
    i = 0
    while True:
        yield i
        i += 1


class BasicLabour(AbcLabour, abc.ABC):
    __config: ConfigType

    def __init_subclass__(cls, **kwargs):
        if config_type := cls.__annotations__.get('config'):
            cls.__config = Configstore[config_type]
            cls.__number_generator = number_generator()
        super().__init_subclass__(**kwargs)

    def __init__(self, *_):
        self.__status = Status()
        self.__run_cmd = False
        self.__number = next(self.__number_generator)

    async def __call__(self):
        self.__run_cmd = True
        with self.__status.idle_and_stopped_cnx:
            while self.__run_cmd:
                with self.loop as work:
                    await work

    @contextmanager
    def loop(self):
        yield self.work()

    @abc.abstractmethod
    async def work(self, *args, **kwargs) -> None: ...

    @property
    def name(self) -> str:
        return f'{self.BADGE}_{self.__number}'

    @property
    def config(self) -> ConfigType:
        return self.__config

    @property
    def config_store(self) -> type[Configstore]:
        return Configstore

    @property
    def run_cmd(self) -> bool:
        return self.__run_cmd

    @property
    def status(self) -> Status:
        return self.__status

    def stop(self) -> None:
        self.__run_cmd = False
