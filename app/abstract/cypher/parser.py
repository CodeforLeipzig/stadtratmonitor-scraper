import abc
import typing

from .basic import AbcCypher


class AbcParser(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def anchors(cypher: AbcCypher, *anchors) -> AbcCypher:
        """produces anchor string like ´a, b, c´"""

    @staticmethod
    @abc.abstractmethod
    def labels(cypher: AbcCypher, item, separator: typing.Optional[str]) -> AbcCypher:
        """produces label string like ´label_1:label_2´"""

    @staticmethod
    @abc.abstractmethod
    def properties(cypher: AbcCypher,
                   anchor: typing.Optional[str],
                   *properties,
                   separator: typing.Optional[str]) -> AbcCypher:
        """produces properties string like
         if anchor is given: ´a.key_1, a.key_2´
         if separator as ´=´ is given: ´key_1=$value_1, key_2=$value_2´"""

    @staticmethod
    @abc.abstractmethod
    def node(cypher: AbcCypher, anchor, item, *properties) -> AbcCypher:
        """produces node string like ´(a:labels {properties})´"""

    @staticmethod
    @abc.abstractmethod
    def relation(cypher: AbcCypher, anchor, item, *properties) -> AbcCypher:
        """produces relations string like ´[a:labels {properties}]´"""
