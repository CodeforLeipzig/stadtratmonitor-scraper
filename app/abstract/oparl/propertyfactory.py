import abc
import typing


class AbcOparlProperty(abc.ABC):
    @abc.abstractmethod
    def __get__(self, instance, owner): ...

    @abc.abstractmethod
    def __set__(self, instance, value): ...

    @abc.abstractmethod
    def workflow(self) -> typing.Iterable[typing.Callable]: ...
