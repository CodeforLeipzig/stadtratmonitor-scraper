import abc
import typing

from ...almanac.book.oparl import OPARL_OBJECT

from .oparlobject import AbcOparlObject


class AbcConsultation(AbcOparlObject, abc.ABC, badeg=OPARL_OBJECT.CONSULTATION):
    PAPER: AbcOparlObject
    ORGANIZATIONS: typing.Iterable[AbcOparlObject]
    MEETING: AbcOparlObject
    AGENDA_ITEM: AbcOparlObject
    AUTHORITATIVE: bool
    ROLE: str


