import abc
import typing

from .. import labour
from ...almanac.craft import CRAFT


class AbcGraphRequest(labour.AbcMinion, abc.ABC, badge=CRAFT.GRAPH_REQUEST):
    """Defines Interface for requests against graph database."""

    @abc.abstractmethod
    def put(self, entity: typing.Any) -> typing.Awaitable: ...

    @abc.abstractmethod
    def get(self, entity: typing.Any) -> typing.Awaitable: ...

    @abc.abstractmethod
    def upsert(self, entity: typing.Any) -> typing.Awaitable: ...


class AbcManufactory(labour.AbcSupervisor, abc.ABC, badge=CRAFT.MANUFACTORY):
    """Defines main instance that holds workers of coroutines, threads and processes"""
    ...

# class AbcUrlGenerator(labour.AbcLabour, abc.ABC, badge=CRAFT.URL_GENERATOR):
#     """Defines interface for url generator"""
#     ...
