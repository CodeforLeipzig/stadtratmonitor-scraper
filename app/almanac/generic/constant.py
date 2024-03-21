class Constant:
    """Descriptor for strings that should act as a constant"""

    def __init__(self, value):
        self.__value = str(value)

    def __get__(self, *_):
        return self.__value

    def __set__(self, *_):
        return NotImplementedError('Try to overwrite a constant eh?')
