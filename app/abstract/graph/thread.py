import abc

from . import basic


class AbcThread(basic.AbcNode, abc.ABC):
    subject: str
    reference: int
    legis_term: basic.AbcRelation
