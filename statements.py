from nodes_from_neo4j import node_factory as neo4j_node_factory
from nodes_scheme import BasicNodeInterface, DbAttribute, DbRelation


def retrieve_single(tx, node):
    ref = 'n'
    match_, parameter = prepare_match_by_primary(node, ref=ref)
    return_, _ = prepare_return(ref)

    result = tx.run('\n'.join((match_, return_)), parameter).single().value()
    return neo4j_node_factory(result)


def full_merge(tx, node):
    ref = 'n'
    match_, p1 = prepare_merge_by_primary(node, ref=ref)
    on_create, p2 = prepare_create_set(node, ref=ref)
    return_, _ = prepare_return(ref)
    parameter = {**p1, **p2}
    result = tx.run('\n'.join((match_, on_create, return_)), parameter)
    result = result.single().value()
    return neo4j_node_factory(result)


def create_relation(tx, node: DbRelation):
    s_ref, source = 'b', node.source
    t_ref, target = 'a', node.target
    r_ref = 'r'
    merge_s, p1 = prepare_merge_by_primary(source, s_ref)
    on_create_s, p2 = prepare_create_set(source, s_ref)
    merge_t, p3 = prepare_merge_by_primary(target, t_ref)
    on_create_t, p4 = prepare_create_set(target, t_ref)
    merge_r, _ = f'MERGE ({s_ref}) - [{r_ref}:{node.relation_type}] -> ({t_ref})', {}
    return_, _ = prepare_return(s_ref, r_ref, t_ref)

    statement = '\n'.join([merge_s, on_create_s, merge_t, on_create_t, merge_r, return_])
    parameter = {**p1, **p2, **p3, **p4}

    result = tx.run(statement, parameter)
    return result.values() #neo4j_node_factory(result)


def delete_all(tx, *_):
    return tx.run('MATCH (n) DETACH DELETE n').to_eager_result()


def prepare_match_by_primary(node_interface: BasicNodeInterface, ref='n') -> tuple[str, dict]:
    prim_keys = list()
    parameter = dict()

    for attribute in node_interface.primary_keys():
        for key, value in attribute:
            p_key = f'{ref}X{key}'
            prim_keys.append(f'{key}:${p_key}')
            parameter.update({p_key: value})

    labels = ':' + ':'.join(node_interface.labels) if node_interface.labels else ''
    prim_keys = '{' + ','.join(prim_keys) + '}'

    statement = f'MATCH ({ref}{labels} {prim_keys})'

    return statement, parameter


def prepare_merge_by_primary(node_interface: BasicNodeInterface, ref='n') -> tuple[str, dict]:
    parameter = dict()
    keys = list()

    for attribute in node_interface.primary_keys():
        for key, value in attribute:
            p_key = f'{ref}X{key}'
            keys.append(f'{key}:${p_key}')
            parameter.update({p_key: value})

    labels = ':'.join(node_interface.labels)
    keys = '{' + ','.join(keys) + '}'

    statement = f'MERGE ({ref}:{labels} {keys})'
    return statement, parameter


def prepare_create_set(node_interface: BasicNodeInterface, ref='n'):
    parameter = dict()
    keys = list()

    for attribute in node_interface.non_primary_keys():
        for key, value in attribute:
            p_key = f'{ref}X{key}'
            keys.append(f'{ref}.{key}=${p_key}')
            parameter.update({p_key: value})

    statement = f'ON CREATE SET {",".join(keys)}'
    return statement, parameter


def prepare_return(*args) -> (str, dict):
    """arg[n] = ref | (ref, attribute, ...) | (ref, ), (ref, attribute), ..."""
    pieces = []
    for arg in args:
        if isinstance(arg, str):
            pieces.append(arg)
        if isinstance(arg, tuple):
            ref = arg[0]
            for a in arg[1:]:
                a: DbAttribute
                pieces.append(f'{ref}.{a.key()}')

    return f'RETURN {",".join(pieces)}', {}
