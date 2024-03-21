import typing


class Initialisable:
    def __init_subclass__(cls, initializer: typing.Optional[typing.Callable] = None, **kwargs):
        if initializer:
            initializer(cls)
        super().__init_subclass__(**kwargs)
