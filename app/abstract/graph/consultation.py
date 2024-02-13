import abc
import datetime

from . import basic


class AbcConsultation(basic.AbcRelation, abc.ABC):
    oparl_id: str
    modified: datetime.datetime
    authoritative: bool
    role: str

