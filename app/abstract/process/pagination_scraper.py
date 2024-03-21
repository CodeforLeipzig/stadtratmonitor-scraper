import abc

from app.abstract import labour
from app.almanac.book.craft import CRAFT


class AbcPaginationScraper(labour.AbcMultiMill, abc.ABC, badge=CRAFT.PAGINATION_SCRAPPER):
    """Defines host for pagination processing workers"""
    ...


class AbcPaginationMinion(labour.AbcMinion, abc.ABC, badge=CRAFT.PAGINATION_SCRAPPER_MINION):
    """Defines worker for pagination processing"""
    ...
