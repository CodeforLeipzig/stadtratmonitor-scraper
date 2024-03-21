import abc
import typing
import datetime

from ...almanac.book.oparl import OPARL_OBJECT

from .oparlobject import AbcOparlObject


class AbcPaper(AbcOparlObject, abc.ABC, badge=OPARL_OBJECT.PAPER):
    OPARL_BODY: AbcOparlObject
    SUBJECT: str
    REFERENCE: str
    ORIGIN_DATE: datetime.datetime
    PAPER_TYPE: str
    MAIN_FILE: AbcOparlObject
    ORIGINATOR_PERSONS: typing.Iterable[AbcOparlObject]
    UNDER_DIRECTION_OF: AbcOparlObject
    CONSULTATIONS: typing.Iterable[AbcOparlObject]
    WEB_URL: str
