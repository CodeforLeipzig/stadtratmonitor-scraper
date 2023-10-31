from app.database import connection
from app.database.statements import query_index, make_index
from app.graph import oparl_node_factory
from app.oparl import Oparl
from app.update_database import Updater


def scrapping(db_con, oparl_):
    updater = Updater()
    for item in oparl_.pagination():
        paper_node = oparl_node_factory(item)
        x = db_con.driver.execute_query(*make_index())
        y = db_con.driver.execute_query(*query_index('Thomas'))
        cypher = updater(paper_node)
        cypher.print()
        cypher.purge()


if __name__ == '__main__':
    with connection() as dbc:
        scrapping(dbc, Oparl)

# print(connection.driver.execute_query('match (n) return count(n)'))
# connection.driver.cose()
