from abc import abstractmethod, ABC
from typing import Any


class AbcNodeInterface(ABC):
    _content: Any
    _labels: list

    def __init__(self, content):
        self._content = content

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
    __slots__ = ('relation_type', 'source', 'target')
    relation_type: str
    source: AbcNodeInterface
    target: AbcNodeInterface

    def __init__(self, rel_type, source, target):
        self.relation_type = rel_type
        self.source = source
        self.target = target


class DbRelationFactory:
    __slots__ = ('_relation_type', )

    def __init__(self, relation_type: str):
        self._relation_type = relation_type

    def __call__(self, func, cls=DbRelation):
        def get_relation(source: AbcNodeInterface, target: AbcNodeInterface):
            return cls(self._relation_type, source, target)
        return DbRelationHook(get_relation)

    def with_class(self, cls):
        assert issubclass(cls, DbRelation)
        return lambda x: self(x, cls=cls)

    def as_generator(self, func, cls=DbRelation):
        def relation_generator(*args):
            for source, target in func(*args):
                yield cls(self._relation_type, source, target)
        return relation_generator

    def as_generator_with_class(self, cls):
        assert issubclass(cls, DbRelation)
        return lambda x: self.as_generator(x, cls=cls)


class LABELS(ABC):
    OPARL = 'Oparl'
    LEGIS_TERM = 'LegisTerm'
    THREAD = 'Thread'
    PAPER = 'Paper'
    NAMED_ENTITY = 'NamedEntity'
    PERSON = 'Person'
    ORGANIZATION = 'Organization'
    LOCATION = 'Location'


class RELATIONS(ABC):
    IS_MEMBER = DbRelationFactory('IS_MEMBER')
    LOCATED = DbRelationFactory('LOCATED')
    PART_OF = DbRelationFactory('PART_OF')
    DIRECTED = DbRelationFactory('DIRECTED')
    SUBMITTED = DbRelationFactory('SUBMITTED')


class ATTRIBUTES(ABC):
    DESCRIPTION = DbAttributeFactory('description')
    LOCALITY = DbAttributeFactory('locality')
    NAME = DbAttributeFactory('name')
    MODIFIED = DbAttributeFactory('modified')
    OPARL_ID = DbAttributeFactory('oparl_id')
    ORIGIN_DATE = DbAttributeFactory('origin_date')
    PAPER_TYPE = DbAttributeFactory('paper_type')
    POSTAL_CODE = DbAttributeFactory('postal_code')
    REFERENCE = DbAttributeFactory('reference')
    START_DATE = DbAttributeFactory('start_date')
    STREET_ADDRESS = DbAttributeFactory('street_address')
    END_DATE = DbAttributeFactory('end_date')
    WEB_URL = DbAttributeFactory('web_url')


class AbcOparlPaperInterface(AbcNodeInterface):
    _labels = [LABELS.OPARL,
               LABELS.PAPER]

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


class AbcOparlPersonInterface(AbcNodeInterface):
    _labels = [LABELS.OPARL,
               LABELS.NAMED_ENTITY,
               LABELS.PERSON]

    @abstractmethod
    def oparl_id(self): pass

    @abstractmethod
    def modified(self): pass

    @abstractmethod
    def name(self): pass

    @abstractmethod
    def web_url(self): pass


class AbcOparlOrganizationInterface(AbcNodeInterface):
    _labels = [LABELS.OPARL,
               LABELS.NAMED_ENTITY,
               LABELS.ORGANIZATION]

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


class AbcOparlLocationInterface(AbcNodeInterface):
    _labels = [LABELS.OPARL,
              LABELS.NAMED_ENTITY,
              LABELS.LOCATION]

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

