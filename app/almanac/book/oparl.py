import datetime
import typing

from ..generic import Book, Constant, singleton, init_annotations


@singleton
class OPARL_KEY(Book):
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


@singleton
class OPARL_OBJECT(Book, initializer=init_annotations):
    CONSULTATION: Constant
    LOCATION: Constant
    MAIN_FILE: Constant
    MEMBERSHIP: Constant
    ORGANIZATION: Constant
    PAPER: Constant
    PERSON: Constant


class Paper:
    OPARL_ID: str = OPARL_KEY.ID
    OPARL_TYPE: str = OPARL_KEY.TYPE
    OPARL_BODY: object = OPARL_KEY.BODY
    SUBJECT: str = OPARL_KEY.NAME
    REFERENCE: str = OPARL_KEY.REFERENCE
    ORIGIN_DATE: datetime.datetime = OPARL_KEY.DATE
    PAPER_TYPE: str = OPARL_KEY.PAPER_TYPE
    MAIN_FILE: object = OPARL_KEY.MAIN_FILE
    ORIGINATOR_PERSONS: typing.Iterable[object] = OPARL_KEY.ORIGINATOR_PERSON
    UNDER_DIRECTION_OF: object = OPARL_KEY.UNDER_DIRECTION_OF
    CONSULTATIONS: typing.Iterable[object] = OPARL_KEY.CONSULTATION
    WEB_URL: str = OPARL_KEY.WEB
    CREATED: datetime.datetime = OPARL_KEY.CREATED
    MODIFIED: datetime.datetime = OPARL_KEY.MODIFIED
    DELETED: bool = OPARL_KEY.DELETED


class MainFile:
    OPARL_ID: str = OPARL_KEY.ID
    OPARL_TYPE: str = OPARL_KEY.TYPE
    KIND: str = OPARL_KEY.NAME
    ORIGIN_DATE: datetime.datetime = OPARL_KEY.DATE
    NAME: str = OPARL_KEY.FILE_NAME
    MIME_TYPE: str = OPARL_KEY.MIME_TYPE
    SIZE: int = OPARL_KEY.SIZE
    ACCESS_URL: str = OPARL_KEY.ACCESS_URL
    DOWNLOAD_URL: None = OPARL_KEY.DOWNLOAD_URL
    CREATED: datetime.datetime = OPARL_KEY.CREATED
    MODIFIED: datetime.datetime = OPARL_KEY.MODIFIED
    DELETED: bool = OPARL_KEY.DELETED


class Consultation:
    OPARL_ID: str = OPARL_KEY.ID
    OPARL_TYPE: str = OPARL_KEY.TYPE
    PAPER: object = OPARL_KEY.PAPER
    ORGANIZATIONS: typing.Iterable[object] = OPARL_KEY.ORGANIZATION
    MEETING: object = 'meeting'
    AGENDA_ITEM: object = 'agendaItem'
    AUTHORITATIVE: bool = 'authoritative'
    ROLE: str = 'role'
    CREATED: datetime.datetime = OPARL_KEY.CREATED
    MODIFIED: datetime.datetime = OPARL_KEY.MODIFIED
    DELETED: bool = OPARL_KEY.DELETED


class Organization:
    OPARL_ID: str = OPARL_KEY.ID
    OPARL_TYPE: str = OPARL_KEY.TYPE
    OPARL_BODY: object = OPARL_KEY.BODY
    NAME: str = OPARL_KEY.NAME
    SHORT_NAME: str = OPARL_KEY.SHORT_NAME
    LOCATION: object = OPARL_KEY.LOCATION
    START_DATE: datetime.date = OPARL_KEY.START_DATE
    END_DATE: datetime.date = OPARL_KEY.END_DATE
    ORGANIZATION_TYPE: str = OPARL_KEY.ORGANIZATION_TYPE
    CLASSIFICATION: str = OPARL_KEY.CLASSIFICATION
    MEETING: object = OPARL_KEY.MEETING
    MEMBERSHIPS: typing.Iterable[object] = OPARL_KEY.MEMBERSHIP
    WEB_URL: str = OPARL_KEY.WEB
    CREATED: datetime.datetime = OPARL_KEY.CREATED
    MODIFIED: datetime.datetime = OPARL_KEY.MODIFIED
    DELETED: bool = OPARL_KEY.DELETED


class Location:
    OPARL_ID: str = OPARL_KEY.ID
    OPARL_TYPE: str = OPARL_KEY.TYPE
    DESCRIPTION: str = OPARL_KEY.DESCRIPTION
    STREET_ADDRESS: str = OPARL_KEY.STREET_ADDRESS
    POSTAL_CODE: str = OPARL_KEY.POSTAL_CODE
    LOCALITY: str = OPARL_KEY.LOCALITY
    CREATED: datetime.datetime = OPARL_KEY.CREATED
    MODIFIED: datetime.datetime = OPARL_KEY.MODIFIED
    DELETED: bool = OPARL_KEY.DELETED


class Person:
    OPARL_ID: str = OPARL_KEY.ID
    OPARL_TYPE: str = OPARL_KEY.TYPE
    NAME: str = OPARL_KEY.NAME
    FAMILY_NAME: str = OPARL_KEY.FAMILY_NAME
    GIVEN_NAME: str = OPARL_KEY.GIVEN_NAME
    FORM_OF_ADDRESS: str = OPARL_KEY.FORM_OF_ADDRESS
    GENDER: str = OPARL_KEY.GENDER
    LOCATION: object = OPARL_KEY.LOCATION
    LOCATION_OBJECT: object = OPARL_KEY.LOCATION_OBJECT
    STATUS: typing.Iterable[str] = OPARL_KEY.STATUS
    TITLE: typing.Iterable[str] = OPARL_KEY.TITLE
    MEMBERSHIPS: typing.Iterable[object] = OPARL_KEY.MEMBERSHIP
    WEB_URL: str = OPARL_KEY.WEB
    CREATED: datetime.datetime = OPARL_KEY.CREATED
    MODIFIED: datetime.datetime = OPARL_KEY.MODIFIED
    DELETED: bool = OPARL_KEY.DELETED


class Membership:
    OPARL_ID:   str = OPARL_KEY.ID
    OPARL_TYPE: str = OPARL_KEY.TYPE
    PERSON: object = OPARL_KEY.PERSON
    ORGANIZATION: object = OPARL_KEY.ORGANIZATION
    ROLE: str = OPARL_KEY.ROLE
    VOTING_RIGHT: bool = OPARL_KEY.VOTING_RIGHT
    START_DATE: datetime.date = OPARL_KEY.START_DATE
    END_DATE: datetime.date = OPARL_KEY.END_DATE
    CREATED: datetime.datetime = OPARL_KEY.CREATED
    MODIFIED: datetime.datetime = OPARL_KEY.MODIFIED
    DELETED: bool = OPARL_KEY.DELETED
