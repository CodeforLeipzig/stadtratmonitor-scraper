from .. import graph
from ._basic import CypherBase, extract


class EntityParser:
    _cypher: CypherBase
    _anchor: str
    _item: graph.Entity
    _properties: tuple[graph.Property]

    def __init__(self, cypher, anchor, item, properties):
        self._cypher = cypher
        self._anchor = anchor
        self._item = item
        self._properties = properties

    def anchor_str(self):
        anchor = self._anchor
        return anchor if anchor else ''

    def label_str(self, sep=':'):
        labels = self._item.labels if self._item else []
        return ':' + sep.join(labels) if labels else ''

    # noinspection PyProtectedMember
    def properties_str(self, kv_seperator: str, anchor_dot: bool):
        strings, params = [], self._cypher._parameters
        tk_sep = self._cypher._tk_seperator
        anchor_str = self.anchor_str()
        anchor_dot = anchor_dot and anchor_str

        for prop in extract(graph.Property, *self._properties):
            key, value = prop.key(), prop.value()
            tag = next(self._cypher._tag_generator)

            tagged_key = f'{tag}{tk_sep}{key}'  # a_name

            if anchor_dot:
                key = f'{anchor_str}.{key}'  # a.name

            if kv_seperator:
                prop_str = f'{key}{kv_seperator}${tagged_key}'  # a.name=a_name
                params.update({tagged_key: value})  # {a_name: 'something'}
            else:
                prop_str = key
            strings.append(prop_str)

        return ', '.join(strings)

    def curly_properties(self):
        params = self.properties_str(kv_seperator=':', anchor_dot=False)
        return ' {' + params + '}' if params else ''

    def squared_properties(self):
        params = self.properties_str(kv_seperator='', anchor_dot=True)
        return '[' + params + ']' if params else ''

    def to_node(self, label_sep=':'):
        anc, lab, cur = self.anchor_str(), self.label_str(label_sep), self.curly_properties()
        return f'({anc}{lab} {cur})'

    def to_relation(self):
        anc, lab, cur = self.anchor_str(), self.label_str(), self.curly_properties()
        return f'[{anc}{lab}{cur}]'
