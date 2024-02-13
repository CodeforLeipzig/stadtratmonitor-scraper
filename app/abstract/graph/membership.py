import abc
import datetime

from . import basic


class AbcMembership(basic.AbcRelation, abc.ABC):
    oparl_id: str
    modified: datetime.datetime
    voting_right: bool
    role: str
    start_date: datetime.date
    end_date: datetime.date
