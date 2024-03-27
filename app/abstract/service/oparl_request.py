import abc
import typing

from app.almanac.book.craft import CRAFT

from .. labour import AbcMinion


class AbcOparlRequest(AbcMinion, abc.ABC, badge=CRAFT.OPARL_REQUEST):
    """Defines interface that delegates requests to http or mirror"""

    async def get_page(self, url: str) -> typing.Awaitable[object]:
        ...

    async def get_object(self, url: str) -> typing.Awaitable[object]:
        ...

    async def get_html(self, url: str) -> typing.Awaitable[object]:
        ...

    async def get_pdf(self, url: str) -> typing.Awaitable[object]:
        ...
