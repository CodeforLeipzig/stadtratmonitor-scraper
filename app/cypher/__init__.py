from ._basic import tag_generator
from . import _chunks
from . import abstract
from ._index import Index


class Cypher(
    _chunks.EntityCommand,
    _chunks.PropertyCommands,
    _chunks.ReturnCommand,
    _chunks.NodeString,
    _chunks.RelationString,
    _chunks.PropertyString,
    _chunks.AnchorString
): ...


Cypher: abstract.NewlineCommand
