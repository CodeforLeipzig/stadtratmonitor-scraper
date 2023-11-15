from ._basic import Attributes, PropertyFactory


class ATTRIBUTES(Attributes):
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
