from .basic import book

C = book.Constant


@book.overwrite
class CRAFT(book.Book, initializer=book.init_annotations):
    GRAPH_REQUEST: C
    HTML_SCRAPER: C
    HTTP_REQUEST: C
    HTTP_REQUEST_MINION: C
    MANUFACTORY: C
    MIRROR_REQUEST: C
    OPARL_REQUEST: C
    OPARL_SCRAPER: C
    OPARL_SCRAPER_MINION: C
    PAGINATION_SCRAPPER: C
    PAGINATION_SCRAPPER_MINION: C
    URL_GENERATOR: C

