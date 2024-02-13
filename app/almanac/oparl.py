import datetime
import typing

from .basic import book


@book.overwrite
class KEY(book.Book):
    ACCESS_URL: str = 'accessUrl'
    AGENDA_ITEM: object = 'agendaItem'
    AUTHORITATIVE: bool = 'authoritative'
    BODY: int = 'body'
    CLASSIFICATION: str = 'classification'
    CONSULTATION: typing.Iterable[object] = 'consultation'
    CREATED: datetime.datetime = 'created'
    DATE: datetime.datetime = 'date'
    DELETED: bool = 'deleted'
    DESCRIPTION: str = 'description'
    DOWNLOAD_URL: str = 'downloadUrl'
    END_DATE: datetime.date = 'endDate'
    FAMILY_NAME: str = 'familyName'
    FILE_NAME: str = 'fileName'
    # noinspection SpellCheckingInspection
    FORM_OF_ADDRESS: str = 'formOfAdress'
    GENDER: str = 'gender'
    GIVEN_NAME: str = 'givenName'
    ID: str = 'id'
    LOCATION_OBJECT: object = 'locationObject'
    LOCATION: object = 'location'
    LOCALITY: str = 'locality'
    MAIN_FILE: object = 'mainFile'
    MEETING: object = 'meeting'
    MEMBERSHIP: typing.Iterable[object] = 'membership'
    MIME_TYPE: str = 'mimeType'
    MODIFIED: datetime.datetime = 'modified'
    NAME: str = 'name'
    ORIGINATOR_PERSON: typing.Iterable[object] = 'originatorPerson'
    ORGANIZATION: object = 'organization'
    ORGANIZATION_TYPE: str = 'organizationType'
    PAPER: object = 'paper'
    PAPER_TYPE: str = 'paperType'
    PERSON: object = 'person'
    POSTAL_CODE: str = 'postalCode'
    REFERENCE: str = 'reference'
    ROLE: str = 'role'
    SHORT_NAME: str = 'shortName'
    SIZE: int = 'size'
    START_DATE: datetime.date = 'startDate'
    STATUS: str = 'status'
    STREET_ADDRESS: str = 'streetAddress'
    SUB_ORGANIZATION_OF: object = 'subOrganizationOf'
    TITLE: typing.Iterable[str] = 'title'
    TYPE: str = 'type'
    UNDER_DIRECTION_OF: object = 'underDirectionOf'
    VOTING_RIGHT: bool = 'votingRight'
    WEB: str = 'web'

# TODO: move the following away
# LEGISLATIVE_TERM: str = '-'
# THREAD_NUMBER: int = '-'


@book.overwrite
class OBJECT(book.Book, initializer=book.init_annotations):
    CONSULTATION: book.Constant
    LOCATION: book.Constant
    MEMBERSHIP: book.Constant
    ORGANIZATION: book.Constant
    PAPER: book.Constant
    PERSON: book.Constant


class Paper:
    OPARL_ID: str = KEY.ID
    OPARL_TYPE: str = KEY.TYPE
    OPARL_BODY: object = KEY.BODY
    SUBJECT: str = KEY.NAME
    REFERENCE: str = KEY.REFERENCE
    ORIGIN_DATE: datetime.datetime = KEY.DATE
    PAPER_TYPE: str = KEY.PAPER_TYPE
    MAIN_FILE: object = KEY.MAIN_FILE
    ORIGINATOR_PERSONS: typing.Iterable[object] = KEY.ORIGINATOR_PERSON
    UNDER_DIRECTION_OF: object = KEY.UNDER_DIRECTION_OF
    CONSULTATIONS: typing.Iterable[object] = KEY.CONSULTATION
    WEB_URL: str = KEY.WEB
    CREATED: datetime.datetime = KEY.CREATED
    MODIFIED: datetime.datetime = KEY.MODIFIED
    DELETED: bool = KEY.DELETED


class MainFile:
    OPARL_ID: str = KEY.ID
    OPARL_TYPE: str = KEY.TYPE
    KIND: str = KEY.NAME
    ORIGIN_DATE: datetime.datetime = KEY.DATE
    NAME: str = KEY.FILE_NAME
    MIME_TYPE: str = KEY.MIME_TYPE
    SIZE: int = KEY.SIZE
    ACCESS_URL: str = KEY.ACCESS_URL
    DOWNLOAD_URL: None = KEY.DOWNLOAD_URL
    CREATED: datetime.datetime = KEY.CREATED
    MODIFIED: datetime.datetime = KEY.MODIFIED
    DELETED: bool = KEY.DELETED


class Consultation:
    OPARL_ID: str = KEY.ID
    OPARL_TYPE: str = KEY.TYPE
    PAPER: object = KEY.PAPER
    ORGANIZATIONS: typing.Iterable[object] = KEY.ORGANIZATION
    MEETING: object = 'meeting'
    AGENDA_ITEM: object = 'agendaItem'
    AUTHORITATIVE: bool = 'authoritative'
    ROLE: str = 'role'
    CREATED: datetime.datetime = KEY.CREATED
    MODIFIED: datetime.datetime = KEY.MODIFIED
    DELETED: bool = KEY.DELETED


class Organization:
    OPARL_ID: str = KEY.ID
    OPARL_TYPE: str = KEY.TYPE
    OPARL_BODY: object = KEY.BODY
    NAME: str = KEY.NAME
    SHORT_NAME: str = KEY.SHORT_NAME
    LOCATION: object = KEY.LOCATION
    START_DATE: datetime.date = KEY.START_DATE
    END_DATE: datetime.date = KEY.END_DATE
    ORGANIZATION_TYPE: str = KEY.ORGANIZATION_TYPE
    CLASSIFICATION: str = KEY.CLASSIFICATION
    MEETING: object = KEY.MEETING
    MEMBERSHIPS: typing.Iterable[object] = KEY.MEMBERSHIP
    WEB_URL: str = KEY.WEB
    CREATED: datetime.datetime = KEY.CREATED
    MODIFIED: datetime.datetime = KEY.MODIFIED
    DELETED: bool = KEY.DELETED


class Location:
    OPARL_ID: str = KEY.ID
    OPARL_TYPE: str = KEY.TYPE
    DESCRIPTION: str = KEY.DESCRIPTION
    STREET_ADDRESS: str = KEY.STREET_ADDRESS
    POSTAL_CODE: str = KEY.POSTAL_CODE
    LOCALITY: str = KEY.LOCALITY
    CREATED: datetime.datetime = KEY.CREATED
    MODIFIED: datetime.datetime = KEY.MODIFIED
    DELETED: bool = KEY.DELETED


class Person:
    OPARL_ID: str = KEY.ID
    OPARL_TYPE: str = KEY.TYPE
    NAME: str = KEY.NAME
    FAMILY_NAME: str = KEY.FAMILY_NAME
    GIVEN_NAME: str = KEY.GIVEN_NAME
    FORM_OF_ADDRESS: str = KEY.FORM_OF_ADDRESS
    GENDER: str = KEY.GENDER
    LOCATION: object = KEY.LOCATION
    LOCATION_OBJECT: object = KEY.LOCATION_OBJECT
    STATUS: typing.Iterable[str] = KEY.STATUS
    TITLE: typing.Iterable[str] = KEY.TITLE
    MEMBERSHIPS: typing.Iterable[object] = KEY.MEMBERSHIP
    WEB_URL: str = KEY.WEB
    CREATED: datetime.datetime = KEY.CREATED
    MODIFIED: datetime.datetime = KEY.MODIFIED
    DELETED: bool = KEY.DELETED


class MEMBERSHIP:
    OPARL_ID: str = KEY.ID
    OPARL_TYPE: str = KEY.TYPE
    PERSON: object = KEY.PERSON
    ORGANIZATION: object = KEY.ORGANIZATION
    ROLE: str = KEY.ROLE
    VOTING_RIGHT: bool = KEY.VOTING_RIGHT
    START_DATE: datetime.date = KEY.START_DATE
    END_DATE: datetime.date = KEY.END_DATE
    CREATED: datetime.datetime = KEY.CREATED
    MODIFIED: datetime.datetime = KEY.MODIFIED
    DELETED: bool = KEY.DELETED
