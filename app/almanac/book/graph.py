from ..generic import Book, Constant, singleton, init_annotations


@singleton
class LABEL(Book):
    CONSULTATION = 'Consultation'
    LEGIS_TERM = 'LegisTerm'
    LOCATION = 'Location'
    NAMED_ENTITY = 'NamedEntity'
    OPARL = 'Oparl'
    ORGANIZATION = 'Organization'
    PAPER = 'Paper'
    PERSON = 'Person'
    THREAD = 'Thread'


L = LABEL


# noinspection PyPep8Naming
@singleton
class NODE_LABEL(Book):
    LEGISLATIVE_TERM = (L.OPARL, L.LEGIS_TERM)
    THREAD = (L.OPARL, L.THREAD)
    PAPER = (L.OPARL, L.PAPER)
    OPARL_PERSON = (L.OPARL, L.NAMED_ENTITY, L.PERSON)
    OPARL_ORGANIZATION = (L.OPARL, L.NAMED_ENTITY, L.ORGANIZATION)
    OPARL_LOCATION = (L.OPARL, L.NAMED_ENTITY, L.LOCATION)
    CONSULTATION = (L.OPARL, L.CONSULTATION)


# noinspection PyPep8Naming
@singleton
class RELATION_TYPE(Book):
    CONCERNED = 'CONCERNED'  # Consultation -> Paper -> Thread
    DIRECTED = 'DIRECTED'  # Organization | Person -> Paper
    IN_PERIOD = 'IN_PERIOD'  # Thread -> Legis_term
    IS_MEMBER = 'IS_MEMBER'  # Person -> Organization
    LOCATED = 'LOCATED'  # Organization -> Location
    PARTICIPATED = 'PARTICIPATED'
    INDUCED = 'INDUCED'  # Organization | Person -> Paper


# noinspection PyPep8Naming
@singleton
class PROPERTY_KEY(Book):
    AUTHORITATIVE = 'authoritative'
    CLASSIFICATION = 'classification'
    DESCRIPTION = 'description'
    END_DATE = 'end_date'
    LOCALITY = 'locality'
    MODIFIED = 'modified'
    NAME = 'name'
    ORGANIZATION_TYPE = 'organization_type'
    OPARL_ID = 'oparl_id'
    ORIGIN_DATE = 'origin_date'
    PAPER_TYPE = 'paper_type'
    POSTAL_CODE = 'postal_code'
    REFERENCE = 'reference'
    ROLE = 'role'
    START_DATE = 'start_date'
    STREET_ADDRESS = 'street_address'
    VOTING_RIGHT = 'voting_right'
    WEB_URL = 'web_url'
