import abc

from ..abstract.labour import AbcMinion, AbcSupervisor

from .labour import BasicLabour, LabourStore


class BasicMinion(BasicLabour, AbcMinion, abc.ABC):
    supervisor: AbcSupervisor
    __supervisor_type: type[AbcSupervisor]

    def __init_subclass__(cls, **kwargs):
        if supervisor_type := cls.__annotations__.get('supervisor'):
            supervisor_type.register(cls)
            cls.__supervisor_type = supervisor_type

        super().__init_subclass__(**kwargs)

    def __init__(self):
        self.__supervisor = LabourStore[self.__annotations__.get('supervisor')]
        super().__init__()

    @property
    def supervisor(self) -> AbcSupervisor:
        return LabourStore[self.__supervisor_type]



