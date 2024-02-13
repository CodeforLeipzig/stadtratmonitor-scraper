import typing


class Initialized:
    def __init_subclass__(cls, initializer: typing.Optional[typing.Callable] = None, **kwargs):
        print('call Initializer')
        if initializer:
            initializer(cls)
        super().__init_subclass__(**kwargs)
