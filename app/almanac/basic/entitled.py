from .initilized import Initialized


class Entitled(Initialized):
    BADGE: str

    def __init_subclass__(cls, badge=None, work=lambda x: None, **kwargs):
        if badge:
            super().__init_subclass__(
                initializer=lambda c: setattr(c, 'BADGE', str(badge)), **kwargs
            )
        work(cls)

