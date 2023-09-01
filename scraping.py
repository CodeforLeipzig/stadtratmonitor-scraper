from neo_connector import database_connection, Session
from nodes_from_oparl import node_factory as oparl_node_factory
from statements import create_relation
from nodes_from_oparl import UnknownOparlNode
from oparl import Pagination


def scrapping(db_con):
    for item in Pagination():
        paper_node = oparl_node_factory(item)
        with db_con.session() as session:
            session: Session
            #db_node: AbcOparlPaperInterface = session.execute_write(retrieve_single, node_paper)
            #if db_node.modified == node_paper.modified: continue
            for director in paper_node.directors():
                if isinstance(director.source, UnknownOparlNode) or isinstance(director.target, UnknownOparlNode):
                    continue
                r = session.execute_write(create_relation, director)
                pass
            for originator in paper_node.originators():
                if isinstance(originator.source, UnknownOparlNode) or isinstance(originator.target, UnknownOparlNode):
                    continue
                r = session.execute_write(create_relation, originator)
                pass


if __name__ == '__main__':
    with database_connection() as dbc:
        scrapping(dbc)


#print(connection.driver.execute_query('match (n) return count(n)'))
#connection.driver.close()
