import asyncio
from .missing import MISSING


class Promise:
    __result = MISSING

    async def result(self):
        while self.__result is MISSING:
            await asyncio.sleep(0)
        return self.__result

    def __set_result(self, item):
        self.__result = item

    @classmethod
    def make(cls):
        instance = cls()
        return instance, instance.__set_result
