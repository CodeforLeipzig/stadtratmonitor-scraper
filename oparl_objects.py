from typing import Generator
from datetime import date, datetime
from re import findall


def as_date_type(func):
    def convert_date(*args) -> date:
        date_str = func(*args)
        return date.fromisoformat(date_str) if date_str else None

    return convert_date


def as_datetime_type(func):
    def convert_datetime(*args) -> date:
        date_str = func(*args)
        return datetime.fromisoformat(date_str) if date_str else None

    return convert_datetime


def as_simple_generator(func):
    def generator(*args) -> Generator:
        item = func(*args)
        if isinstance(item, list):
            for sub_item in item:
                if sub_item:
                    yield sub_item
    return generator


def as_oparl_object(func):
    def oparl_object(*args):
        return oparl_factory(func(*args))
    return oparl_object


def as_oparl_object_generator(func):
    def oparl_object_generator(*args):
        for item in as_simple_generator(func)(*args):
            yield oparl_factory(item)
    return oparl_object_generator


class BasicOparl:
    _content: dict

    def __init__(self, content: dict):
        self._content = content

    @property
    def oparl_id(self) -> str:
        return self._content.get('id')

    @property
    def oparl_type(self) -> str:
        return self._content.get('type')

    @property
    @as_datetime_type
    def modified(self):
        return self._content.get('modified')

    @property
    def is_deleted(self):
        return self._content.get('deleted')


class UnknownOparl(BasicOparl):
    pass


class Paper(BasicOparl):
    @property
    def subject(self) -> str:
        return self._content.get('name')

    @property
    def reference(self) -> str:
        return self._content.get('reference')

    @property
    def legis_term(self) -> str:
        reference = self.reference
        if isinstance(reference, str):
            hits = findall('^[XIV]+', reference)
            return hits[0] if hits else None

    @property
    def thread_number(self) -> str:
        reference = self.reference
        if isinstance(reference, str):
            hits = findall('\d{5}', reference)
            return hits[0] if hits else None

    @property
    @as_date_type
    def origin_date(self):
        return self._content.get('date')

    @property
    def paper_type(self) -> str:
        return self._content.get('paperType')

    @property
    def file_url(self) -> str:
        main_file = self._content.get('mainFile')
        if isinstance(main_file, dict) and not main_file.get('deleted'):
            return main_file.get('accessUrl')

    @property
    @as_oparl_object_generator
    def originator_persons(self):
        return self._content.get('originatorPerson')

    @property
    @as_oparl_object_generator
    def under_direction_of(self):
        return self._content.get('underDirectionOf')

    @property
    @as_oparl_object_generator
    def consultations(self):
        return self._content.get('consultations')

    @property
    def web_url(self) -> str:
        return self._content.get('web')


class Person(BasicOparl):
    @property
    def name(self) -> str:
        return self._content.get('name')

    @property
    @as_oparl_object
    def location(self) -> (str, dict):
        loc_obj = self._content.get('locationObject')
        if loc_obj:
            return loc_obj
        else:
            return self._content.get('location')

    @property
    @as_simple_generator
    def status(self):
        return self._content.get('status')

    @property
    def web_url(self) -> str:
        return self._content.get('web')

    @property
    @as_oparl_object_generator
    def memberships(self):
        return self._content.get('membership')


class Organization(BasicOparl):
    @property
    def name(self) -> str:
        return self._content.get('name')

    @property
    @as_oparl_object
    def location(self) -> (str, dict):
        loc_obj = self._content.get('locationObject')
        if loc_obj:
            return loc_obj
        else:
            return self._content.get('location')

    @property
    @as_date_type
    def start_date(self):
        return self._content.get('startDate')

    @property
    @as_date_type
    def end_date(self):
        return self._content.get('endDate')

    @property
    @as_oparl_object_generator
    def memberships(self):
        return self._content.get('membership')


class Location(BasicOparl):
    @property
    def locality(self) -> str:
        return self._content.get('locality')

    @property
    def postal_code(self) -> str:
        return self._content.get('postalCode')

    @property
    def description(self) -> str:
        return self._content.get('description')

    @property
    def street_address(self) -> str:
        return self._content.get('streetAddress')


class Membership(BasicOparl):
    @property
    @as_oparl_object
    def person(self) -> (str, dict):
        return self._content.get('person')

    @property
    @as_oparl_object
    def organization(self) -> (str, dict):
        return self._content.get('organization')

    @property
    def voting_right(self) -> bool:
        return self._content.get('votingRight')

    @property
    def role(self) -> str:
        return self._content.get('role')

    @property
    @as_date_type
    def start_date(self):
        return self._content.get('startDate')

    @property
    @as_date_type
    def end_date(self):
        return self._content.get('endDate')


fabric_dict = {"https://schema.oparl.org/1.1/Paper": Paper,
               "https://schema.oparl.org/1.1/Person": Person,
               "https://schema.oparl.org/1.1/Organization": Organization,
               "https://schema.oparl.org/1.1/Location": Location,
               "https://schema.oparl.org/1.1/Membership": Membership}


def oparl_factory(item: (str, dict)):
    if item is None:
        return
    elif isinstance(item, str) and item.startswith('http'):
        return UnknownOparl(dict(id=item))
    elif isinstance(item, dict):
        object_type = item.get('type')
        assert object_type is not None
        oparl_object = fabric_dict.get(object_type)
        return oparl_object(item)
    else:
        message = f'unsupported item {item} type {type(item)}, expected url_str or dict with key "type"'
        raise TypeError(message)
