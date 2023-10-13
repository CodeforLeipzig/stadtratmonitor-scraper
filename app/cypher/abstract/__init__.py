from abc import ABC
from ._cypher import CypherABC
from ._commands import EntityCommand, PropertyCommand, ReturnCommand
from ._strings import AnchorString, PropertyString, NodeString, RelationString


class AnchorOrProperty(
    AnchorString,
    PropertyString,
    CypherABC, ABC
): ...


class NewlineCommand(
    PropertyCommand,
    EntityCommand,
    CypherABC, ABC
): ...


class NewlineOrReturn(
    ReturnCommand,
    NewlineCommand,
    CypherABC, ABC
): ...


class NewlineOrRelationOrReturn(
    NewlineOrReturn,
    RelationString,
    CypherABC, ABC
): ...
