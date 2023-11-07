from abc import ABC, abstractmethod
from .. import _entity


class Property(_entity.Property): ...


class Entity(_entity.Entity, ABC):
    _attributes: list[_entity.Property]

    def attributes(self):
        yield from self._attributes

    @property
    @abstractmethod
    def add(self): ...


class Node(Entity, _entity.Node, ABC):
    def __init__(self, labels=(), relations=(), properties=()):
        self._labels = list(labels)
        self._attributes = list(properties)
        self._relations = list(relations)

    def relations(self):
        yield from self._relations


class Relation(Entity, _entity.Relation, ABC):
    def __init__(self, relation_type=None, source_node=None, target_node=None, properties=()):
        self._relation_type = [relation_type] if relation_type else ['']
        self._source = source_node  # if source_node else Node()
        self._target = target_node  # if target_node else Node()
        self._attributes = list(properties)
