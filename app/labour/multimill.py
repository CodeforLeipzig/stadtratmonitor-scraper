import abc

from ..abstract.labour import AbcMultiMill

from .mediator import BasicMediator
from .mill import BasicMill


class BasicMultiMill(BasicMediator,
                     BasicMill,
                     AbcMultiMill,
                     abc.ABC):

    async def work(self) -> None:
        item = await self.queue.get()
        while item:
            for minion in self.minions:
                if minion.assign(item):
                    item = None
                    break
