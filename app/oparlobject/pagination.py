class Pagination:
    def __init__(self, content: dict):
        self.__content = content

    def items(self):
        items = self.__content.get('data')
        yield from (item for item in items)

    def next(self):
        links: dict = self.__content.get('links')
        return links.get('next') if links else None

