from collections import deque
from app.database import connection, Session
from app.graph import Node, Relation, oparl_node_factory
from app.database.statements import create_relation
from app.oparl import Oparl


def update_nodes_and_relations(tx, node: Node, buffer=None, /):
    _buffer = buffer if buffer else deque()
    for relation in node.relations():
        relation: Relation
        if relation in _buffer:
            continue
        else:
            result = create_relation(tx, relation)
            print(result)
            _buffer.appendleft(relation)
            for item in (relation.source, relation.target):
                item: Node
                update_nodes_and_relations(tx, item, _buffer)


def scrapping(db_con, oparl_):
    for item in oparl_.pagination():
        paper_node = oparl_node_factory(item)

        with db_con.session() as session:
            session: Session
            # db_node: AbcOparlPaperInterface = session.execute_write(retrieve_single, node_paper)
            # if db_node.modified == node_paper.modified: continue

            session.execute_write(update_nodes_and_relations, paper_node, None)

            '''
            for director in paper_node.directors():
                r = session.execute_write(create_relation, director)
                pass
            for originator in paper_node.originators():
                r = session.execute_write(create_relation, originator)
                pass
            '''


if __name__ == '__main__':
    with connection() as dbc:
        oparl = Oparl()
        scrapping(dbc, oparl)

# print(connection.driver.execute_query('match (n) return count(n)'))
# connection.driver.close()
