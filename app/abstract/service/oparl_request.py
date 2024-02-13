import abc

from .. import labour
from ...almanac.craft import CRAFT


class AbcOparlRequest(labour.AbcMediator, abc.ABC, badge=CRAFT.OPARL_REQUEST):
    """Defines interface that delegates requests to http or mirror"""
    ...
