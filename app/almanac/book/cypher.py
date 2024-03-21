from ..generic import Book, Constant, singleton


def init_annotations(cls: type, _):
    for key, type_ in cls.__annotations__.items():
        setattr(cls, key, type_(key.replace('_', ' ')))


@singleton
class COMMAND(Book, initializer=init_annotations):
    CALL: Constant
    CREATE: Constant
    DELETE: Constant
    LIMIT: Constant
    MATCH: Constant
    MERGE: Constant
    ON_CREATE_SET: Constant
    ON_MERGE_SET: Constant
    ORDER_BY: Constant
    RETURN: Constant
    SET: Constant
    WHERE: Constant
    YIELD: Constant
