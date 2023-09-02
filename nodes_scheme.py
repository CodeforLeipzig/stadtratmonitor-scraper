from abc import abstractmethod, ABC
from typing import Any


class BasicNodeInterface:
    _content: Any
    _labels: list
    __slots__ = ('_content', '_labels')

    def __init__(self, content, labels=None):
        self._content = content
        self._labels = labels

    @property
    def labels(self):
        for label in self._labels:
            yield label

    def attributes(self):
        for cls in self.__class__.mro():
            for key, attr in cls.__dict__.items():
                if isinstance(attr, DbAttributeHook):
                    yield getattr(self, key)

    def primary_keys(self):
        for property_ in self.attributes():
            property_: DbAttribute
            if property_.is_primary():
                yield property_

    def non_primary_keys(self):
        for attribute in self.attributes():
            attribute: DbAttribute
            if not attribute.is_primary():
                yield attribute

    def relations(self):
        for cls in self.__class__.mro():
            for key, attr in cls.__dict__.items():
                if isinstance(attr, DbRelationHook):
                    yield getattr(self, key)


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
        assert isinstance(other, self.__class__)
        if self.key() == other.key() and self.value() == other.value():
            return True


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

    def __init__(self, relation_type, source, target, *, content=None):
        self._relation_type = relation_type
        self._source = source
        self._target = target
        self._content = content

    @property
    def source(self):
        return self._source

    @property
    def target(self):
        return self._target


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
        return lambda x: self(x, cls=cls)

    def as_generator(self, func, cls=DbRelation):
        def relation_generator(*args):
            for items in func(*args):
                yield cls(self._relation_type, *items)
        return relation_generator

    def as_generator_with_class(self, cls):
        assert issubclass(cls, DbRelation)
        return lambda x: self.as_generator(x, cls=cls)


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
    INDUCED = DbRelationFactory('SUBMITTED')  # Organization | Person -> Paper


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



class AbcOparlPersonInterface(BasicNodeInterface):
    def __init__(self, content):
        super().__init__(content, labels=[LABELS.OPARL, LABELS.NAMED_ENTITY, LABELS.PERSON])

    @abstractmethod
    def oparl_id(self): pass

    @abstractmethod
    def modified(self): pass

    @abstractmethod
    def name(self): pass

    @abstractmethod
    def web_url(self): pass


class AbcOparlOrganizationInterface(BasicNodeInterface):
    def __init__(self, content):
        super().__init__(content, labels=[LABELS.OPARL, LABELS.NAMED_ENTITY, LABELS.ORGANIZATION])

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


class AbcOparlLocationInterface(BasicNodeInterface):
    def __init__(self, content):
        super().__init__(content, labels=[LABELS.OPARL, LABELS.NAMED_ENTITY, LABELS.LOCATION])

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


class AbcOparlConsultationInterface(BasicNodeInterface):
    def __init__(self, content):
        super().__init__(content, labels=[LABELS.OPARL, LABELS.CONSULTATION])

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
    def voting_right(self): pass

    @abstractmethod
    def role(self): pass

    @abstractmethod
    def start_date(self): pass

    @abstractmethod
    def end_date(self): pass

