import abc
import typing

from app.almanac.book.craft import CRAFT

from ..labour import AbcMinion, AbcSupervisor


class AbcGraphRequest(AbcMinion, abc.ABC, badge=CRAFT.GRAPH_REQUEST):
    """Defines Interface for requests against graph database."""

    @abc.abstractmethod
    def put(self, entity: typing.Any) -> typing.Awaitable: ...

    @abc.abstractmethod
    def get(self, entity: typing.Any) -> typing.Awaitable: ...

    @abc.abstractmethod
    def upsert(self, entity: typing.Any) -> typing.Awaitable: ...


class AbcManufactory(AbcSupervisor, abc.ABC, badge=CRAFT.MANUFACTORY):
    """Defines main instance that holds workers of coroutines, threads and processes"""
    ...

# class AbcUrlGenerator(labour.AbcLabour, abc.ABC, badge=CRAFT.URL_GENERATOR):
#     """Defines interface for url generator"""
#     ...
