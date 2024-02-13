import abc

from app.abstract import labour
from app.almanac.craft import CRAFT


class AbcPaginationScraper(labour.AbcMultiMill, abc.ABC, craft_title=CRAFT.PAGINATION_SCRAPPER):
    """Defines host for pagination processing workers"""
    ...


class AbcPaginationMinion(labour.AbcMinion, abc.ABC, craft_title=CRAFT.PAGINATION_SCRAPPER_MINION):
    """Defines worker for pagination processing"""
    ...
