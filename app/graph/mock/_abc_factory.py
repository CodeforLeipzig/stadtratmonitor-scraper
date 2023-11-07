from abc import ABC, abstractmethod
from . import _abc_entity
from .. import _scheme


class AbstractFactory(ABC):
    _entity: type
    _space: object

    def __init__(self, func=None):
        self._func: callable = func

    @abstractmethod
    def _create(self, item):
        ...

    def __getattr__(self, item):
        try:
            item = getattr(self._space, item)
            return self._create(item)
        except Exception:
            return object.__getattribute__(self, item)


class PropertyFactory(AbstractFactory, ABC):
    def _create(self, item):
        def creator(value=None, is_primary=False):
            prop = item(lambda *_: value, is_primary).fget(None)
            if self._func: self._func(prop)
            return prop

        return creator


class DefinedNodeFactory(_scheme.NODES, AbstractFactory, ABC):
    _entity: type[_abc_entity.Node] = None

    def _create(self, item):
        def creator(relations=(), properties=()):
            node = self._entity(item, relations, properties)
            if self._func: self._func(node)
            return node

        return creator


class LabelFactory(_scheme.LABELS, AbstractFactory, ABC):
    _entity = type[_abc_entity.Node]

    def _create(self, item):
        if self._func:
            self._func(item)
            return self
        else:
            return self._entity((item,))


class RelationFactory(_scheme.RELATIONS, AbstractFactory, ABC):
    _entity: type[_abc_entity.Relation]

    def _create(self, item):
        def creator(source=None, target=None, properties=()):
            relation = item(lambda *_: (source, target, properties), cls=self._entity).fget(None)
            if self._func: self._func(relation)
            return relation

        return creator
