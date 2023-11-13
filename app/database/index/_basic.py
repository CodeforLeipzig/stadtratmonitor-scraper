from ... import cypher
from ..neo_connector import database_connection


def send(statement, parameter):
    with database_connection() as dbc:
        return dbc.driver.execute_query(statement, parameter)


class Index:
    def __init__(self, name):
        self.name = name

    def create(self, item, *properties):
        statement, parameter = cypher.Index().create_fulltext_index(
            self.name, item, *properties)
        return send(statement, parameter)

    def delete(self):
        statement, parameter = cypher.Index().drop_index(self.name)
        return send(statement, parameter)

    def call(self, string):
        statement, parameter = cypher.Index.call_index(self.name, string)
        return send(statement, parameter)
