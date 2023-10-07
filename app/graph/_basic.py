from abc import ABC, abstractmethod


class Item(ABC):
    __slots__ = ()

    @abstractmethod
    def __eq__(self, other):
        pass


class Property(Item):
    __slots__ = ('_get_key', '_get_value', '_is_primary')

    def __init__(self, key_getter, value_getter, is_primary):
        self._get_key = key_getter
        self._get_value = value_getter
        self._is_primary = is_primary

    def key(self):
        return self._get_key()

    def value(self):
        return self._get_value()

    def is_primary(self):
        return self._is_primary

    def __iter__(self):
        yield self.key(), self.value()

    def __eq__(self, other):
        if self is other or \
                isinstance(other, Property) and \
                self.key() == other.key() and \
                self.value() == other.value():
            return True
        else:
            return False


class PropertyHook(property):
    pass
