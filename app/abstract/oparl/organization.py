import abc
import typing
import datetime

from ...almanac.book.oparl import OPARL_OBJECT

from .oparlobject import AbcOparlObject


class AbcOrganization(AbcOparlObject, abc.ABC, badge=OPARL_OBJECT.ORGANIZATION):
    OPARL_BODY: AbcOparlObject
    NAME: str
    SHORT_NAME: str
    LOCATION: AbcOparlObject
    START_DATE: datetime.date
    END_DATE: datetime.date
    ORGANIZATION_TYPE: str
    CLASSIFICATION: str
    MEETING: AbcOparlObject
    MEMBERSHIPS: typing.Iterable[AbcOparlObject]
    WEB_URL: str
