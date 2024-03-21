from .initialisable import Initialisable
from .constant import Constant


class Entitlable(Initialisable):
    BADGE = None

    def __init_subclass__(cls, badge=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if badge:
            setattr(cls, 'BADGE', Constant(badge))
