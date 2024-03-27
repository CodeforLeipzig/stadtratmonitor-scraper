from contextlib import contextmanager
import abc
import asyncio
import threading

from ..abstract.labour import AbcMinion, AbcSupervisor

from .labour import BasicLabour


class BasicMinion(BasicLabour, AbcMinion, abc.ABC):
    supervisor: AbcSupervisor

    def __init__(self, supervisor, *args):
        super().__init__(*args)
        self.__supervisor = supervisor
        self.__semaphore = threading.Semaphore()
        self.__item = None

    @contextmanager
    def loop(self):
        if self.__item is None: return asyncio.sleep(0)
        with self.status.busy_and_idle_cnx:
            yield self.work(self.__item)

    @abc.abstractmethod
    async def work(self, item, *args, **kwargs):
        ...

    @property
    def supervisor(self) -> AbcSupervisor:
        return self.__supervisor

    @property
    def semaphore(self):
        return self.__semaphore

    def assign(self, item: object) -> bool:
        if self.__semaphore.acquire(blocking=False):
            self.__item = item
            return True
        return False

    def release(self):
        self.__item = None
        self.__semaphore.release()
