from app.almanac.book.oparl import OPARL_KEY, singleton

from .propertyfactory import OparlProperty
from .propertyconverter import *


@singleton
class PropertyStore:
    def __init__(self):
        for key, work in filter(lambda x: not x[0].startswith('_'), self.__class__.__dict__.items()):
            property_key = getattr(OPARL_KEY, key)
            work = work if isinstance(work, typing.Iterable) else (work, )
            setattr(self, key, OparlProperty(property_key, *work))

    ACCESS_URL = to_str
    AGENDA_ITEM: object = always_none
    AUTHORITATIVE = to_bool
    BODY: int = always_none
    CLASSIFICATION = to_str
    CONSULTATION = to_object_generator
    CREATED = to_datetime
    DATE = to_datetime
    DELETED = to_bool
    DESCRIPTION = to_str
    DOWNLOAD_URL = to_str
    END_DATE = to_date
    FAMILY_NAME = to_str
    FILE_NAME = to_str
    FORM_OF_ADDRESS = to_str
    GENDER = to_str
    GIVEN_NAME = to_str
    ID = to_str
    LOCATION_OBJECT = to_object
    LOCATION = to_object
    LOCALITY = to_str
    MAIN_FILE = to_object
    MEETING = to_object
    MEMBERSHIP = to_object_generator
    MIME_TYPE = to_str
    MODIFIED = to_datetime
    NAME = to_str
    ORIGINATOR_PERSON = to_generator
    ORGANIZATION = to_object
    ORGANIZATION_TYPE = to_str
    PAPER = to_object
    PAPER_TYPE = to_str
    PERSON = to_object
    POSTAL_CODE = to_str
    REFERENCE = to_str
    ROLE = to_str
    SHORT_NAME = to_str
    SIZE = to_int
    START_DATE = to_datetime
    STATUS = to_str
    STREET_ADDRESS = to_str
    SUB_ORGANIZATION_OF = to_object
    TITLE = to_generator
    TYPE = to_str
    UNDER_DIRECTION_OF = to_object
    VOTING_RIGHT = to_bool
    WEB = to_str
