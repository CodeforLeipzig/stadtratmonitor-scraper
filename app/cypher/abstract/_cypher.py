from abc import ABC


class CypherABC(ABC):
    _parameters: dict
    _lines: list
    _current_line: list
    _anchors: set
    _tag_generator: callable
    _tk_seperator = '_'
