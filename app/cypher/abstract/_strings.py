from abc import abstractmethod, ABC
from ._cypher import CypherABC


class AnchorString(CypherABC, ABC):
    @abstractmethod
    def anchors(self, *anchors): ...


class PropertyString(CypherABC, ABC):
    @abstractmethod
    def properties(self, anchor='', *properties): ...


class NodeString(CypherABC, ABC):
    @abstractmethod
    def node(self, anchor, item, *properties): ...


class RelationString(CypherABC, ABC):
    @abstractmethod
    def related_to(self, anchor, item, *properties): ...

    @abstractmethod
    def related_from(self, anchor, item, *properties): ...

    @abstractmethod
    def related_by(self, anchor, item, *properties): ...
