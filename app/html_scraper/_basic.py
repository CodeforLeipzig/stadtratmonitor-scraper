from typing import NamedTuple, Iterable
import re


class Section(NamedTuple):
    title: str
    content: str


FILTERS = ('\s', '\n', '\r', '\t', '\xa0')


def remove_symbols(chunks: Iterable[str], *filters: str) -> str:
    regex = f'[^{"".join(filters)}]+'
    survivors = []
    for chunk in chunks:
        survivors.extend(re.findall(regex, chunk))
    return ' '.join(survivors)
