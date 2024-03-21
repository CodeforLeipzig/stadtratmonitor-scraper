import typing
from functools import reduce

from ...abstract.oparl import AbcOparlObject, AbcOparlProperty


class OparlProperty(AbcOparlProperty):
    def __init__(self, key, *work):
        self.__key = key
        self.__work = work

    def __get__(self, instance: AbcOparlObject, owner):
        if not instance: return
        return reduce(lambda x, y: y(x), self.workflow(), instance.content.get(self.__key))

    def __set__(self, instance, value):
        pass

    def workflow(self) -> typing.Iterable[typing.Callable]:
        yield from self.__work
