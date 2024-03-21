import tomllib
import typing

from ..abstract.config import AbcConfig, AbcConfigStore
from ..almanac import Entitlable


class Configstore(AbcConfigStore):
    workdir = '.'
    filename = 'config.toml'

    __registered: list[type[AbcConfig]] = []
    __config: dict[str, AbcConfig] = {}

    def __class_getitem__(cls, item: typing.Union[str, Entitlable, type[Entitlable]]) -> AbcConfig:
        if isinstance(item, Entitlable) or isinstance(item, type) and issubclass(item, Entitlable):
            item = item.BADGE
        return cls.__config.get(item)

    @classmethod
    def dump(cls, name: str) -> None:
        with open(f'{cls.workdir}/{name}.toml', 'w') as file:
            for config in cls.__registered:
                file.writelines(config.dump())

    @classmethod
    def load(cls, name: str = None) -> None:
        name = f'{name}.toml' if name else cls.filename
        with open(f'{cls.workdir}/{name}', 'rb') as file:
            config: dict[str, dict] = tomllib.load(file)
            cls.__config.update(
                ((cnf_type.BADGE, cnf_type(config.get(cnf_type.BADGE)))
                 for cnf_type in cls.__registered)
            )

    @classmethod
    def register(cls, cnf_type: type[AbcConfig]) -> None:
        assert issubclass(cnf_type, AbcConfig)
        cls.__registered.append(cnf_type)

