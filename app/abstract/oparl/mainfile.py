import abc
import datetime

from ...almanac.book.oparl import OPARL_OBJECT

from .oparlobject import AbcOparlObject


class AbcMainFile(AbcOparlObject, abc.ABC, badge=OPARL_OBJECT.MAIN_FILE):
    KIND: str
    ORIGIN_DATE: datetime.datetime
    NAME: str
    MIME_TYPE: str
    SIZE: int
    ACCESS_URL: str
    DOWNLOAD_URL: None
