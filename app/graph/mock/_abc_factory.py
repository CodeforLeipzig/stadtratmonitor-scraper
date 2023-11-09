from abc import ABC, abstractmethod
from . import _abc_entity
from .. import _scheme


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


class PropertyFactory(_scheme.ATTRIBUTES, AbstractFactory, ABC):
    _entity: type[_abc_entity.Node]
    _namespace = _scheme.ATTRIBUTES


class DefinedNodeFactory(_scheme.NODES, AbstractFactory, ABC):
    _entity: type[_abc_entity.Node]
    _namespace = _scheme.NODES


class LabelFactory(_scheme.LABELS, AbstractFactory, ABC):
    _entity = type[_abc_entity.Node]
    _namespace = _scheme.LABELS


class RelationFactory(_scheme.RELATIONS, AbstractFactory, ABC):
    _entity: type[_abc_entity.Relation]
    _namespace = _scheme.RELATIONS
