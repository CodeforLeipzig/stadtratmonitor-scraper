import abc
import datetime

from . import basic


class AbcLocation(basic.AbcNode, abc.ABC):
    oparl_id: str
    modified: datetime.datetime
    locality: str
    postal_code: int
    description: str
    street_address: str

