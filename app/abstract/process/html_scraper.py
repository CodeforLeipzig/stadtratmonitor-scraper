import abc

from app.abstract import labour
from app.almanac.craft import CRAFT


class AbcHtmlScraper(labour.AbcMill, abc.ABC, craft_title=CRAFT.HTML_SCRAPER):
    """Defines worker for html processing"""
    ...
