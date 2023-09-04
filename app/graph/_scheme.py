from ._basic import DbAttributeFactory, DbRelationFactory


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
    CONCERNED = DbRelationFactory('CONCERNED')  # Consultation -> Paper -> Thread
    DIRECTED = DbRelationFactory('DIRECTED')  # Organization | Person -> Paper
    IN_PERIOD = DbRelationFactory('IN_PERIOD')  # Thread -> Legis_term
    IS_MEMBER = DbRelationFactory('IS_MEMBER')  # Person -> Organization
    LOCATED = DbRelationFactory('LOCATED')  # Organization -> Location
    PARTICIPATED = DbRelationFactory('PARTICIPATED')
    INDUCED = DbRelationFactory('INDUCED')  # Organization | Person -> Paper


class ATTRIBUTES:
    AUTHORITATIVE = DbAttributeFactory('authoritative')
    DESCRIPTION = DbAttributeFactory('description')
    END_DATE = DbAttributeFactory('end_date')
    LOCALITY = DbAttributeFactory('locality')
    MODIFIED = DbAttributeFactory('modified')
    NAME = DbAttributeFactory('name')
    OPARL_ID = DbAttributeFactory('oparl_id')
    ORIGIN_DATE = DbAttributeFactory('origin_date')
    PAPER_TYPE = DbAttributeFactory('paper_type')
    POSTAL_CODE = DbAttributeFactory('postal_code')
    REFERENCE = DbAttributeFactory('reference')
    ROLE = DbAttributeFactory('role')
    START_DATE = DbAttributeFactory('start_date')
    STREET_ADDRESS = DbAttributeFactory('street_address')
    VOTING_RIGHT = DbAttributeFactory('voting_right')
    WEB_URL = DbAttributeFactory('web_url')
