from .basic import book


def init_annotations(cls: type, _):
    for key, type_ in cls.__annotations__.items():
        setattr(cls, key, type_(key.replace('_', ' ')))


@book.overwrite
class COMMAND(book.Book, initializer=init_annotations):
    CALL: book.Constant
    CREATE: book.Constant
    DELETE: book.Constant
    LIMIT: book.Constant
    MATCH: book.Constant
    MERGE: book.Constant
    ON_CREATE_SET: book.Constant
    ON_MERGE_SET: book.Constant
    ORDER_BY: book.Constant
    RETURN: book.Constant
    SET: book.Constant
    WHERE: book.Constant
    YIELD: book.Constant
