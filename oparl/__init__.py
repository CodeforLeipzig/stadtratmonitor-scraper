import oparl.fakerequest as request
from oparl.oparl_factory import Factory
from oparl.oparl_objects import Basic, Paper, Person, Organization, Location, Membership


START_URL = request.START_URL

Factory.request = request
Factory.mapping = {None: Basic,
                   "https://schema.oparl.org/1.1/Paper": Paper,
                   "https://schema.oparl.org/1.1/Person": Person,
                   "https://schema.oparl.org/1.1/Organization": Organization,
                   "https://schema.oparl.org/1.1/Location": Location,
                   "https://schema.oparl.org/1.1/Membership": Membership}


class Pagination:
    def __init__(self, start_url=START_URL, max_pages=5):
        self.start_url = start_url
        self.max_pages = max_pages

    def __iter__(self):
        max_pages = self.max_pages
        url = self.start_url
        page_count = 0
        while url and page_count < max_pages:
            page = request.get(url)
            page_count += 1
            for item in page.get('data'):
                yield Factory.fabricate(item)
                url = page.get('links')
                if url:
                    url = url.get('next')


if __name__ == '__main__':
    for item in Pagination():
        print(item)