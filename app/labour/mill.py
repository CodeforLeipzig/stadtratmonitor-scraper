import abc
import asyncio

from .minion import BasicMinion
from ..abstract.labour import AbcMill


class BasicMill(BasicMinion, AbcMill, abc.ABC):
    _queue: asyncio.Queue

    async def put(self, item) -> None:
        await self._queue.put(item)
