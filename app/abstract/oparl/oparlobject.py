import abc
import datetime
import typing

from ...almanac import Entitlable


class AbcOparlObject(Entitlable, abc.ABC):
    ID: str
    TYPE: str
    CREATED: datetime.datetime
    MODIFIED: datetime.datetime
    DELETED: bool

    @property
    @abc.abstractmethod
    def content(self) -> dict: ...

    @abc.abstractmethod
    def resolve(self) -> typing.Awaitable: ...

    @abc.abstractmethod
    def is_resolvable(self) -> bool: ...

    @abc.abstractmethod
    def is_valid(self) -> bool: ...

    @abc.abstractmethod
    def is_deleted(self) -> bool: ...

