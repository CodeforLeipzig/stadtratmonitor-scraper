import abc
import asyncio
import typing

from .minion import BasicMinion
from ..abstract.labour import AbcMill


class BasicMill(BasicMinion, AbcMill, abc.ABC):
    def __init__(self):
        self.__queue = self.init_queue()
        super().__init__()

    @abc.abstractmethod
    def init_queue(self) -> asyncio.Queue: ...

    @property
    def queue(self):
        return self.__queue

    def put(self, item) -> typing.Awaitable:
        return self.__queue.put(item)
