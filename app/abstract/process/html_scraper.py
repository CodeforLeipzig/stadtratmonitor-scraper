import abc

from app.abstract import labour
from app.almanac.book.craft import CRAFT


class AbcHtmlScraper(labour.AbcMill, abc.ABC, badge=CRAFT.HTML_SCRAPER):
    """Defines worker for html processing"""
    ...
