from neo4j.graph import Node

from nodes_scheme import \
    ATTRIBUTES, \
    BasicNodeInterface, \
    AbcOparlPaperInterface, \
    AbcOparlPersonInterface, \
    AbcOparlOrganizationInterface, \
    AbcOparlLocationInterface


class Paper(AbcOparlPaperInterface):
    _content: Node

    @ATTRIBUTES.OPARL_ID.as_primary
    def oparl_id(self):
        return self._content.get('oparl_id')

    @ATTRIBUTES.MODIFIED
    def modified(self):
        return self._content.get('modified')

    @ATTRIBUTES.REFERENCE.as_primary
    def reference(self):
        return self._content.get('reference')

    @ATTRIBUTES.PAPER_TYPE
    def paper_type(self):
        return self._content.get('paper_type')

    @ATTRIBUTES.WEB_URL
    def web_url(self):
        return self._content.get('web_url')

    @ATTRIBUTES.ORIGIN_DATE
    def origin_date(self):
        return self._content.get('origin_date')

    def directors(self):
        pass


factory_mapping = [Paper,
                   AbcOparlPersonInterface,
                   AbcOparlOrganizationInterface,
                   AbcOparlLocationInterface]


def node_factory(result):
    for cls in factory_mapping:
        if cls._labels == list(result.labels):
            obj = cls(result)
            return obj
