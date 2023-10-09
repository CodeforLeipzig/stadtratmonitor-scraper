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

    def purge(self) -> tuple[str, dict]:
        lines = '\n'.join((' '.join(line) for line in self.lines))
        parameter = self.parameters
        self.parameters, self.lines, self.current_line = {}, [], []
        return lines, parameter


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

    def set(self, anchor, *properties):
        p_str = Entity(self, anchor, None, properties).properties_str('=', anchor_dot=True)
        if p_str:
            self.newline('SET')
            self.current_line.append(p_str)
        return self

    def on_merge(self, anchor, *properties):
        p_str = Entity(self, anchor, None, properties).properties_str('=', anchor_dot=True)
        if p_str:
            self.newline('ON MERGE')
            self.current_line.append(p_str)
        return self

    def on_create(self, anchor, *properties):
        p_str = Entity(self, anchor, None, properties).properties_str('=', anchor_dot=True)
        if p_str:
            self.newline('ON CREATE')
            self.current_line.append(p_str)
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

    def relation_to(self, anchor, item, *properties):
        chunk = Entity(self, anchor, item, properties).to_relation()
        self.current_line.append(f'- {chunk} ->')
        return self

    def relation_from(self, anchor, item, *properties):
        chunk = Entity(self, anchor, item, properties).to_relation()
        self.current_line.append(f'<- {chunk} -')
        return self

    def relation(self, anchor, item, *properties):
        chunk = Entity(self, anchor, item, properties).to_relation()
        self.current_line.append(f'- {chunk} -')
        return self
