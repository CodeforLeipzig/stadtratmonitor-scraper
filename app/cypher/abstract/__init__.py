from abc import ABC

from ._abc_cypher import CypherABC
from ._abc_commands import EntityCommand, PropertyCommand, ReturnCommand
from ._abc_strings import AnchorString, PropertyString, NodeString, RelationString


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
