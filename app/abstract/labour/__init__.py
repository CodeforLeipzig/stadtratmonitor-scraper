import abc

from .labour import AbcLabour
from .mill import AbcMill
from .minion import AbcMinion
from .supervisor import AbcSupervisor


class AbcMediator(AbcSupervisor, AbcMinion, abc.ABC): ...


class AbcMultiMill(AbcMediator, AbcMill, abc.ABC): ...
