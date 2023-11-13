from ... import graph
from ._basic import Index

person_names = Index('person_names')
person_names.create(graph.mock.CustomNode.PERSON(),
                    graph.mock.Property.NAME())

subjects = Index('subjects')
subjects.create(graph.mock.CustomNode.THREAD(),
                graph.mock.Property.NAME())
