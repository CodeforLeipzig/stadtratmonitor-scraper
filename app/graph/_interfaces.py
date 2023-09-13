import datetime as dt
from abc import abstractmethod
from ._basic import BasicNodeInterface, DbRelation
from ._scheme import NODES


class LegislativeTerm(BasicNodeInterface):
    def __init__(self, content):
        super().__init__(content, NODES.LEGISLATIVE_TERM)

    @abstractmethod
    def name(self) -> str:
        """define name property"""
        pass

    @abstractmethod
    def start_date(self) -> dt.date:
        """define start date property"""
        pass

    @abstractmethod
    def end_date(self) -> dt.date:
        """define end date property"""
        pass


class Thread(BasicNodeInterface):
    def __init__(self, content):
        super().__init__(content, NODES.THREAD)

    @abstractmethod
    def subject(self) -> str:
        """define subject property"""
        pass

    @abstractmethod
    def reference(self) -> int:
        """define reference property"""
        pass

    @abstractmethod
    def legis_term(self) -> tuple:
        """define concerned relation
        cypher: (thread) - [concerned] -> (legislative term)"""
        pass


class Paper(BasicNodeInterface):
    def __init__(self, content):
        super().__init__(content, NODES.PAPER)

    @abstractmethod
    def oparl_id(self) -> str:
        """define oparl id property"""
        pass

    @abstractmethod
    def modified(self) -> dt.datetime:
        """define modified property"""
        pass

    @abstractmethod
    def reference(self) -> str:
        """define reference property"""
        pass

    @abstractmethod
    def paper_type(self) -> str:
        """define paper type property"""
        pass

    @abstractmethod
    def web_url(self) -> str:
        """define web url property"""
        pass

    @abstractmethod
    def origin_date(self) -> dt.date:
        """define origin date property"""
        pass

    @abstractmethod
    def directors(self) -> tuple:
        """define directed relation
        cypher: (named entity) - [directed] -> (paper)"""
        pass

    @abstractmethod
    def originators(self) -> tuple:
        """define induced relation
        cypher: (named entity) - [induced] -> (paper)"""
        pass

    @abstractmethod
    def consultations(self) -> tuple:
        """define concerned relation
        cypher: (named entity) - [concerned] -> (paper)"""
        pass

    @abstractmethod
    def oparl_thread(self) -> tuple:
        """define concerned relation
        cypher: (paper) - [concerned] -> (thread)"""
        pass


class OparlPerson(BasicNodeInterface):
    def __init__(self, content):
        super().__init__(content, NODES.OPARL_PERSON)

    @abstractmethod
    def oparl_id(self) -> str:
        """define oparl id property"""
        pass

    @abstractmethod
    def modified(self) -> dt.datetime:
        """define modified property"""
        pass

    @abstractmethod
    def name(self) -> str:
        """define name property"""
        pass

    @abstractmethod
    def web_url(self) -> str:
        """define web url property"""
        pass

    @abstractmethod
    def location(self) -> tuple:
        """define located relation
        cypher: (Person) - [located] -> (Location)"""
        pass

    @abstractmethod
    def status(self) -> str:
        """define status property"""
        pass

    @abstractmethod
    def title(self) -> str:
        """define status property"""
        pass


class OparlOrganization(BasicNodeInterface):
    def __init__(self, content):
        super().__init__(content, NODES.OPARL_ORGANIZATION)

    @abstractmethod
    def oparl_id(self) -> str:
        """define oparl id property"""
        pass

    @abstractmethod
    def modified(self) -> dt.datetime:
        """define modified property"""
        pass

    @abstractmethod
    def name(self) -> str:
        """define name property"""
        pass

    @abstractmethod
    def start_date(self) -> dt.date:
        """define start date property"""
        pass

    @abstractmethod
    def end_date(self) -> dt.date:
        """define end date property"""
        pass

    @abstractmethod
    def location(self) -> tuple:
        """define located relation
        cypher: (Organization) -[located] -> (Location)"""
        pass

    @abstractmethod
    def organization_type(self) -> str:
        """define organization type property"""
        pass

    @abstractmethod
    def classification(self) -> str:
        """define classification property"""
        pass

    @abstractmethod
    def members(self) -> tuple:
        """define is_member relation
        cypher (Person) - [is_member] -> (Organization))"""
        pass

    @abstractmethod
    def web_url(self) -> str:
        """define web url property"""
        pass

    @abstractmethod
    def parent_organization(self) -> tuple:
        """define is_member relation
        cypher: (Organization) - [is_member] -> (Organization)"""
        pass


class OparlLocation(BasicNodeInterface):
    def __init__(self, content):
        super().__init__(content, NODES.OPARL_LOCATION)

    @abstractmethod
    def oparl_id(self) -> str:
        """define oparl id property"""
        pass

    @abstractmethod
    def modified(self) -> dt.datetime:
        """define modified property"""
        pass

    @abstractmethod
    def locality(self) -> str:
        """define locality property"""
        pass

    @abstractmethod
    def postal_code(self) -> int:
        """define postal code property"""
        pass

    @abstractmethod
    def description(self) -> str:
        """define description property"""
        pass

    @abstractmethod
    def street_address(self) -> str:
        """define street address property"""
        pass


class Consultation(DbRelation):

    @abstractmethod
    def oparl_id(self) -> str:
        """define oparl ip property"""
        pass

    @abstractmethod
    def modified(self) -> dt.datetime:
        """define modified property"""
        pass

    @abstractmethod
    def authoritative(self) -> bool:
        """define authoritative property"""
        pass

    @abstractmethod
    def role(self) -> str:
        """define role property"""
        pass


class Membership(DbRelation):
    @abstractmethod
    def oparl_id(self) -> str:
        """define oparl id property"""
        pass

    @abstractmethod
    def modified(self) -> dt.datetime:
        """define modified property"""
        pass

    @abstractmethod
    def voting_right(self) -> bool:
        """define voting right property"""
        pass

    @abstractmethod
    def role(self) -> str:
        """define role property"""
        pass

    @abstractmethod
    def start_date(self) -> dt.date:
        """define start date property"""
        pass

    @abstractmethod
    def end_date(self) -> dt.date:
        """define end date property"""
        pass
