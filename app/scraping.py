from app.database import connection, Session
from app.graph import Node, oparl_node_factory
from app.oparl import Oparl
from app.cypher import Cypher, tag_generator
from app.update_database import Updater


def scrapping(db_con, oparl_):
    updater = Updater()
    for item in oparl_.pagination():
        paper_node = oparl_node_factory(item)
        cypher = updater(paper_node)
        cypher.print()
        continue

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
    # with connection() as dbc:
    oparl = Oparl()
    scrapping(None, oparl)

# print(connection.driver.execute_query('match (n) return count(n)'))
# connection.driver.close()
