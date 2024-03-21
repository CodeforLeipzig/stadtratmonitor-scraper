from .book.status import STATUS


class Status:
    def __init__(self):
        self.__status = STATUS.INITIALIZED

    def __call__(self, *args, **kwargs):
        return self.__status

    def __enter__(self):
        self.__status = STATUS.IDLE
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__status = STATUS.STOPPED

    def __eq__(self, other):
        return self.__status == (other.__status if type(other) is Status else other)

    def set_idle(self):
        self.__status = STATUS.IDLE

    def set_busy(self):
        self.__status = STATUS.BUSY

    def is_idle(self):
        return self.__status == STATUS.IDLE

    def is_busy(self):
        return self.__status == STATUS.BUSY
