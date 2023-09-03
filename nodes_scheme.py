from abc import abstractmethod, ABC
from typing import Any, Generator


class BasicNodeInterface:
    _content: Any
    _thread_labels: list
    __slots__ = ('_content', '_labels')

    def __init__(self, content, labels):
        self._content = content
        self._labels = labels

    def __eq__(self, other):
        if self is other or \
                isinstance(other, BasicNodeInterface) and \
                sorted(self.labels) == sorted(other.labels) and \
                sorted(self.attributes(), key=lambda x: x.key()) == \
                sorted(other.attributes(), key=lambda x: x.key()):
            return True
        else:
            return False

    @property
    def labels(self):
        for label in self._labels:
            yield label

    def attributes(self):
        for key, attr in self.__class__.__dict__.items():
            if isinstance(attr, DbAttributeHook):
                yield getattr(self, key)

    def primary_keys(self):
        for attribute in self.attributes():
            attribute: DbAttribute
            if attribute.is_primary():
                yield attribute

    def non_primary_keys(self):
        for attribute in self.attributes():
            attribute: DbAttribute
            if not attribute.is_primary():
                yield attribute

    def relations(self):
        for key, attr in self.__class__.__dict__.items():
            if isinstance(attr, DbRelationHook):
                relation = getattr(self, key)
                if isinstance(relation, Generator):
                    for rel in relation:
                        yield rel
                else:
                    yield relation


class DbAttribute:
    __slots__ = ('_get_key', '_get_value', '_is_primary')

    def __init__(self, key_getter, value_getter, is_primary):
        self._get_key = key_getter
        self._get_value = value_getter
        self._is_primary = is_primary

    def key(self):
        return self._get_key()

    def value(self):
        return self._get_value()

    def is_primary(self):
        return self._is_primary

    def __iter__(self):
        yield self.key(), self.value()

    def __eq__(self, other):
        if self is other or \
                isinstance(other, DbAttribute) and \
                self.key() == other.key() and \
                self.value() == other.value():
            return True
        else:
            return False


class DbAttributeHook(property):
    pass


class DbRelationHook(property):
    pass


class DbAttributeFactory:
    __slots__ = ('_key',)

    def __init__(self, key: str):
        self._key = key

    def key(self):
        return self._key

    def __call__(self, func, is_primary=False):
        def get_property(instance):
            return DbAttribute(self.key, lambda: func(instance), is_primary)

        return DbAttributeHook(get_property)

    def as_primary(self, func):
        return self(func, is_primary=True)


class DbRelation:
    __slots__ = ('_relation_type', '_source', '_target', '_content')
    _relation_type: str
    _source: BasicNodeInterface
    _target: BasicNodeInterface
    _content: (BasicNodeInterface, None)

    def __init__(self, relation_type, source, target, *, content=None):
        self._relation_type = relation_type
        self._source = source
        self._target = target
        self._content = content

    def __eq__(self, other):
        if self is other or \
                isinstance(other, DbRelation) and \
                self.relation_type == other.relation_type and \
                self.source == other.source and \
                self.target == other.target and \
                self._content == other._content:
            return True
        else:
            return False

    @property
    def source(self):
        return self._source

    @property
    def target(self):
        return self._target

    @property
    def relation_type(self):
        return self._relation_type


class DbRelationFactory:
    __slots__ = ('_relation_type', )

    def __init__(self, relation_type: str):
        self._relation_type = relation_type

    def __call__(self, func, cls=DbRelation):
        def get_relation(*args):
            return cls(self._relation_type, *func(*args))

        return DbRelationHook(get_relation)

    def with_class(self, cls):
        assert issubclass(cls, DbRelation)
        return DbRelationHook(lambda x: self(x, cls=cls))

    def as_generator(self, func, cls=DbRelation):
        def relation_generator(*args):
            for items in func(*args):
                yield cls(self._relation_type, *items)

        return DbRelationHook(relation_generator)

    def as_generator_with_class(self, cls):
        assert issubclass(cls, DbRelation)
        return DbRelationHook(lambda x: self.as_generator(x, cls=cls))


class LABELS(ABC):
    CONSULTATION = 'Consultation'
    LEGIS_TERM = 'LegisTerm'
    LOCATION = 'Location'
    NAMED_ENTITY = 'NamedEntity'
    OPARL = 'Oparl'
    ORGANIZATION = 'Organization'
    PAPER = 'Paper'
    PERSON = 'Person'
    THREAD = 'Thread'


class RELATIONS(ABC):
    CONCERNED = DbRelationFactory('CONCERNED')  # Consultation -> Paper -> Thread
    DIRECTED = DbRelationFactory('DIRECTED')  # Organization | Person -> Paper
    IN_PERIOD = DbRelationFactory('IN_PERIOD')  # Thread -> Legis_term
    IS_MEMBER = DbRelationFactory('IS_MEMBER')  # Person -> Organization
    LOCATED = DbRelationFactory('LOCATED')  # Organization -> Location
    PARTICIPATED = DbRelationFactory('PARTICIPATED')
    INDUCED = DbRelationFactory('INDUCED')  # Organization | Person -> Paper


class ATTRIBUTES(ABC):
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


class AbcOparlPaperInterface(BasicNodeInterface):
    def __init__(self, content):
        super().__init__(content, labels=[LABELS.OPARL, LABELS.PAPER])

    @abstractmethod
    def oparl_id(self): pass

    @abstractmethod
    def modified(self): pass

    @abstractmethod
    def reference(self): pass

    @abstractmethod
    def paper_type(self): pass

    @abstractmethod
    def web_url(self): pass

    @abstractmethod
    def origin_date(self): pass

    @abstractmethod
    def directors(self): pass

    @abstractmethod
    def originators(self): pass

    @abstractmethod
    def consultations(self): pass


_oparl_person_labels = [LABELS.OPARL, LABELS.NAMED_ENTITY, LABELS.PERSON]


class AbcOparlPersonInterface(BasicNodeInterface):
    def __init__(self, content):
        super().__init__(content, _oparl_person_labels)

    @abstractmethod
    def oparl_id(self): pass

    @abstractmethod
    def modified(self): pass

    @abstractmethod
    def name(self): pass

    @abstractmethod
    def web_url(self): pass


_oparl_organization_labels = [LABELS.OPARL, LABELS.NAMED_ENTITY, LABELS.ORGANIZATION]


class AbcOparlOrganizationInterface(BasicNodeInterface):
    def __init__(self, content):
        super().__init__(content, _oparl_organization_labels)

    @abstractmethod
    def oparl_id(self): pass

    @abstractmethod
    def modified(self): pass

    @abstractmethod
    def name(self): pass

    @abstractmethod
    def start_date(self): pass

    @abstractmethod
    def end_date(self): pass


_oparl_location_labels = [LABELS.OPARL, LABELS.NAMED_ENTITY, LABELS.LOCATION]


class AbcOparlLocationInterface(BasicNodeInterface):
    def __init__(self, content):
        super().__init__(content, _oparl_location_labels)

    @abstractmethod
    def oparl_id(self): pass

    @abstractmethod
    def modified(self): pass

    @abstractmethod
    def locality(self): pass

    @abstractmethod
    def postal_code(self): pass

    @abstractmethod
    def description(self): pass

    @abstractmethod
    def street_address(self): pass


_consultation_labels = [LABELS.OPARL, LABELS.CONSULTATION]


class AbcOparlConsultationInterface(BasicNodeInterface):
    def __init__(self, content):
        super().__init__(content, _consultation_labels)

    @abstractmethod
    def oparl_id(self): pass

    @abstractmethod
    def modified(self): pass

    @abstractmethod
    def paper(self): pass

    @abstractmethod
    def organizations(self): pass

    @abstractmethod
    def authoritative(self): pass

    @abstractmethod
    def role(self): pass


class AbcOparlMembershipInterface(DbRelation):
    @abstractmethod
    def oparl_id(self): pass

    @abstractmethod
    def modified(self): pass

    @abstractmethod
    def voting_right(self): pass

    @abstractmethod
    def role(self): pass

    @abstractmethod
    def start_date(self): pass

    @abstractmethod
    def end_date(self): pass
