import abc
import typing
import datetime

from ...almanac.book.oparl import OPARL_OBJECT

from .oparlobject import AbcOparlObject


class AbcPerson(AbcOparlObject, abc.ABC, badge=OPARL_OBJECT.PERSON):
    NAME: str
    FAMILY_NAME: str
    GIVEN_NAME: str
    FORM_OF_ADDRESS: str
    GENDER: str
    LOCATION: AbcOparlObject
    LOCATION_OBJECT: AbcOparlObject
    STATUS: typing.Iterable[str]
    TITLE: typing.Iterable[str]
    MEMBERSHIPS: typing.Iterable[AbcOparlObject]
    WEB_URL: str
