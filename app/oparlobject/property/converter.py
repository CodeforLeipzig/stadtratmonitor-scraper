import datetime


def always_none(*_) -> None:
    return None


def to_object(item):
    return


def to_object_generator(item):
    objects = (to_object(sub) for sub in to_generator(item))
    yield from filter(lambda x: x is not None, objects)


def to_generator(items):
    if not items: return ()
    subs = (sub for sub in items)
    yield from filter(lambda x: x is not None, subs)


def to_datetime(item):
    return datetime.datetime.fromisoformat(item) if item else None


def to_date(item):
    return datetime.date.fromisoformat(item) if item else None


def to_str(item):
    return str(item) if item is not None else None


def to_bool(item):
    return bool(item) if item is not None else None


def to_int(item):
    return int(item) if item is not None else None

