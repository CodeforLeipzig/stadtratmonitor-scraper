from abc import ABC, abstractmethod
from . import _abc_entity
from .. import schema


class AbstractFactory(ABC):
    _entity: type
    _namespace: type
    _item: object
    _func: callable

    def __init__(self, func=None):
        self._func = func

    @abstractmethod
    def __call__(self, *args, **kwargs):
        ...

    def __getattribute__(self, item: str):
        if item.startswith('_'):
            return object.__getattribute__(self, item)
        else:
            self._item = getattr(self._namespace, item)
            return self.__call__


class PropertyFactory(schema.ATTRIBUTES, AbstractFactory, ABC):
    _entity: type[_abc_entity.Node]
    _namespace = schema.ATTRIBUTES


class DefinedNodeFactory(schema.NODES, AbstractFactory, ABC):
    _entity: type[_abc_entity.Node]
    _namespace = schema.NODES


class LabelFactory(schema.LABELS, AbstractFactory, ABC):
    _entity = type[_abc_entity.Node]
    _namespace = schema.LABELS


class RelationFactory(schema.RELATIONS, AbstractFactory, ABC):
    _entity: type[_abc_entity.Relation]
    _namespace = schema.RELATIONS
