from .schema import RELATIONS, ATTRIBUTES
from ._entity import Node
from . import _interfaces as ifs
from .. import oparl


class LegislativeTermNode(ifs.LegislativeTerm):
    _content: oparl.Paper

    @ATTRIBUTES.NAME.as_primary
    def name(self):
        return self._content.legis_term

    @ATTRIBUTES.START_DATE
    def start_date(self): pass

    @ATTRIBUTES.END_DATE
    def end_date(self): pass


class ThreadNode(ifs.Thread):
    _content: oparl.Paper

    @ATTRIBUTES.NAME
    def subject(self):
        return self._content.subject

    @ATTRIBUTES.REFERENCE.as_primary
    def reference(self):
        return self._content.thread_number

    @RELATIONS.IN_PERIOD
    def legis_term(self):
        return self, LegislativeTermNode(self._content)


class ConsultationRelation(ifs.Consultation):
    _content: oparl.Consultation

    @ATTRIBUTES.OPARL_ID
    def oparl_id(self):
        return self._content.oparl_id

    @ATTRIBUTES.MODIFIED
    def modified(self):
        return self._content.modified

    @ATTRIBUTES.AUTHORITATIVE
    def authoritative(self):
        return self._content.authoritative

    @ATTRIBUTES.ROLE
    def role(self):
        return self._content.role


class MembershipRelation(ifs.Membership):
    _content: oparl.Membership

    @ATTRIBUTES.OPARL_ID.as_primary
    def oparl_id(self):
        return self._content.oparl_id

    @ATTRIBUTES.MODIFIED
    def modified(self):
        return self._content.modified

    @ATTRIBUTES.VOTING_RIGHT
    def voting_right(self):
        return self._content.voting_right

    @ATTRIBUTES.ROLE
    def role(self):
        return self._content.role

    @ATTRIBUTES.START_DATE
    def start_date(self):
        return self._content.start_date

    @ATTRIBUTES.END_DATE
    def end_date(self):
        return self._content.end_date


class PaperNode(ifs.Paper):
    _content: oparl.Paper

    @ATTRIBUTES.OPARL_ID.as_primary
    def oparl_id(self):
        return self._content.oparl_id

    @ATTRIBUTES.MODIFIED
    def modified(self):
        return self._content.modified

    @ATTRIBUTES.REFERENCE.as_primary
    def reference(self):
        return self._content.reference

    @ATTRIBUTES.PAPER_TYPE
    def paper_type(self):
        return self._content.paper_type

    @ATTRIBUTES.WEB_URL
    def web_url(self):
        return self._content.web_url

    @ATTRIBUTES.ORIGIN_DATE
    def origin_date(self):
        return self._content.origin_date

    @RELATIONS.DIRECTED.as_generator
    def directors(self):
        for director in self._content.under_direction_of:
            director: oparl.Basic
            if director.is_valid:
                yield node_factory(director), self

    @RELATIONS.INDUCED.as_generator
    def originators(self):
        for originator in self._content.originator_persons:
            originator: oparl.Basic
            if originator.is_valid:
                yield node_factory(originator), self

    @RELATIONS.CONCERNED.as_generator_with_class(ConsultationRelation)
    def consultations(self):
        for consultation in self._content.consultations:
            consultation: oparl.Consultation
            if consultation.is_valid:
                for organization in consultation.organizations:
                    organization: oparl.Organization
                    if organization.is_valid:
                        yield node_factory(organization), self, \
                            consultation

    @RELATIONS.CONCERNED
    def oparl_thread(self):
        return self, ThreadNode(self._content)


class OparlPersonNode(ifs.OparlPerson):
    _content: oparl.Person

    @ATTRIBUTES.OPARL_ID.as_primary
    def oparl_id(self):
        return self._content.oparl_id

    @ATTRIBUTES.MODIFIED
    def modified(self):
        return self._content.modified

    @ATTRIBUTES.NAME
    def name(self):
        return self._content.name

    @ATTRIBUTES.WEB_URL
    def web_url(self):
        return self._content.web_url

    def location(self) -> tuple:
        pass

    def status(self) -> str:
        pass

    def title(self) -> str:
        pass


class OparlOrganizationNode(ifs.OparlOrganization):
    _content: oparl.Organization

    @ATTRIBUTES.OPARL_ID.as_primary
    def oparl_id(self):
        return self._content.oparl_id

    @ATTRIBUTES.MODIFIED
    def modified(self):
        return self._content.modified

    @ATTRIBUTES.NAME
    def name(self):
        return self._content.name

    @ATTRIBUTES.START_DATE
    def start_date(self):
        return self._content.start_date

    @ATTRIBUTES.END_DATE
    def end_date(self):
        return self._content.end_date

    @RELATIONS.LOCATED
    def location(self) -> tuple:
        location = self._content.location
        if location.is_valid:
            return self, node_factory(location)

    @ATTRIBUTES.ORGANIZATION_TYPE
    def organization_type(self) -> str:
        return self._content.organization_type

    @ATTRIBUTES.CLASSIFICATION
    def classification(self) -> str:
        return self._content.classification

    @RELATIONS.IS_MEMBER.as_generator_with_class(MembershipRelation)
    def members(self) -> tuple:
        for membership in self._content.memberships:
            membership: oparl.Membership
            if membership.is_valid:
                member = membership.person
                member: oparl.Person
                if member.is_valid:
                    yield node_factory(member), self, membership

    @ATTRIBUTES.WEB_URL
    def web_url(self) -> str:
        return self._content.web_url

    @RELATIONS.IS_MEMBER.as_generator
    def parent_organization(self) -> tuple:
        parent_org = self._content.parent_organization
        parent_org: oparl.Organization
        if parent_org.is_valid:
            yield self, node_factory(parent_org)


class OparlLocationNode(ifs.OparlLocation):
    _content: oparl.Location

    @ATTRIBUTES.OPARL_ID.as_primary
    def oparl_id(self):
        return self._content.oparl_id

    @ATTRIBUTES.MODIFIED
    def modified(self):
        return self._content.modified

    @ATTRIBUTES.LOCALITY
    def locality(self):
        return self._content.locality

    @ATTRIBUTES.POSTAL_CODE
    def postal_code(self):
        return self._content.postal_code

    @ATTRIBUTES.DESCRIPTION
    def description(self):
        return self._content.description

    @ATTRIBUTES.STREET_ADDRESS
    def street_address(self):
        return self._content.street_address


factory_mapping = {oparl.Basic: Node,
                   oparl.Location: OparlLocationNode,
                   oparl.Organization: OparlOrganizationNode,
                   oparl.Paper: PaperNode,
                   oparl.Person: OparlPersonNode}


def node_factory(oparl_obj: oparl.Basic):
    oparl_cls = oparl_obj.__class__
    node_cls = factory_mapping.get(oparl_cls)
    return node_cls(oparl_obj)
