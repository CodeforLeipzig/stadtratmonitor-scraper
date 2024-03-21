from ..abstract.config import AbcConfig
from ..almanac import Entitlable
from .configstore import Configstore


class ConfigType(AbcConfig):
    def __init__(self, cnf: dict):
        for key, type_ in self.__annotations__.items():
            setattr(self, key, type_(cnf.get(key)))

    def __init_subclass__(cls, abstract: Entitlable = None, **kwargs):
        if abstract:
            kwargs['badge'] = abstract.BADGE
        super().__init_subclass__(**kwargs)
        Configstore.register(cls)

    @classmethod
    def dump(cls) -> list[str]:
        yield toml_head.format(value=cls.BADGE)
        for key, type_ in cls.__annotations__.items():
            yield toml_line.format(key=key, value=toml_map.get(type_))
        yield '\n'


toml_head = '[{value}]\n'
toml_comment = '# {value}\n'
toml_line = '{key} = {value}\n'

toml_map = {str: '""',
            int: str(0),
            float: str(0.0),
            list: '[]'}


