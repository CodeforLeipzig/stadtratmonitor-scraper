from . import _entity, _scheme, _factory


class Property(_scheme.ATTRIBUTES):

    def __getattribute__(self, item):
        pf: _factory.PropertyFactory = getattr(_scheme.ATTRIBUTES, item)

        def creator(value=None, is_primary=False):
            return pf(lambda *_: value, is_primary).fget(None)

        return creator


class Labels:
    def __init__(self, owner):
        self.owner: Node = owner

    def __getattr__(self, item):
        label = getattr(_scheme.LABELS, item)


class Node(_entity.Node):
    def __init__(self, labels, relations, properties):
        self._attributes = properties
        self._relations = relations
        self._labels = labels

    def attributes(self):
        yield from self._attributes

    def relations(self):
        yield from self._relations
