from .initialisable import Initialisable
from .entitlable import Entitlable


def singleton[T](cls: type[T]) -> T:
    """decorator to create pseudo singleton"""
    return cls()


def init_annotations(cls: type):
    for key, type_ in cls.__annotations__.items():
        setattr(cls, key, type_(key))


class Book(Initialisable):
    def __setattr__(self, key, value):
        raise AttributeError('This is not a note book. Please don´t write into it.')

    def __getitem__[T](self, item: T) -> T:
        item = item.BADGE if (
                isinstance(item, Entitlable) or
                isinstance(item, type) and issubclass(item, Entitlable)
                ) else str(item)

        return getattr(self, item, None)
