from ._basic import Relations, RelationFactory


class RELATIONS(Relations):
    CONCERNED = RelationFactory('CONCERNED')  # Consultation -> Paper -> Thread
    DIRECTED = RelationFactory('DIRECTED')  # Organization | Person -> Paper
    IN_PERIOD = RelationFactory('IN_PERIOD')  # Thread -> Legis_term
    IS_MEMBER = RelationFactory('IS_MEMBER')  # Person -> Organization
    LOCATED = RelationFactory('LOCATED')  # Organization -> Location
    PARTICIPATED = RelationFactory('PARTICIPATED')
    INDUCED = RelationFactory('INDUCED')  # Organization | Person -> Paper
