from datetime import date, datetime
from typing import Generator


class Factory:
    pipeline = []

    @classmethod
    def add_function(cls, *args):
        for arg in args:
            cls.pipeline.append(arg)

    @classmethod
    def fabricate(cls, item: (str, dict)):
        for func in cls.pipeline:
            result = func(cls, item)
            if result:
                return result

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


