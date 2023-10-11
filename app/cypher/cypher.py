from .parser import Entity, tag_generator


class CypherBase:
    _parameters: dict
    _lines: list
    _current_line: list
    _tag_generator: callable
    _tk_seperator = '_'

    def __init__(self):
        self._current_line = []
        self._lines = []
        self._parameters = {}
        self._tag_generator = tag_generator()

    def _newline(self, chunk):
        self._current_line = [chunk]
        self._lines.append(self._current_line)

    def _stage(self, chunk):
        self._current_line.append(chunk)

    def purge(self) -> tuple[str, dict]:
        lines = '\n'.join((' '.join(line) for line in self._lines))
        parameter = self._parameters
        self._parameters, self._lines, self._current_line = {}, [], []
        return lines, parameter


class EntityCommands(CypherBase):
    def __entity_command(self, cmd, anchor, item, properties):
        self._newline(cmd)
        self: NodeString
        NodeString.node(self, anchor, item, properties)
        self: NewlineOrRelationOrReturn
        return self

    def match(self, anchor, item, *properties):
        return self.__entity_command('MATCH', anchor, item, properties)

    def merge(self, anchor, item, *properties):
        return self.__entity_command('MERGE', anchor, item, properties)

    def create(self, anchor, item, *properties):
        return self.__entity_command('CREATE', anchor, item, properties)


class PropertyCommands(CypherBase):
    def __property_command(self, cmd: str, anchor: str, properties):
        prop_str = Entity(self, anchor, None, properties).properties_str('=', anchor_dot=True)
        if prop_str:
            self._newline(cmd)
            self._stage(prop_str)
        self: NewlineOrReturn
        return self

    def set(self, anchor, *properties):
        return self.__property_command('SET', anchor, *properties)

    def on_merge(self, anchor, *properties):
        return self.__property_command('ON MERGE SET', anchor, *properties)

    def on_create(self, anchor, *properties):
        return self.__property_command('ON CREATE SET', anchor, *properties)


class ReturnCommand(CypherBase):
    @property
    def return_(self):
        self._newline('RETURN')
        self: AnchorOrProperty
        return self


class AnchorString(CypherBase):
    def anchors(self, *anchors):
        self._stage(', '.join(anchors))
        self: NewlineCommands
        return self


class PropertyString(CypherBase):
    def properties(self, anchor='', *properties):
        entity = Entity(self, anchor, None, properties).properties_str('=', anchor_dot=True)
        self._stage(entity)
        self: NewlineCommands
        return self


class NodeString(CypherBase):
    def node(self, anchor, item, *properties):
        chunk = Entity(self, anchor, item, properties).to_node()
        self._stage(chunk)
        self: NewlineOrRelationOrReturn
        return self


class RelationString(CypherBase):
    def __relation_str(self, s, anchor, item, properties, e):
        chunk = Entity(self, anchor, item, properties).to_relation()
        self._stage(f'{s} {chunk} {e}')
        self: NodeString
        return self

    def related_to(self, anchor, item, *properties):
        return self.__relation_str('-', anchor, item, properties, '->')

    def related_from(self, anchor, item, *properties):
        return self.__relation_str('<-', anchor, item, properties, '-')

    def related_by(self, anchor, item, *properties):
        return self.__relation_str('-', anchor, item, properties, '-')


class AnchorOrProperty(
    AnchorString,
    PropertyString
):
    pass


class NewlineCommands(
    PropertyCommands,
    EntityCommands
):
    pass


class NewlineOrReturn(
    ReturnCommand,
    NewlineCommands
):
    pass


class NewlineOrRelationOrReturn(
    NewlineOrReturn,
    RelationString
):
    pass


class Cypher(
    NewlineOrRelationOrReturn,
    AnchorOrProperty,
    NodeString
):
    pass


Cypher: NewlineCommands
