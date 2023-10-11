from ._basic import CypherBase
from ._parser import EntityParser
from . import abstract


class EntityCommand(CypherBase):
    # noinspection PyTypeChecker
    def __entity_command(self, cmd, anchor, item, properties) -> abstract.NewlineOrRelationOrReturn:
        self._newline(cmd)
        NodeString.node(self, anchor, item, properties)
        return self

    def match(self, anchor, item, *properties):
        return self.__entity_command('MATCH', anchor, item, properties)

    def merge(self, anchor, item, *properties):
        return self.__entity_command('MERGE', anchor, item, properties)

    def create(self, anchor, item, *properties):
        return self.__entity_command('CREATE', anchor, item, properties)


class PropertyCommands(CypherBase):
    def __property_command(self, cmd: str, anchor: str, properties) -> abstract.NewlineOrReturn:
        prop_str = EntityParser(self, anchor, None, properties).properties_str('=', anchor_dot=True)
        if prop_str:
            self._newline(cmd)
            self._stage(prop_str)
        # noinspection PyTypeChecker
        return self

    def set(self, anchor, *properties):
        return self.__property_command('SET', anchor, *properties)

    def on_merge(self, anchor, *properties):
        return self.__property_command('ON MERGE SET', anchor, *properties)

    def on_create(self, anchor, *properties):
        return self.__property_command('ON CREATE SET', anchor, *properties)


class ReturnCommand(CypherBase):
    @property
    def return_(self) -> abstract.AnchorOrProperty:
        self._newline('RETURN')
        # noinspection PyTypeChecker
        return self


class AnchorString(CypherBase):
    def anchors(self, *anchors) -> abstract.NewlineCommand:
        self._stage(', '.join(anchors))
        # noinspection PyTypeChecker
        return self


class PropertyString(CypherBase):
    def properties(self, anchor='', *properties) -> abstract.NewlineCommand:
        entity = EntityParser(self, anchor, None, properties).properties_str('=', anchor_dot=True)
        self._stage(entity)
        # noinspection PyTypeChecker
        return self


class NodeString(CypherBase):
    def node(self, anchor, item, *properties) -> abstract.NewlineOrRelationOrReturn:
        chunk = EntityParser(self, anchor, item, properties).to_node()
        self._stage(chunk)
        # noinspection PyTypeChecker
        return self


class RelationString(CypherBase):
    def __relation_str(self, s, anchor, item, properties, e) -> abstract.NodeString:
        chunk = EntityParser(self, anchor, item, properties).to_relation()
        self._stage(f'{s} {chunk} {e}')
        # noinspection PyTypeChecker
        return self

    def related_to(self, anchor, item, *properties):
        return self.__relation_str('-', anchor, item, properties, '->')

    def related_from(self, anchor, item, *properties):
        return self.__relation_str('<-', anchor, item, properties, '-')

    def related_by(self, anchor, item, *properties):
        return self.__relation_str('-', anchor, item, properties, '-')
