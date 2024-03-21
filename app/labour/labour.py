import abc
import typing

from ..almanac import Entitlable
from app.almanac.book.status import STATUS
from ..abstract.labour import AbcLabour

from ..config import Configstore, ConfigType


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
            # if there is a config annotations, it´s a concrete labour
            # noinspection PyTypeChecker
            cls.__config = Configstore[config_type]
            cls.__number_generator = number_generator()
        super().__init_subclass__(**kwargs)

    def __init__(self):
        self.__status = STATUS.INITIALIZED
        self.__run_cmd = False
        self.__number = next(self.__number_generator)

    async def __call__(self):
        self.__run_cmd = True

        while self.__run_cmd:
            self.__status = STATUS.IDLE
            await self.work()

        self._status = STATUS.STOPPED

    @abc.abstractmethod
    async def work(self) -> None: ...

    @property
    def name(self) -> str:
        return f'{self.BADGE}_{self.__number}'

    @property
    def config(self) -> ConfigType:
        return self.__config

    @property
    def config_store(self) -> type[Configstore]:
        return Configstore

    def status(self) -> str:
        return self.__status

    def set_idle(self) -> None:
        self.__status = STATUS.IDLE

    def set_busy(self) -> None:
        self.__status = STATUS.BUSY

    def stop(self) -> None:
        self.__run_cmd = False


class LabourStore(type):
    __registered = []
    __labour = {}

    @classmethod
    def register(cls, labour_type):
        assert issubclass(labour_type, AbcLabour)
        cls.__registered.append(labour_type)

    def __class_getitem__(cls, item: typing.Union[str, Entitlable, type[Entitlable]]) -> AbcLabour:
        if isinstance(item, Entitlable) or isinstance(item, type) and issubclass(item, Entitlable):
            item = item.BADGE
        return cls.__labour.get(item)
