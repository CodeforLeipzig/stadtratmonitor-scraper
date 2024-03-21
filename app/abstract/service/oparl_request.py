import abc

from app.almanac.book.craft import CRAFT

from .. labour import AbcMinion


class AbcOparlRequest(AbcMinion, abc.ABC, badge=CRAFT.OPARL_REQUEST):
    """Defines interface that delegates requests to http or mirror"""
