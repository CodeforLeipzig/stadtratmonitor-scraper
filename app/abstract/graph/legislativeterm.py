import abc
import datetime

from . import basic


class AbcLegislativeTerm(basic.AbcNode, abc.ABC):
    name: str
    start_date: datetime.date
    end_date: datetime.date
