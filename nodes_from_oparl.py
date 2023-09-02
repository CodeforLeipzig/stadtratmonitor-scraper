from oparl import \
    Basic as OparlBasic, \
    Paper as OparlPaper, \
    Person as OparlPerson, \
    Organization as OparlOrganization, \
    Location as OparlLocation, \
    Consultation as OparlConsultation, \
    Membership as OparlMembership

from nodes_scheme import \
    RELATIONS, \
    ATTRIBUTES, \
    BasicNodeInterface, \
    AbcOparlPaperInterface, \
    AbcOparlPersonInterface, \
    AbcOparlOrganizationInterface, \
    AbcOparlLocationInterface, \
    AbcOparlConsultationInterface, \
    AbcOparlMembershipInterface


class UnknownOparlNode(BasicNodeInterface):
    _content: OparlBasic
    _labels = []

    @ATTRIBUTES.OPARL_ID.as_primary
    def oparl_id(self):
        return self._content.oparl_id


class OparlPaperNode(AbcOparlPaperInterface):
    _content: OparlPaper

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
            director: OparlBasic
            if director.is_valid:
                yield node_factory(director), self

    @RELATIONS.INDUCED.as_generator
    def originators(self):
        for originator in self._content.originator_persons:
            originator: OparlBasic
            if originator.is_valid:
                yield node_factory(originator), self

    @RELATIONS.CONCERNED.as_generator
    def consultations(self):
        for consultation in self._content.consultations:
            consultation: OparlBasic
            if consultation.is_valid:
                yield node_factory(consultation), self


class OparlPersonNode(AbcOparlPersonInterface):
    _content: OparlPerson

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


class OparlOrganizationNode(AbcOparlOrganizationInterface):
    _content: OparlOrganization

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


class OparlLocationNode(AbcOparlLocationInterface):
    _content: OparlLocation

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


class OparlConsultationNode(AbcOparlConsultationInterface):
    _content: OparlConsultation

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
            return node_factory(paper)

    @RELATIONS.PARTICIPATED.as_generator
    def organizations(self):
        for organization in self._content.organizations:
            organization: OparlBasic
            if organization.is_valid:
                yield node_factory(organization), self

    @ATTRIBUTES.AUTHORITATIVE
    def authoritative(self):
        return self._content.authoritative

    @ATTRIBUTES.ROLE
    def role(self):
        return self._content.role


class OparlMembershipRelation(AbcOparlMembershipInterface):
    _content: OparlMembership

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


factory_mapping = {OparlBasic: UnknownOparlNode,
                   OparlConsultation: OparlConsultationNode,
                   OparlLocation: OparlLocationNode,
                   OparlOrganization: OparlOrganizationNode,
                   OparlPaper: OparlPaperNode,
                   OparlPerson: OparlPersonNode}


def node_factory(oparl_obj: OparlBasic):
    oparl_cls = oparl_obj.__class__
    assert issubclass(oparl_cls, OparlBasic)
    node_cls = factory_mapping.get(oparl_cls)
    return node_cls(oparl_obj)
