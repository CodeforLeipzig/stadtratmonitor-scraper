import abc
import datetime
import typing

from . import basic


class AbcPaper(basic.AbcNode, abc.ABC):
    oparl_id: str
    modified: datetime.datetime
    reference: str
    paper_type: str
    web_url: str
    origin_date: datetime.date
    directors: typing.Iterable[basic.AbcRelation]
    originators: typing.Iterable[basic.AbcRelation]
    consultations: typing.Iterable[basic.AbcRelation]
    oparl_thread: basic.AbcRelation
