from configparser import ConfigParser
from neo4j import GraphDatabase, Session
from contextlib import contextmanager


def neo4j_config():
    config = ConfigParser()
    config.read('./config')
    section = config['Neo4j']
    return dict(uri=section['NEO4J_URI'],
                user=section['NEO4J_USERNAME'],
                password=section['NEO4J_PASSWORD'])


class Database:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.driver.verify_connectivity()
        self.session = self.driver.session


@contextmanager
def database_connection():
    database = Database(**neo4j_config())
    exception: (Exception, None) = None
    try:
        yield database
    except Warning as w:
        print(w)
    except Exception as e:
        exception = e
    finally:
        database.driver.close()
        if exception:
            raise exception


if __name__ == '__main__':
    database = Database(**neo4j_config())
    print(database.driver.execute_query('match (n) return count(n)'))
    print(database.driver.execute_query('match (n) detach delete n'))
    print(database.driver.execute_query('match (n) return count(n)'))
    database.driver.close()
    exit()
