from ..abstract.labour import AbcSupervisor
from ..abstract.process.pagination_scraper import AbcPaginationScraper
from app.almanac.book.craft import CRAFT
from ..config import ConfigType
from ..labour import BasicMinion


class UrlGeneratorCnf(ConfigType, badge=CRAFT.URL_GENERATOR):
    frist_page: int
    last_page: int
    base_str: str


class UrlGenerator(BasicMinion, badge=CRAFT.URL_GENERATOR):
    config: UrlGeneratorCnf
    supervisor: AbcSupervisor

    def __init__(self, supervisor):
        super().__init__(supervisor)
        self.urls = self.url_generator(self.config.frist_page,
                                       self.config.last_page,
                                       self.config.base_str)

    async def work(self, *_) -> None:
        try:
            url = next(self.urls)
        except StopIteration:
            self.stop()
            return
        await self.supervisor[AbcPaginationScraper].put(url)

    @staticmethod
    def url_generator(min_, max_, str_):
        for number in range(min_, max_):
            yield str_.format(number=number)
