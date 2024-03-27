import abc
import typing

from app.almanac.book.craft import CRAFT

from ..labour import AbcMediator, AbcMinion


class AbcHttpRequest(AbcMediator, abc.ABC, badge=CRAFT.HTTP_REQUEST):
    """Defines interface for http request. Is a host for worker. Should only be used within oparl request"""

    @abc.abstractmethod
    def get_html(self, url) -> typing.Awaitable[bytes]: ...

    @abc.abstractmethod
    def get_object(self, url) -> typing.Awaitable[dict]: ...

    @abc.abstractmethod
    def get_page(self, url) -> typing.Awaitable[dict]: ...

    @abc.abstractmethod
    def get_pdf(self, url) -> typing.Awaitable[bytes]: ...


class AbcHttpRequestMinion(AbcMinion, abc.ABC, badge=CRAFT.HTTP_REQUEST_MINION):
    """Defines worker for multiple http requests."""
