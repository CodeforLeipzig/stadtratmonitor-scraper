from . import _abc_factory
from abc import ABC, abstractmethod


class AnyNodes(ABC):
    _defined: type[_abc_factory.DefinedNodeFactory]
    _custom: type[_abc_factory.LabelFactory]

    def __init__(self, add_node=None):
        self.defined = self._defined(add_node)
        self.custom = self._custom(add_node)

    @property
    @abstractmethod
    def _defined(self) -> type[_abc_factory.DefinedNodeFactory]: ...

    @property
    @abstractmethod
    def _custom(self) -> type[_abc_factory.LabelFactory]: ...


class NodeDefinable(ABC):
    def __init__(self, add_property=None, add_relation=None, add_label=None):
        self.property = self._property(add_property)
        self.relation = self._relation(add_relation)
        self.label = self._label(add_label)

    @property
    @abstractmethod
    def _property(self) -> type[_abc_factory.PropertyFactory]: ...

    @property
    @abstractmethod
    def _relation(self) -> type[_abc_factory.RelationFactory]: ...

    @property
    @abstractmethod
    def _label(self) -> type[_abc_factory.LabelFactory]: ...


class RelationDefinable(ABC):
    def __init__(self, set_target=None, set_source=None, add_property=None):
        self.target = self._target(set_target)
        self.source = self._source(set_source)
        self.property = self._property(add_property)

    @property
    @abstractmethod
    def _target(self) -> type[AnyNodes]: ...

    @property
    @abstractmethod
    def _source(self) -> type[AnyNodes]: ...

    @property
    @abstractmethod
    def _property(self) -> type[_abc_factory.PropertyFactory]: ...
