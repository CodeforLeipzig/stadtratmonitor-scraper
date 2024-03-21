import datetime
import typing

from ...abstract.oparl.oparlobject import AbcOparlObject
from ...almanac import singleton


@singleton
class Connector:
    __slots__ = ('oparl_factory', )

    def __init__(self):
        self.oparl_factory: typing.Optional[typing.Callable] = None


def always_none(*_) -> None:
    return None


def to_object_generator(item) -> typing.Iterable[AbcOparlObject]:
    objects = (Connector.oparl_factory(sub) for sub in to_generator(item))
    yield from filter(lambda x: x is not None, objects)


def to_generator(items) -> typing.Iterable:
    if not items: return ()
    subs = (sub for sub in items)
    yield from filter(lambda x: x is not None, subs)


def to_datetime(item) -> datetime.datetime:
    return datetime.datetime.fromisoformat(item) if item else None


def to_date(item) -> datetime.date:
    return datetime.date.fromisoformat(item) if item else None


def to_str(item) -> str:
    return str(item) if item is not None else None


def to_bool(item) -> bool:
    return bool(item) if item is not None else None


def to_int(item) -> int:
    return int(item) if item is not None else None

