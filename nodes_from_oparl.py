from oparl_objects import BasicOparl as OparlBasic
from oparl_objects import UnknownOparl as OparlUnknown
from oparl_objects import Paper as OparlPaper
from oparl_objects import Person as OparlPerson
from oparl_objects import Organization as OparlOrganization
from oparl_objects import Location as OparlLocation
from oparl_objects import oparl_factory as oparl_factory
import fakerequest as request
import json

from nodes_scheme import \
    RELATIONS, \
    ATTRIBUTES, \
    AbcNodeInterface, \
    AbcOparlPaperInterface, \
    AbcOparlPersonInterface, \
    AbcOparlOrganizationInterface, \
    AbcOparlLocationInterface


class UnknownOparlNode(AbcNodeInterface):
    _content: OparlUnknown
    _labels = []

    @ATTRIBUTES.OPARL_ID.as_primary
    def oparl_id(self):
        return self._content.oparl_id


def converted_get_request(o_obj: OparlUnknown):
    url = o_obj.oparl_id
    response = request.get(url)
    if response.state == 200:
        content = json.loads(response.content)
        return oparl_factory(content)


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
            if isinstance(director, OparlUnknown):
                director = converted_get_request(director)
            if director:
                yield node_factory(director), self

    @RELATIONS.SUBMITTED.as_generator
    def originators(self):
        for originator in self._content.originator_persons:
            if isinstance(originator, OparlUnknown):
                originator = converted_get_request(originator)
            if originator:
                yield node_factory(originator), self


    #_content.consultations


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


factory_mapping = {OparlPerson: OparlPersonNode,
                   OparlPaper: OparlPaperNode,
                   OparlOrganization: OparlOrganizationNode,
                   OparlLocation: OparlLocationNode,
                   OparlUnknown: UnknownOparlNode}


def node_factory(oparl_obj: OparlBasic):
    oparl_cls = oparl_obj.__class__
    assert issubclass(oparl_cls, OparlBasic)
    node_cls = factory_mapping.get(oparl_cls)
    return node_cls(oparl_obj)
