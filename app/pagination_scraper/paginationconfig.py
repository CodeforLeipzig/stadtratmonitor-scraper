from app.almanac.book.craft import CRAFT
from app.config import ConfigType


class PaginationScraperCnf(ConfigType, badge=CRAFT.PAGINATION_SCRAPPER):
    workers: int
    put_next: bool
    queue_size: int

