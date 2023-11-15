from . import _mock
from .. import schema

# noinspection PyTypeChecker
Property: schema.ATTRIBUTES = _mock.PropertyFactory()
DefinedNode: schema.NODES = _mock.DefinedNodeFactory()
CustomNode: schema.LABELS = _mock.CustomNodeFactory()
Relation: schema.RELATIONS = _mock.RelationFactory()
