def make_index():
    query = 'CREATE FULLTEXT INDEX name_index IF NOT EXISTS ' \
            'FOR (n: Oparl) ON EACH [n.name] ' \
            'OPTIONS { indexConfig: { ' \
            '`fulltext.analyzer`: "german", ' \
            '`fulltext.eventually_consistent`: true } }'
    return query, {}


def query_index(string):
    query = f'CALL db.index.fulltext.queryNodes("name_index", $string ) ' \
            f'YIELD node, score ' \
            f'RETURN labels(node), node.name, score'
    return query, {'string': string}


def drop_index(name):
    query = f'DROP INDEX $name'
    return query, {'name': name}
