from abc import abstractmethod
from ._basic import BasicNodeInterface, DbRelation
from ._scheme import NODES


class LegislativeTerm(BasicNodeInterface):
    def __init__(self, content):
        super().__init__(content, NODES.LEGISLATIVE_TERM)

    @abstractmethod
    def name(self): pass

    @abstractmethod
    def start_date(self): pass

    @abstractmethod
    def end_date(self): pass


class Thread(BasicNodeInterface):
    def __init__(self, content):
        super().__init__(content, NODES.THREAD)

    @abstractmethod
    def subject(self): pass

    @abstractmethod
    def reference(self): pass

    @abstractmethod
    def concerned(self): pass


class Paper(BasicNodeInterface):
    def __init__(self, content):
        super().__init__(content, NODES.PAPER)

    @abstractmethod
    def oparl_id(self): pass

    @abstractmethod
    def modified(self): pass

    @abstractmethod
    def reference(self): pass

    @abstractmethod
    def paper_type(self): pass

    @abstractmethod
    def web_url(self): pass

    @abstractmethod
    def origin_date(self): pass

    @abstractmethod
    def directors(self): pass

    @abstractmethod
    def originators(self): pass

    @abstractmethod
    def consultations(self): pass


class OparlPerson(BasicNodeInterface):
    def __init__(self, content):
        super().__init__(content, NODES.OPARL_PERSON)

    @abstractmethod
    def oparl_id(self): pass

    @abstractmethod
    def modified(self): pass

    @abstractmethod
    def name(self): pass

    @abstractmethod
    def web_url(self): pass


class OparlOrganization(BasicNodeInterface):
    def __init__(self, content):
        super().__init__(content, NODES.OPARL_ORGANIZATION)

    @abstractmethod
    def oparl_id(self): pass

    @abstractmethod
    def modified(self): pass

    @abstractmethod
    def name(self): pass

    @abstractmethod
    def start_date(self): pass

    @abstractmethod
    def end_date(self): pass


class OparlLocation(BasicNodeInterface):
    def __init__(self, content):
        super().__init__(content, NODES.OPARL_LOCATION)

    @abstractmethod
    def oparl_id(self): pass

    @abstractmethod
    def modified(self): pass

    @abstractmethod
    def locality(self): pass

    @abstractmethod
    def postal_code(self): pass

    @abstractmethod
    def description(self): pass

    @abstractmethod
    def street_address(self): pass


class Consultation(BasicNodeInterface):
    def __init__(self, content):
        super().__init__(content, NODES.CONSULTATION)

    @abstractmethod
    def oparl_id(self): pass

    @abstractmethod
    def modified(self): pass

    @abstractmethod
    def paper(self): pass

    @abstractmethod
    def organizations(self): pass

    @abstractmethod
    def authoritative(self): pass

    @abstractmethod
    def role(self): pass


class Membership(DbRelation):
    @abstractmethod
    def oparl_id(self): pass

    @abstractmethod
    def modified(self): pass

    @abstractmethod
    def voting_right(self): pass

    @abstractmethod
    def role(self): pass

    @abstractmethod
    def start_date(self): pass

    @abstractmethod
    def end_date(self): pass
