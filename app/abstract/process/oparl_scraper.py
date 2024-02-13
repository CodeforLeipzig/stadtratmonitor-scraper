import abc

from app.abstract import labour
from app.almanac.craft import CRAFT


class AbcOparlScraper(labour.AbcMultiMill, abc.ABC, craft_title=CRAFT.OPARL_SCRAPER):
    """Defines host for oparl object processing workers"""
    ...


class AbcOparlScraperMinion(labour.AbcMinion, abc.ABC, craft_title=CRAFT.OPARL_SCRAPER_MINION):
    """Defines worker for oparl object processing"""
    ...
