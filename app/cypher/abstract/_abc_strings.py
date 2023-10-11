from abc import abstractmethod
from ._abc_cypher import CypherABC


class AnchorString(CypherABC):
    @abstractmethod
    def anchors(self, *anchors): ...


class PropertyString(CypherABC):
    @abstractmethod
    def properties(self, anchor='', *properties): ...


class NodeString(CypherABC):
    @abstractmethod
    def node(self, anchor, item, *properties): ...


class RelationString(CypherABC):
    @abstractmethod
    def related_to(self, anchor, item, *properties): ...

    @abstractmethod
    def related_from(self, anchor, item, *properties): ...

    @abstractmethod
    def related_by(self, anchor, item, *properties): ...
