from app.database import connection
from app.cypher import Cypher
from app.graph import mock, _scheme, oparl_node_factory
from app.oparl import Oparl

o_node = oparl_node_factory(Oparl.pagination().__next__())

cypher = Cypher()
cypher.match('n', o_node, o_node.primary_keys()).return_anchors()
cypher.add_lines('LIMIT 1')

with connection() as con:
    n = con.driver.execute_query(*cypher.purge())

# response: tuple[list[record], _, _ ] | record: keys = anchors, values = Nodes
n = n[0][0]['n']


def find_and_create_attributes(items):
    for key, value in items:
        for property_factory in _scheme.ATTRIBUTES.__dict__.values():
            if isinstance(property_factory, _scheme.PropertyFactory) and key == property_factory.key():
                mock.Property._item = property_factory
                yield mock.Property(value)


def create_node(labels, items):
    return mock._mock.Node(labels, (), find_and_create_attributes(items))


n_node = create_node(n.labels, n.items())
print(o_node == n_node)

o_relation = next(o_node.relations())
cypher.match('', o_node) \
    .related_by('r', o_relation, o_relation.attributes()) \
    .node('', None) \
    .return_anchors()

with connection() as con:
    r = con.driver.execute_query(*cypher.purge())

r = r[0][0]['r']


def create_relation(label, start_node, end_node, items):
    for relation_factory in _scheme.RELATIONS.__dict__.values():
        if isinstance(relation_factory, _scheme.RelationFactory) and label == relation_factory.key():
            mock.Relation._item = relation_factory
            start_node = create_node(start_node.labels, start_node.items())
            end_node = create_node(end_node.labels, end_node.items())
            return mock.Relation(start_node, end_node, find_and_create_attributes(items))


n_relation = create_relation(r.type, r.start_node, r.end_node, r.items())
# AttributeError: 'Relation' object has no attribute '_labels'
exit()
