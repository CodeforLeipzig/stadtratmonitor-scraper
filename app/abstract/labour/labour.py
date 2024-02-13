import abc
import typing

from .. import basic
from .. import config


class AbcLabour(basic.Entitled, abc.ABC):

    @abc.abstractmethod
    def __call__(self) -> typing.Awaitable:
        """run command, no args, no return"""
        ...

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """yes, even proletarians got names, they need them to be blamed"""
        ...

    @property
    @abc.abstractmethod
    def status(self) -> str:
        """but be kind, ask them how they are"""
        ...

    @abc.abstractmethod
    def stop(self) -> None:
        """everybody needs to rest sometimes"""
        ...

    @property
    @abc.abstractmethod
    def config(self) -> config.AbcConfig:
        """a place for the labours basic working instructions"""
        ...
