from _basic import Property, PropertyHook
from _entity import Relation, RelationHook


class PropertyFactory:
    __slots__ = ('_key',)

    def __init__(self, key: str):
        self._key = key

    def key(self):
        return self._key

    def __call__(self, func, is_primary=False):
        def get_property(instance):
            return Property(self.key, lambda: func(instance), is_primary)

        return PropertyHook(get_property)

    def as_primary(self, func):
        return self(func, is_primary=True)


class RelationFactory:
    __slots__ = ('_relation_type',)

    def __init__(self, relation_type: str):
        self._relation_type = relation_type

    def __call__(self, func, cls=Relation):
        def get_relation(*args):
            params = func(*args)
            return cls(self._relation_type, *params)

        return RelationHook(get_relation)

    def with_class(self, cls):
        assert issubclass(cls, Relation)
        return lambda x: self(x, cls=cls)

    def as_generator(self, func, cls=Relation):
        def relation_generator(*args):
            for items in func(*args):
                yield cls(self._relation_type, *items)

        return RelationHook(relation_generator)

    def as_generator_with_class(self, cls):
        assert issubclass(cls, Relation)
        return lambda x: self.as_generator(x, cls=cls)
