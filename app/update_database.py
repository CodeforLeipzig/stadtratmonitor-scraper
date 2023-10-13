from typing import NamedTuple, Generator
from collections import deque
from app import graph
from app.cypher import Cypher, tag_generator as TagGenerator


class MemoryItem(NamedTuple):
    anchor: str
    item: graph.Entity


class Memory:
    _memory: deque[MemoryItem]

    def __init__(self):
        self._memory = deque()

    def append(self, anchor, entity):
        self._memory.appendleft(MemoryItem(anchor, entity))

    def items(self) -> Generator:
        return (item.item for item in self._memory)

    def anchors(self) -> Generator:
        return (item.anchor for item in self._memory)

    def find_anchor(self, item) -> str:
        for memory_item in self._memory:
            if memory_item.item == item:
                return memory_item.anchor

    def find_item(self, anchor) -> graph.Entity:
        for memory_item in self._memory:
            if memory_item.anchor == anchor:
                return memory_item.item


class Updater:
    def __init__(self):
        self.cypher = Cypher()
        self.memory = Memory()
        self.tag_generator = TagGenerator()

    def __call__(self, node: graph.Node):
        self.update_node(node)
        for relation in node.relations():
            self.update_relation(relation)
        self.cypher.return_.anchors(*self.memory.anchors())
        return self.cypher

    def update_node(self, node):
        tag = self.memory.find_anchor(node)
        if tag:
            return tag
        else:
            tag = next(self.tag_generator)

        self.cypher \
            .merge(tag, node, node.primary_keys()) \
            .set(tag, node.non_primary_keys())

        self.memory.append(tag, node)
        return tag

    def update_relation(self, relation):
        r_tag = self.memory.find_anchor(relation)
        if r_tag:
            return r_tag
        else:
            r_tag = next(self.tag_generator)

        s_tag = self.update_node(relation.source)
        t_tag = self.update_node(relation.target)

        self.cypher.merge(
            s_tag, None). \
            related_to(r_tag, relation, relation.primary_keys()). \
            node(t_tag, None). \
            set(r_tag, relation.non_primary_keys())

        self.memory.append(r_tag, relation)
        return r_tag
