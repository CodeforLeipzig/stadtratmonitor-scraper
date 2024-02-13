import abc

from ..abstract.labour import AbcMultiMill

from .mediator import BasicMediator
from .mill import BasicMill


class BasicMultiMill(BasicMediator,
                     BasicMill,
                     AbcMultiMill,
                     abc.ABC): ...
