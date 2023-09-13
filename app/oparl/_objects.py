from re import findall
from ._factory import Factory

as_oparl_object = Factory.as_oparl_object
as_simple_generator = Factory.as_simple_generator
as_oparl_object_generator = Factory.as_oparl_object_generator
as_date_type = Factory.as_date_type
as_datetime_type = Factory.as_datetime_type


class Basic:
    _content: dict

    def __init__(self, content: dict):
        self._content = content

    def __eq__(self, other):
        if self is other or \
                isinstance(other, self.__class__) and \
                self.oparl_id == other.oparl_id and \
                self.oparl_type == other.oparl_type and \
                self.modified == other.modified:
            return True
        else:
            return False

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
    def is_valid(self):
        return self.oparl_type and self.oparl_id and not self._content.get('deleted')


class Paper(Basic):
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
        return self._content.get('consultation')

    @property
    def web_url(self) -> str:
        return self._content.get('web')


class Person(Basic):
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


class Organization(Basic):
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

    @property
    def organization_type(self):
        return self._content.get('organizationType')

    @property
    def classification(self):
        return self._content.get('classification')

    @property
    def web_url(self):
        return self._content.get('web')

    @property
    @as_oparl_object
    def parent_organization(self):
        return self._content.get('subOrganizationOf')


class Location(Basic):
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


class Membership(Basic):
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


class Consultation(Basic):
    # 'meeting'
    # 'agendaItem'
    @property
    @as_oparl_object
    def paper(self):
        return self._content.get('paper')

    @property
    @as_oparl_object_generator
    def organizations(self):
        return self._content.get('organization')

    @property
    def authoritative(self):
        return self._content.get('authoritative')

    @property
    def role(self):
        return self._content.get('role')
