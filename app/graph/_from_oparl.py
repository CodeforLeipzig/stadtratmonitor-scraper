from ._scheme import RELATIONS, ATTRIBUTES
from ._basic import BasicNodeInterface
from . import _interfaces as ifs
from .. import oparl


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

    @RELATIONS.CONCERNED.as_generator
    def consultations(self):
        for consultation in self._content.consultations:
            consultation: oparl.Basic
            if consultation.is_valid:
                yield node_factory(consultation), self

    @RELATIONS.CONCERNED
    def oparl_thread(self):
        return self, ThreadNode(self._content)


class LegislativeTermNode(ifs.LegislativeTerm):
    _content: oparl.Paper

    @ATTRIBUTES.NAME.as_primary
    def name(self):
        return self._content.legis_term

    @ATTRIBUTES.START_DATE
    def start_date(self): pass

    @ATTRIBUTES.END_DATE
    def end_date(self): pass

    @RELATIONS.IN_PERIOD
    def in_period(self):
        return ThreadNode(self._content), self


class ThreadNode(ifs.Thread):
    _content: oparl.Paper

    @ATTRIBUTES.NAME
    def subject(self):
        return self._content.subject

    @ATTRIBUTES.REFERENCE.as_primary
    def reference(self):
        return self._content.thread_number

    @RELATIONS.CONCERNED
    def paper(self):
        return node_factory(self._content), self

    @RELATIONS.IN_PERIOD
    def legis_term(self):
        return self, LegislativeTermNode(self._content)


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


class ConsultationNode(ifs.Consultation):
    _content: oparl.Consultation

    @ATTRIBUTES.OPARL_ID.as_primary
    def oparl_id(self):
        return self._content.oparl_id

    @ATTRIBUTES.MODIFIED
    def modified(self):
        return self._content.modified

    @RELATIONS.CONCERNED
    def paper(self):
        paper = self._content.paper
        if paper.is_valid:
            return self, node_factory(paper)

    @RELATIONS.PARTICIPATED.as_generator
    def organizations(self):
        for organization in self._content.organizations:
            organization: oparl.Basic
            if organization.is_valid:
                yield node_factory(organization), self

    @ATTRIBUTES.AUTHORITATIVE
    def authoritative(self):
        return self._content.authoritative

    @ATTRIBUTES.ROLE
    def role(self):
        return self._content.role


class MembershipRelation(ifs.Membership):
    _content: oparl.Membership

    @property
    def source(self):
        if isinstance(self._source, OparlPersonNode):
            return self._source
        else:
            return node_factory(self._content.person)

    @property
    def target(self):
        if isinstance(self._target, OparlOrganizationNode):
            return self._target
        else:
            return node_factory(self._content.organization)

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


factory_mapping = {oparl.Basic: BasicNodeInterface,
                   oparl.Consultation: ConsultationNode,
                   oparl.Location: OparlLocationNode,
                   oparl.Organization: OparlOrganizationNode,
                   oparl.Paper: PaperNode,
                   oparl.Person: OparlPersonNode}


def node_factory(oparl_obj: oparl.Basic):
    oparl_cls = oparl_obj.__class__
    node_cls = factory_mapping.get(oparl_cls)
    return node_cls(oparl_obj)
