from ._factory import PropertyFactory, RelationFactory


class LABELS:
    CONSULTATION = 'Consultation'
    LEGIS_TERM = 'LegisTerm'
    LOCATION = 'Location'
    NAMED_ENTITY = 'NamedEntity'
    OPARL = 'Oparl'
    ORGANIZATION = 'Organization'
    PAPER = 'Paper'
    PERSON = 'Person'
    THREAD = 'Thread'


L = LABELS


class NODES:
    LEGISLATIVE_TERM = [L.OPARL, L.LEGIS_TERM]
    THREAD = [L.OPARL, L.THREAD]
    PAPER = [L.OPARL, L.PAPER]
    OPARL_PERSON = [L.OPARL, L.NAMED_ENTITY, L.PERSON]
    OPARL_ORGANIZATION = [L.OPARL, L.NAMED_ENTITY, L.ORGANIZATION]
    OPARL_LOCATION = [L.OPARL, L.NAMED_ENTITY, L.LOCATION]
    CONSULTATION = [L.OPARL, L.CONSULTATION]


class RELATIONS:
    CONCERNED = RelationFactory('CONCERNED')  # Consultation -> Paper -> Thread
    DIRECTED = RelationFactory('DIRECTED')  # Organization | Person -> Paper
    IN_PERIOD = RelationFactory('IN_PERIOD')  # Thread -> Legis_term
    IS_MEMBER = RelationFactory('IS_MEMBER')  # Person -> Organization
    LOCATED = RelationFactory('LOCATED')  # Organization -> Location
    PARTICIPATED = RelationFactory('PARTICIPATED')
    INDUCED = RelationFactory('INDUCED')  # Organization | Person -> Paper


class ATTRIBUTES:
    AUTHORITATIVE = PropertyFactory('authoritative')
    CLASSIFICATION = PropertyFactory('classification')
    DESCRIPTION = PropertyFactory('description')
    END_DATE = PropertyFactory('end_date')
    LOCALITY = PropertyFactory('locality')
    MODIFIED = PropertyFactory('modified')
    NAME = PropertyFactory('name')
    ORGANIZATION_TYPE = PropertyFactory('organization_type')
    OPARL_ID = PropertyFactory('oparl_id')
    ORIGIN_DATE = PropertyFactory('origin_date')
    PAPER_TYPE = PropertyFactory('paper_type')
    POSTAL_CODE = PropertyFactory('postal_code')
    REFERENCE = PropertyFactory('reference')
    ROLE = PropertyFactory('role')
    START_DATE = PropertyFactory('start_date')
    STREET_ADDRESS = PropertyFactory('street_address')
    VOTING_RIGHT = PropertyFactory('voting_right')
    WEB_URL = PropertyFactory('web_url')
