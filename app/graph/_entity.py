from ._basic import Item, Property, PropertyHook
from typing import Any, Generator
from abc import ABC


class Entity(Item, ABC):
    __slots__ = ('_content', '_labels')
    _content: Any
    _labels: list

    @property
    def labels(self):
        for label in self._labels:
            yield label

    def attributes(self):
        for key, attr in self.__class__.__dict__.items():
            if isinstance(attr, PropertyHook):
                yield getattr(self, key)

    def primary_keys(self):
        for attribute in self.attributes():
            attribute: Property
            if attribute.is_primary():
                yield attribute

    def non_primary_keys(self):
        for attribute in self.attributes():
            attribute: Property
            if not attribute.is_primary():
                yield attribute


class Node(Entity):
    __slots__ = ()

    def __init__(self, content, labels):
        self._content = content
        self._labels = labels

    def __eq__(self, other):
        if self is other or \
                isinstance(other, Node) and \
                sorted(self.labels) == sorted(other.labels) and \
                sorted(self.attributes(), key=lambda x: x.key()) == \
                sorted(other.attributes(), key=lambda x: x.key()):
            return True
        else:
            return False

    def relations(self):
        for key, attr in self.__class__.__dict__.items():
            if isinstance(attr, RelationHook):
                relation = getattr(self, key)
                if isinstance(relation, Generator):
                    for rel in relation:
                        yield rel
                else:
                    yield relation


class Relation(Entity):
    __slots__ = ('_source', '_target', '_content')
    _labels: list
    _source: Node
    _target: Node
    _content: (Node, None)

    def __init__(self, relation_type=None, source=None, target=None, content=None, /):
        self._labels = [relation_type] if relation_type else ['']
        self._source = source
        self._target = target
        self._content = content

    def __eq__(self, other):
        if self is other or \
                isinstance(other, Relation) and \
                sorted(self.labels) == sorted(other.labels) and \
                self.source == other.source and \
                self.target == other.target and \
                self._content == other._content:
            return True
        else:
            return False

    @property
    def source(self):
        return self._source

    @property
    def target(self):
        return self._target

    @property
    def relation_type(self):
        return self._labels


class RelationHook(property):
    pass
