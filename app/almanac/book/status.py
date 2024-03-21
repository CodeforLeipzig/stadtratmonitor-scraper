from ..generic import Book, Constant, singleton, init_annotations


@singleton
class STATUS(Book, initializer=init_annotations):
    BUSY: Constant
    IDLE: Constant
    INITIALIZED: Constant
    PENDING: Constant
    STOPPED: Constant
