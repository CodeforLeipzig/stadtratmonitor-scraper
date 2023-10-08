from .parser import Entity, tag_generator


class CypherAbc:
    parameters: dict
    lines: list
    current_line: list
    tag_generator: callable
    tk_seperator = '_'

    def newline(self, chunk):
        self.current_line = [chunk]
        self.lines.append(self.current_line)


class Cypher(CypherAbc):
    def __init__(self):
        self.current_line = []
        self.lines = []
        self.parameters = {}
        self.tag_generator = tag_generator()

    @property
    def match(self):
        self.newline('MATCH')
        return self

    @property
    def merge(self):
        self.newline('MERGE')
        return self

    @property
    def create(self):
        self.newline('CREATE')
        return self

    @property
    def set(self):
        self.newline('SET')
        return self

    @property
    def on_merge(self):
        self.newline('ON MERGE')
        return self

    @property
    def on_create(self):
        self.newline('ON CREATE')
        return self

    @property
    def return_(self):
        self.newline('RETURN')
        return self

    def anchors(self, *anchors):
        self.current_line.extend(anchors)
        return self

    def properties(self, anchor='', *properties):
        entity = Entity(self, anchor, None, properties).properties_str('=', anchor_dot=True)
        self.current_line.append(entity)
        return self

    def node(self, anchor, item, *properties):
        chunk = Entity(self, anchor, item, properties).to_node()
        self.current_line.append(chunk)
        return self

    def relation(self, anchor, item, *properties):
        chunk = Entity(self, anchor, item, properties).to_relation()
        self.current_line.append(chunk)
        return self
