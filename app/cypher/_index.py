from .. import graph
from ._parser import EntityParser, CypherBase


class Index(CypherBase):
    def create_fulltext_index(self, name, item, *properties,
                              anchor='x', eventually_consistent=True, analyzer='german'):
        parser = EntityParser(self, anchor, item, properties)
        match_phrase = parser.to_node(label_sep='|') if isinstance(item, graph.Node) else parser.to_relation()
        self.add_lines(f'CREATE FULLTEXT INDEX {name} IF NOT EXISTS',
                       f'FOR {match_phrase}',
                       f'ON EACH [{parser.properties_str(kv_seperator="", anchor_dot=True)}]',
                       *self.__make_options(eventually_consistent, analyzer))
        return self.purge()

    @staticmethod
    def call_index(name, string):
        query = f'CALL db.index.fulltext.queryNodes("{name}", $string ) ' \
                f'YIELD node, score ' \
                f'RETURN node, score'
        return query, {'string': string}

    @staticmethod
    def drop_index(name):
        query = f'DROP INDEX $name'
        return query, {'name': name}

    @staticmethod
    def __make_options(eventually_consistent, analyzer):
        s, e = '{', '}'
        eventually_consistent = 'true' if eventually_consistent else 'false'
        return (f'OPTIONS {s} indexConfig: {s}',
                f'`fulltext.analyzer`: "{analyzer}",',
                f'`fulltext.eventually_consistent`: {eventually_consistent} {e} {e}')
