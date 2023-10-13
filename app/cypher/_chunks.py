from ._basic import CypherBase
from ._parser import EntityParser
from . import abstract


class EntityCommand(CypherBase, abstract.EntityCommand):
    # noinspection PyTypeChecker
    def __entity_command(self, cmd, anchor, item, properties):
        self._newline(cmd)
        NodeString.node(self, anchor, item, properties)
        self: abstract.NewlineOrRelationOrReturn
        return self

    def match(self, anchor, item, *properties) -> abstract.NewlineOrRelationOrReturn:
        return self.__entity_command('MATCH', anchor, item, properties)

    def merge(self, anchor, item, *properties) -> abstract.NewlineOrRelationOrReturn:
        return self.__entity_command('MERGE', anchor, item, properties)

    def create(self, anchor, item, *properties) -> abstract.NewlineOrRelationOrReturn:
        return self.__entity_command('CREATE', anchor, item, properties)


class PropertyCommands(CypherBase, abstract.PropertyCommand):
    def __property_command(self, cmd: str, anchor: str, properties):
        prop_str = EntityParser(self, anchor, None, properties).properties_str('=', anchor_dot=True)
        if prop_str:
            self._newline(cmd)
            self._stage(prop_str)
        self: abstract.NewlineOrReturn
        return self

    def set(self, anchor, *properties) -> abstract.NewlineOrReturn:
        return self.__property_command('SET', anchor, *properties)

    def on_merge(self, anchor, *properties) -> abstract.NewlineOrReturn:
        return self.__property_command('ON MERGE SET', anchor, *properties)

    def on_create(self, anchor, *properties) -> abstract.NewlineOrReturn:
        return self.__property_command('ON CREATE SET', anchor, *properties)


class ReturnCommand(CypherBase, abstract.ReturnCommand):
    @property
    def return_(self) -> abstract.AnchorOrProperty:
        self._newline('RETURN')
        self: abstract.AnchorOrProperty
        return self


class AnchorString(CypherBase, abstract.AnchorString):
    def anchors(self, *anchors) -> abstract.NewlineCommand:
        self._stage(', '.join(anchors))
        self: abstract.NewlineCommand
        return self


class PropertyString(CypherBase, abstract.PropertyString):
    def properties(self, anchor='', *properties) -> abstract.NewlineCommand:
        entity = EntityParser(self, anchor, None, properties).properties_str('=', anchor_dot=True)
        self._stage(entity)
        self: abstract.NewlineCommand
        return self


class NodeString(CypherBase, abstract.NodeString):
    def node(self, anchor, item, *properties) -> abstract.NewlineOrRelationOrReturn:
        chunk = EntityParser(self, anchor, item, properties).to_node()
        self._stage(chunk)
        self: abstract.NewlineOrRelationOrReturn
        return self


class RelationString(CypherBase, abstract.RelationString):
    def __relation_str(self, s, anchor, item, properties, e):
        chunk = EntityParser(self, anchor, item, properties).to_relation()
        self._stage(f'{s} {chunk} {e}')
        self: abstract.NodeString
        return self

    def related_to(self, anchor, item, *properties) -> abstract.NodeString:
        return self.__relation_str('-', anchor, item, properties, '->')

    def related_from(self, anchor, item, *properties) -> abstract.NodeString:
        return self.__relation_str('<-', anchor, item, properties, '-')

    def related_by(self, anchor, item, *properties) -> abstract.NodeString:
        return self.__relation_str('-', anchor, item, properties, '-')
