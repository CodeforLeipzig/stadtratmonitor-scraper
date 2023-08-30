import json
import fakerequest as request
from fakerequest import START_URL
from oparl_objects import oparl_factory
from neo_connector import database_connection, Session
from nodes_from_oparl import node_factory as oparl_node_factory
from statements import full_merge, retrieve_single
from nodes_scheme import AbcOparlPaperInterface
from nodes_from_oparl import UnknownOparlNode


def pages(start_url):
    max_pages = 1
    page_count = 0
    url = start_url
    while url and page_count < max_pages:
        response = request.get(url)
        page_count += 1
        if response.state == 200:
            content = json.loads(response.content)
            yield content.get('data')
            url = content.get('links')
            if url:
                url = url.get('next')


def converted_item_on(page):
    for item in page:
        yield oparl_node_factory(oparl_factory(item))


def converted_get_request(node: UnknownOparlNode):
    url = node.oparl_id.value()
    response = request.get(url)
    if response.state == 200:
        content = json.loads(response.content)
        return oparl_node_factory(oparl_factory(content))


def scrapping(db_con, start_url):
    for page in pages(start_url):
        for node_paper in converted_item_on(page):
            with db_con.session() as session:
                session: Session
                knowledge = dict()
                #db_node: AbcOparlPaperInterface = session.execute_write(retrieve_single, node_paper)
                #if db_node.modified == node_paper.modified: continue
                for director in node_paper.directors():
                    print(director)
                for originator in node_paper.originators():
                    print(originator)
                pass


if __name__ == '__main__':
    with database_connection() as dbc:
        scrapping(dbc, START_URL)


#print(connection.driver.execute_query('match (n) return count(n)'))
#connection.driver.close()
