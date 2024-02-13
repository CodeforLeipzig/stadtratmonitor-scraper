import abc
import typing

from .minion import AbcMinion


class AbcMill(AbcMinion, abc.ABC):
    @abc.abstractmethod
    def put(self, item) -> typing.Awaitable:
        """put something into a mill and it will do something with it"""
        ...
