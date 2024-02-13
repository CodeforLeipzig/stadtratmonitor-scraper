import abc
import typing

from .. import labour
from ...almanac.craft import CRAFT


class AbcHttpRequest(labour.AbcMediator, abc.ABC, badge=CRAFT.HTTP_REQUEST):
    """Defines interface for http request. Is a host for worker. Should only be used within oparl request"""

    @abc.abstractmethod
    def get_html(self, url) -> typing.Awaitable[bytes]: ...

    @abc.abstractmethod
    def get_oparl(self, url) -> typing.Awaitable[dict]: ...

    @abc.abstractmethod
    def get_pagination(self, url) -> typing.Awaitable[dict]: ...

    @abc.abstractmethod
    def get_pdf(self, url) -> typing.Awaitable[bytes]: ...


class AbcHttpRequestMinion(labour.AbcMinion, abc.ABC, badge=CRAFT.HTTP_REQUEST_MINION):
    """Defines worker for multiple http requests."""
    ...
