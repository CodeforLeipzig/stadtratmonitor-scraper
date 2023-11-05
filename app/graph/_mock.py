from abc import ABC

from . import _entity, _scheme, _factory


class Property:
    def __init__(self, owner=None):
        self._owner: Entity = owner

    def __getattribute__(self, item):
        pf: _factory.PropertyFactory = getattr(_scheme.ATTRIBUTES, item)

        def creator(value=None, is_primary=False):
            prop = pf(lambda *_: value, is_primary).fget(None)
            if self._owner:
                self._owner.append_property(prop)
                return self
            else:
                return prop

        return creator


class DefinedNodes:
    def __getattribute__(self, item):
        labels = getattr(_scheme.NODES, item)
        return Node(labels)


class CustomNodes:
    def __init__(self, owner):
        self._owner: Node = owner

    def __getattribute__(self, item):
        label = getattr(_scheme.LABELS, item)
        if self._owner:
            self._owner.append_label(label)
            return self
        else:
            return Node([label])


class AnyNodes:
    def __init__(self, owner):
        self.custom = CustomNodes(owner)
        self.defined = DefinedNodes(owner)


class DefinedRelations:
    def __init__(self, owner):
        self._owner = owner

    def __getattribute__(self, item):
        rf: _factory.RelationFactory = getattr(_scheme.RELATIONS, item)

        def creator(source=None, target=None, properties=()):
            relation = rf(lambda *_: (source, target, properties), cls=Relation).fget(None)
            if self._owner:
                self._owner.append_relation(relation)
                return self
            else:
                return relation

        return creator


class Entity(_entity.Entity, ABC):
    _attributes: list[Property]

    def attributes(self):
        yield from self._attributes

    def add(self): ...

    def append_property(self, prop: _entity.Property):
        self._attributes.append(prop)


class NodeAddable:
    def __init__(self, owner):
        self.property = Property(owner)
        self.relation = DefinedRelations(owner)


class Node(Entity, _entity.Node):
    def __init__(self, labels=(), relations=(), properties=()):
        self._labels = list(labels)
        self._attributes = list(properties)
        self._relations = list(relations)

    def relations(self):
        yield from self._relations

    @property
    def add(self):
        return NodeAddable(self)

    def append_relation(self, relation):
        self._relations.append(relation)

    def append_label(self, label):
        self._labels.append(label)


class RelationSetable:
    def __init__(self, owner):
        self.target = AnyNodes(owner)
        self.source = AnyNodes(owner)


class Relation(Entity, _entity.Relation):
    def __init__(self, relation_type=None, source_node=None, target_node=None, properties=()):
        self._relation_type = [relation_type] if relation_type else ['']
        self._source = source_node if source_node else Node()
        self._target = target_node if target_node else Node()
        self._attributes = list(properties)

    def attributes(self):
        yield from self._attributes

    @property
    def add(self):
        return Property(self)

    @property
    def set(self):
        return RelationSetable()

    ## give append function to factory instead of instance
