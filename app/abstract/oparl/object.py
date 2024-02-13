import abc
import datetime
import typing

from . import basic


class Paper(basic.OparlObject, abc.ABC):
    OPARL_ID: str
    OPARL_TYPE: str
    OPARL_BODY: object
    SUBJECT: str
    REFERENCE: str
    ORIGIN_DATE: datetime.datetime
    PAPER_TYPE: str
    MAIN_FILE: object
    ORIGINATOR_PERSONS: typing.Iterable[object]
    UNDER_DIRECTION_OF: object
    CONSULTATIONS: typing.Iterable[object]
    WEB_URL: str
    CREATED: datetime.datetime
    MODIFIED: datetime.datetime
    DELETED: bool


class MainFile(basic.OparlObject, abc.ABC):
    OPARL_ID: str
    OPARL_TYPE: str
    KIND: str
    ORIGIN_DATE: datetime.datetime
    NAME: str
    MIME_TYPE: str
    SIZE: int
    ACCESS_URL: str
    DOWNLOAD_URL: None
    CREATED: datetime.datetime
    MODIFIED: datetime.datetime
    DELETED: bool


class Consultation(basic.OparlObject, abc.ABC):
    OPARL_ID: str
    OPARL_TYPE: str
    PAPER: object
    ORGANIZATIONS: typing.Iterable[object]
    MEETING: object
    AGENDA_ITEM: object
    AUTHORITATIVE: bool
    ROLE: str
    CREATED: datetime.datetime
    MODIFIED: datetime.datetime
    DELETED: bool


class Organization(basic.OparlObject, abc.ABC):
    OPARL_ID: str
    OPARL_TYPE: str
    OPARL_BODY: object
    NAME: str
    SHORT_NAME: str
    LOCATION: object
    START_DATE: datetime.date
    END_DATE: datetime.date
    ORGANIZATION_TYPE: str
    CLASSIFICATION: str
    MEETING: object
    MEMBERSHIPS: typing.Iterable[object]
    WEB_URL: str
    CREATED: datetime.datetime
    MODIFIED: datetime.datetime
    DELETED: bool


class Location(basic.OparlObject, abc.ABC):
    OPARL_ID: str
    OPARL_TYPE: str
    DESCRIPTION: str
    STREET_ADDRESS: str
    POSTAL_CODE: str
    LOCALITY: str
    CREATED: datetime.datetime
    MODIFIED: datetime.datetime
    DELETED: bool


class Person(basic.OparlObject, abc.ABC):
    OPARL_ID: str
    OPARL_TYPE: str
    NAME: str
    FAMILY_NAME: str
    GIVEN_NAME: str
    FORM_OF_ADDRESS: str
    GENDER: str
    LOCATION: object
    LOCATION_OBJECT: object
    STATUS: typing.Iterable[str]
    TITLE: typing.Iterable[str]
    MEMBERSHIPS: typing.Iterable[object]
    WEB_URL: str
    CREATED: datetime.datetime
    MODIFIED: datetime.datetime
    DELETED: bool


class Membership(basic.OparlObject, abc.ABC):
    OPARL_ID: str
    OPARL_TYPE: str
    PERSON: object
    ORGANIZATION: object
    ROLE: str
    VOTING_RIGHT: bool
    START_DATE: datetime.date
    END_DATE: datetime.date
    CREATED: datetime.datetime
    MODIFIED: datetime.datetime
    DELETED: bool
