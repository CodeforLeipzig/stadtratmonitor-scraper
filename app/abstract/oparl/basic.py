import abc
import typing


class OparlObject(abc.ABC):
    @property
    @abc.abstractmethod
    def content(self) -> dict: ...

    @property
    @abc.abstractmethod
    def is_resolvable(self) -> bool: ...

    @property
    @abc.abstractmethod
    def is_valid(self) -> bool: ...

    @property
    @abc.abstractmethod
    def is_deleted(self) -> bool: ...


class PropertyFactory(abc.ABC):
    @abc.abstractmethod
    def __get__(self, instance, owner): ...

    @abc.abstractmethod
    def __set__(self, instance, value): ...

    @abc.abstractmethod
    def workflow(self) -> typing.Iterable[typing.Callable]: ...
