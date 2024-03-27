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


class AbcConfigStore(abc.ABC):
    @abc.abstractmethod
    def __getitem__(self, item: str) -> AbcConfig:
        """finds a config by it´s name"""

    @abc.abstractmethod
    def dump(self, name: str) -> None:
        """stores an (empty) config file generated from registered config classes"""

    @abc.abstractmethod
    def load(self) -> None:
        """loads a toml config file"""

    @abc.abstractmethod
    def register(self, config: type[AbcConfig]) -> None:
        """it registers a config class, could see it coming"""
