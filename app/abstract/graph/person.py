import abc
import datetime

from . import basic


class AbcPerson(basic.AbcNode, abc.ABC):
    oparl_id: str
    modified: datetime.datetime
    name: str
    web_url: str
    location: basic.AbcRelation
    status: str
    title: str

