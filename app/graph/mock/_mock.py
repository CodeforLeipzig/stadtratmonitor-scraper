from . import _abc_entity, _abc_factory, _abc_spaces


class Property(_abc_entity.Property): ...


class Node(_abc_entity.Node):
    def add(self):
        return NodeSpace(self._attributes.append,
                         self._relations.append,
                         self._labels.append)


class Relation(_abc_entity.Relation):
    @property
    def add(self):
        return RelationSpace(lambda x: setattr(self, '_target', x),
                             lambda x: setattr(self, '_source', x),
                             self._attributes.append)


class NodeSpace(_abc_spaces.NodeDefinable):
    @property
    def _property(self) -> type[_abc_factory.PropertyFactory]:
        return PropertyFactory

    @property
    def _relation(self) -> type[_abc_factory.RelationFactory]:
        return RelationFactory

    @property
    def _label(self) -> type[_abc_factory.LabelFactory]:
        return CustomNodeFactory


class AnyNodeSpace(_abc_spaces.AnyNodes):
    @property
    def _defined(self) -> type[_abc_factory.DefinedNodeFactory]:
        return DefinedNodeFactory

    @property
    def _custom(self) -> type[_abc_factory.LabelFactory]:
        return CustomNodeFactory


class RelationSpace(_abc_spaces.RelationDefinable):
    @property
    def _target(self) -> type[AnyNodeSpace]:
        return AnyNodeSpace

    @property
    def _source(self) -> type[AnyNodeSpace]:
        return AnyNodeSpace

    @property
    def _property(self) -> type[_abc_factory.PropertyFactory]:
        return PropertyFactory


class PropertyFactory(_abc_factory.PropertyFactory):
    _entity = Property
    _space = _abc_factory._scheme.ATTRIBUTES


class DefinedNodeFactory(_abc_factory.DefinedNodeFactory):
    _entity = Node
    _space = _abc_factory._scheme.NODES


class CustomNodeFactory(_abc_factory.LabelFactory):
    _entity = Node
    _space = _abc_factory._scheme.LABELS


class RelationFactory(_abc_factory.RelationFactory):
    _entity = Relation
    _space = _abc_factory._scheme.RELATIONS
