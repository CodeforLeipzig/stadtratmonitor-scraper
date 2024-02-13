import abc
import typing

from .. import labour
from ...almanac.craft import CRAFT


class AbcMirrorRequest(labour.AbcMinion, abc.ABC, badge=CRAFT.MIRROR_REQUEST):
    """Defines interface for requests against mirror db. Should only be used within oparl request"""

    @abc.abstractmethod
    def get_html(self, url) -> typing.Awaitable[bytes]: ...

    @abc.abstractmethod
    def get_oparl(self, url) -> typing.Awaitable[dict]: ...

    @abc.abstractmethod
    def get_pagination(self, url) -> typing.Awaitable[dict]: ...

    @abc.abstractmethod
    def get_pdf(self, url) -> typing.Awaitable[bytes]: ...

    @abc.abstractmethod
    def put_html(self, url: str, data: bytes) -> typing.Awaitable: ...

    @abc.abstractmethod
    def put_oparl(self, url: str, data: dict) -> typing.Awaitable: ...

    @abc.abstractmethod
    def put_pagination(self, url: str, data: dict) -> typing.Awaitable: ...

    @abc.abstractmethod
    def put_pdf(self, url: str, data: bytes) -> typing.Awaitable: ...
