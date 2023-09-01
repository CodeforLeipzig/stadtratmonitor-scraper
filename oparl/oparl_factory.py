import oparl.fakerequest as request
from datetime import date, datetime
from typing import Generator


class Factory:
    mapping = {}
    request = request

    @classmethod
    def fabricate(cls, item: (str, dict)):
        if item is None:
            return

        elif isinstance(item, str) and item.startswith('http'):
            response = cls.request.get(item)
            return cls.fabricate(response)

        elif isinstance(item, dict):
            object_type = item.get('type')
            oparl_object = cls.mapping.get(object_type)
            return oparl_object(item)

        else:
            message = f'unsupported item {item} type {type(item)}, expected url_str or dict with key "type"'
            raise TypeError(message)

    @classmethod
    def as_oparl_object(cls, func):
        def oparl_object(*args):
            return cls.fabricate(func(*args))
        return oparl_object

    @classmethod
    def as_oparl_object_generator(cls, func):
        def oparl_object_generator(*args):
            for item in cls.as_simple_generator(func)(*args):
                yield Factory.fabricate(item)
        return oparl_object_generator

    @staticmethod
    def as_date_type(func):
        def convert_date(*args) -> date:
            date_str = func(*args)
            return date.fromisoformat(date_str) if date_str else None

        return convert_date

    @staticmethod
    def as_datetime_type(func):
        def convert_datetime(*args) -> date:
            date_str = func(*args)
            return datetime.fromisoformat(date_str) if date_str else None

        return convert_datetime

    @staticmethod
    def as_simple_generator(func):
        def generator(*args) -> Generator:
            item = func(*args)
            if isinstance(item, list):
                for sub_item in item:
                    if sub_item:
                        yield sub_item

        return generator


