from . import _mock
from .. import _scheme

# noinspection PyTypeChecker
Property: _scheme.ATTRIBUTES = _mock.PropertyFactory()
DefinedNode: _scheme.NODES = _mock.DefinedNodeFactory()
CustomNode: _scheme.LABELS = _mock.CustomNodeFactory()
Relation: _scheme.RELATIONS = _mock.RelationFactory()
