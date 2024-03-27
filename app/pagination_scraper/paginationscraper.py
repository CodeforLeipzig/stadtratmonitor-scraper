import typing
import asyncio

from app.abstract.process.pagination_scraper import AbcPaginationScraper, AbcPaginationMinion
from app.almanac.book.craft import CRAFT
from app.labour import BasicMultiMill

from .paginationconfig import PaginationScraperCnf
from .paginationminion import PaginationMinion


class PaginationScraper(BasicMultiMill, AbcPaginationScraper, badge=CRAFT.PAGINATION_SCRAPPER):
    config: PaginationScraperCnf
    minion: AbcPaginationMinion
    queue: asyncio.Queue

    def init_minions(self, minion_type) -> typing.Iterable[PaginationMinion]:
        return (PaginationMinion(self) for _ in range(self.config.workers))

    def init_queue(self) -> asyncio.Queue:
        return asyncio.Queue(maxsize=self.config.queue_size)

    async def __call__(self):
        await asyncio.gather(super().__call__(), *(minion() for minion in self.minions))
