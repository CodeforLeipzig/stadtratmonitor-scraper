import abc
import typing
import datetime

from ...almanac.book.oparl import OPARL_OBJECT

from .oparlobject import AbcOparlObject


class AbcLocation(AbcOparlObject, abc.ABC, badge=OPARL_OBJECT.LOCATION):
    DESCRIPTION: str
    STREET_ADDRESS: str
    POSTAL_CODE: str
    LOCALITY: str
