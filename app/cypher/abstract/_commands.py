from abc import abstractmethod
from ._cypher import CypherABC


class EntityCommand(CypherABC):
    @abstractmethod
    def match(self, anchor, item, *properties): ...

    @abstractmethod
    def merge(self, anchor, item, *properties): ...

    @abstractmethod
    def create(self, anchor, item, *properties): ...


class PropertyCommand(CypherABC):
    @abstractmethod
    def set(self, anchor, *properties): ...

    @abstractmethod
    def on_merge(self, anchor, *properties): ...

    @abstractmethod
    def on_create(self, anchor, *properties): ...


class ReturnCommand(CypherABC):
    @abstractmethod
    def return_anchors(self, *anchors): ...

    @abstractmethod
    def return_properties(self, anchor, *properties): ...
