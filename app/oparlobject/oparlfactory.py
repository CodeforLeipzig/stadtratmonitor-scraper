import typing

from app.abstract.oparl import AbcOparlObject
from app.almanac import singleton
from app.almanac.book.oparl import OPARL_KEY, OPARL_OBJECT

from .oparlobject import OparlObject

oparl_type_mapping = {
    "https://schema.oparl.org/1.1/Consultation": OPARL_OBJECT.CONSULTATION,
    "https://schema.oparl.org/1.1/Location": OPARL_OBJECT.LOCATION,
    "https://schema.oparl.org/1.1/File": OPARL_OBJECT.MAIN_FILE,
    "https://schema.oparl.org/1.1/Membership": OPARL_OBJECT.MEMBERSHIP,
    "https://schema.oparl.org/1.1/Organization": OPARL_OBJECT.ORGANIZATION,
    "https://schema.oparl.org/1.1/Paper": OPARL_OBJECT.PAPER,
    "https://schema.oparl.org/1.1/Person": OPARL_OBJECT.PERSON
}


@singleton
class OparlFactory:
    def __init__(self):
        self.__registered = {}
        self.__oparl_type_mapping = oparl_type_mapping

    def __call__(self, item) -> typing.Optional[AbcOparlObject]:
        if not item:
            return OparlObject({})

        elif isinstance(item, str):
            return OparlObject({OPARL_KEY.ID: item})

        elif isinstance(item, dict):
            oparl_type = item.get(OPARL_KEY.TYPE)
            badge = self.__oparl_type_mapping.get(oparl_type)
            oparl_object = self.__registered.get(badge)
            return oparl_object(item)

        elif isinstance(item, AbcOparlObject):
            return item

    def register(self, key, cls):
        assert issubclass(cls, AbcOparlObject)
        self.__registered.update({key: cls})
