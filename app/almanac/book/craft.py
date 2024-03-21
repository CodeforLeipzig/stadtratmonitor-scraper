from ..generic import Book, Constant, singleton, init_annotations


@singleton
class CRAFT(Book, initializer=init_annotations):
    GRAPH_REQUEST: Constant
    HTML_SCRAPER: Constant
    HTTP_REQUEST: Constant
    HTTP_REQUEST_MINION: Constant
    MANUFACTORY: Constant
    MIRROR_REQUEST: Constant
    OPARL_REQUEST: Constant
    OPARL_SCRAPER: Constant
    OPARL_SCRAPER_MINION: Constant
    PAGINATION_SCRAPPER: Constant
    PAGINATION_SCRAPPER_MINION: Constant
    URL_GENERATOR: Constant

