import abc


class AbcConfig(abc.ABC):
    # @abc.abstractmethod
    # def __init_subclass__(cls) -> None:
    #     """registers config class at config store"""
    #     ...

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """it´s a fairly new concept: with a name one can ask for it."""
        ...

    @abc.abstractmethod
    def dump(self) -> list[str]:
        """generates a toml like representation for generating a (empty) config file"""
        ...


class AbcConfigStore(type, abc.ABC):
    @abc.abstractmethod
    def __getitem__(self, item: str) -> AbcConfig:
        """finds a config by it´s name"""

    @abc.abstractmethod
    def dump(self, name: str) -> None:
        """stores an (empty) config file generated from registered config classes"""

    @abc.abstractmethod
    def load(self) -> None:
        """loads a toml config file"""

    @classmethod
    @abc.abstractmethod
    def register(cls, config: type[AbcConfig]) -> None:
        """it registers a config class, could see it coming"""
