import typing

from ...abstract.oparl import AbcOparlObject
from ...almanac import singleton
from ...almanac.book.oparl import OPARL_KEY

from .object import OparlObject


@singleton
class OparlFactory:
    def __init__(self):
        self.__registered = {}

    def register(self, key, cls):
        assert issubclass(cls, AbcOparlObject)
        self.__registered.update({key: cls})

    def __call__(self, item) -> typing.Optional[AbcOparlObject]:
        if not item:
            return

        elif isinstance(item, str):
            return OparlObject({OPARL_KEY.ID: item})

        elif isinstance(item, dict):
            oparl_object = self.__registered.get(item.get(OPARL_KEY.TYPE))
            return oparl_object(item)

        elif isinstance(item, AbcOparlObject):
            return item


OparlFactory: OparlFactory
