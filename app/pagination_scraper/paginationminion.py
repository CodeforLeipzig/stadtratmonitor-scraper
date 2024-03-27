from app.abstract.process.pagination_scraper import AbcPaginationScraper, AbcPaginationMinion
from app.abstract.service.oparl_request import AbcOparlRequest
from app.almanac.book.craft import CRAFT
from app.labour import BasicMinion

from .paginationconfig import PaginationScraperCnf


class PaginationMinion(BasicMinion, AbcPaginationMinion, badge=CRAFT.PAGINATION_SCRAPPER_MINION):
    supervisor: AbcPaginationScraper
    config: PaginationScraperCnf

    async def work(self, item: str, *_) -> None:
        oparl_request = self.supervisor[AbcOparlRequest]
        pagination = await oparl_request.get_page(item)

        if self.config.put_next:
            if next_page := pagination.next:
                await self.supervisor.put(next_page)
