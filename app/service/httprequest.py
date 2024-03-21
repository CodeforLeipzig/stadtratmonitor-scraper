import asyncio
import typing

from ..abstract.service.http_request import AbcHttpRequest
from ..labour import BasicMill

class Semaphore:
    def __init__(self, c: int):
        self.__c = self.__n = c
    def up(self):
        self.__c = min(self.__n, self.__c)

    def down(self):
        self.__c = max(0, self.__c)

    def is_blocked(self):
        return self.__c == 0


class HtmlRequest(BasicMill, AbcHttpRequest):
    def __init__(self, *args):
        super().__init__(*args)
        self.__counter = 10

    def init_queue(self) -> asyncio.Queue:
        return asyncio.Queue()

    async def work(self) -> None:
        if self.__counter == 0:
            return await asyncio.sleep(0)


            self.__counter -= 1
        item = await self.get()

    def

    async def get_page(self, url: str) -> object:
        # await
        # convert
        # return
        ...

    async def get_object(self, url: str) -> object:
        # await
        # convert
        # return
        ...

    async def get_html(self, url: str) -> object:
        # await
        # convert
        # return
        ...

    async def get_pdf(self, url: str) -> object:
        # await
        # convert
        # return
        ...
class Semap