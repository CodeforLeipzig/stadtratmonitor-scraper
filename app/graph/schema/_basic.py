from .._factory import PropertyFactory, RelationFactory
from abc import ABC, abstractmethod


def extract(cls, target: type):
    for item in cls.__dict__.values():
        if isinstance(item, target):
            yield item


class Schema(ABC):
    @classmethod
    @abstractmethod
    def items(cls): ...


class Label(str): ...


class Node(tuple): ...


class Labels(Schema):
    @classmethod
    def items(cls):
        return extract(cls, Label)


class Nodes(Schema):
    @classmethod
    def items(cls):
        return extract(cls, Node)


class Attributes(Schema):
    @classmethod
    def items(cls):
        return extract(cls, PropertyFactory)


class Relations(Schema):
    @classmethod
    def items(cls):
        return extract(cls, RelationFactory)
