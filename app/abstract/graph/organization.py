import abc
import datetime
import typing

from . import basic


class AbcOrganization(basic.AbcNode, abc.ABC):
    oparl_id: str
    modified: datetime.datetime
    name: str
    start_date: datetime.date
    end_date: datetime.date
    location: basic.AbcRelation
    organization_type: str
    classification: str
    members: typing.Iterable[basic.AbcRelation]
    web_url: str
    parent_organization: basic.AbcRelation
