from collections import deque
from . import fakerequest as request
from ._factory import Factory
from ._objects import \
    Basic, Paper, Person, Organization, Location, Membership, Consultation


class Oparl:
    START_URL = request.START_URL
    MAX_PAGES = 10
    BUFFER_SIZE = 1000

    buffer = deque([], BUFFER_SIZE)
    factory = Factory
    factory_mapping = {None: Basic,
                       "https://schema.oparl.org/1.1/Paper": Paper,
                       "https://schema.oparl.org/1.1/Person": Person,
                       "https://schema.oparl.org/1.1/Organization": Organization,
                       "https://schema.oparl.org/1.1/Location": Location,
                       "https://schema.oparl.org/1.1/Membership": Membership,
                       "https://schema.oparl.org/1.1/Consultation": Consultation}

    @classmethod
    def pagination(cls):
        max_pages = cls.MAX_PAGES
        url = cls.START_URL
        factory = cls.factory
        page_count = 0

        while url and page_count < max_pages:
            page = request.get(url)
            page_count += 1
            for item in page.get('data'):
                yield factory.fabricate(item)
                url = page.get('links')
                if url:
                    url = url.get('next')

    @classmethod
    def _is_missing(cls, _, item):
        if item is None:
            return NOPARL

    @classmethod
    def _wrap_oparl(cls, _: Factory, item):
        if isinstance(item, dict):
            o_cls = cls.factory_mapping.get(item.get('type'))
            o_obj = o_cls(item)
            cls.buffer.append(o_obj)
            return o_obj

    @classmethod
    def _ask_buffer(cls, _: Factory, item):
        if isinstance(item, str) and item.startswith('http'):
            for buffered_item in cls.buffer:
                if item == buffered_item.oparl_id:
                    return buffered_item
        elif isinstance(item, Basic):
            for buffered_item in cls.buffer:
                if item == buffered_item:
                    return buffered_item
        else:
            return None

    @classmethod
    def _retrieve_from_api(cls, factory: Factory, item):
        if isinstance(item, str) and item.startswith('http'):
            result = request.get(item)
            result = factory.fabricate(result)
            cls.buffer.append(result)
            return result


Oparl.factory.add_function(Oparl._wrap_oparl, Oparl._ask_buffer, Oparl._retrieve_from_api)
