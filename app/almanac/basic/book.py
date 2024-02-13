from .entitled import Entitled
from .initilized import Initialized


def overwrite[T](cls: type[T]) -> T:
    """decorator to create pseudo singleton"""
    return cls()


def init_annotations(cls: type):
    for key, type_ in cls.__annotations__.items():
        setattr(cls, key, type_(key))


class Book(Initialized):
    def __setattr__(self, key, value):
        raise AttributeError('This is not a note book. Please don´t write into it.')

    def __getitem__[T](self, item: T) -> T:
        item = item.BADGE if (
                isinstance(item, Entitled) or
                isinstance(item, type) and issubclass(item, Entitled)
                ) else str(item)

        if hasattr(self, item):
            return getattr(self, item)


class Constant(str):
    """subclass from str, just for enabling ´is´ comparator"""

