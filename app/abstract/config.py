import abc
from ..almanac import Entitlable


class AbcConfig(Entitlable, abc.ABC):
    @abc.abstractmethod
    def __init__(self, cnf: dict): ...

    @classmethod
    @abc.abstractmethod
    def dump(cls) -> list[str]:
        """generates a toml like representation for generating a (empty) config file"""
        ...


class AbcConfigStore(type, abc.ABC):
    @abc.abstractmethod
    def __class_getitem__(cls, item: str) -> AbcConfig:
        """finds a config by it´s name"""

    @classmethod
    @abc.abstractmethod
    def dump(cls, name: str) -> None:
        """stores an (empty) config file generated from registered config classes"""

    @classmethod
    @abc.abstractmethod
    def load(cls) -> None:
        """loads a toml config file"""

    @classmethod
    @abc.abstractmethod
    def register(cls, config: type[AbcConfig]) -> None:
        """it registers a config class, could see it coming"""
