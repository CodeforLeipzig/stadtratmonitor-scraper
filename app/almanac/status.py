from contextlib import contextmanager

from .book.status import STATUS


class Status:
    def __init__(self):
        self.__status = STATUS.INITIALIZED

    def __enter__(self):
        self.__status = STATUS.IDLE
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__status = STATUS.STOPPED

    def __eq__(self, other):
        return self.__status == (other.__status if type(other) is Status else other)

    def get(self) -> str:
        return self.__status

    def is_idle(self):
        return self.__status == STATUS.IDLE

    def is_busy(self):
        return self.__status == STATUS.BUSY

    def is_initialized(self):
        return self.__status == STATUS.INITIALIZED

    def is_stopped(self):
        return self.__status == STATUS.STOPPED

    @contextmanager
    def idle_and_stopped_cnx(self):
        self.__status = STATUS.IDLE
        yield
        self.__status = STATUS.STOPPED

    @contextmanager
    def busy_and_idle_cnx(self):
        self.__status = STATUS.BUSY
        yield
        self.__status = STATUS.IDLE
