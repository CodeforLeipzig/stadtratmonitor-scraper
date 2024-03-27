import tomllib
import typing

from ..abstract.config import AbcConfig, AbcConfigStore
from ..almanac import Entitlable, singleton


@singleton
class Configstore(AbcConfigStore):
    workdir = '.'
    filename = 'config.toml'

    def __init__(self):
        super().__init__()
        self.__registered: list[type[AbcConfig]] = []
        self.__config: dict[str, AbcConfig] = {}

    def __getitem__(self, item: typing.Union[str, Entitlable, type[Entitlable]]) -> AbcConfig:
        badge = getattr(item, 'BADGE', None)
        return self.__config.get(badge) if badge else self.__config.get(item)

    def dump(self, name: str) -> None:
        with open(f'{self.workdir}/{name}.toml', 'w') as file:
            for config in self.__registered:
                file.writelines(config.dump())

    def load(self, name: str = None) -> None:
        name = f'{name}.toml' if name else self.filename
        with open(f'{self.workdir}/{name}', 'rb') as file:
            config: dict[str, dict] = tomllib.load(file)
        self.__config.update(
            ((cnf_type.BADGE, cnf_type(config.get(cnf_type.BADGE)))
             for cnf_type in self.__registered)
        )

    def register(self, cnf_type: type[AbcConfig]) -> None:
        assert issubclass(cnf_type, AbcConfig)
        self.__registered.append(cnf_type)


Configstore: Configstore
