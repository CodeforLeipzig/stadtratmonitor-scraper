import abc
import typing
import datetime

from ...almanac.book.oparl import OPARL_OBJECT

from .oparlobject import AbcOparlObject


class AbcMembership(AbcOparlObject, abc.ABC, badge=OPARL_OBJECT.MEMBERSHIP):
    PERSON: AbcOparlObject
    ORGANIZATION: AbcOparlObject
    ROLE: str
    VOTING_RIGHT: bool
    START_DATE: datetime.date
    END_DATE: datetime.date
