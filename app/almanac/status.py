from .basic import book


@book.overwrite
class STATUS(book.Book, initializer=book.init_annotations):
    BUSY: book.Constant
    IDLE: book.Constant
    INITIALIZED: book.Constant
    PENDING: book.Constant
    STOPPED: book.Constant
