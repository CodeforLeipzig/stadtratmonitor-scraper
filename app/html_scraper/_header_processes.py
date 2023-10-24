from ._sectionalize_html import Section
from typing import Generator


def ignore(_):
    # noinspection PyUnreachableCode
    if False:
        yield


def clean_outer_spaces(chunk: str) -> str:
    if chunk.startswith(' '):
        return clean_outer_spaces(chunk[1:])
    elif chunk.endswith(' '):
        return clean_outer_spaces(chunk[:-1])
    else:
        return chunk


def split_by_semicolon_or_comma(section: Section) -> Generator[Section, None, None]:
    chunk = section.content
    if ';' in chunk:
        contents = map(clean_outer_spaces, chunk.split(';'))
        yield from (Section(section.title, content) for content in contents)
    elif ',' in chunk and ' und ' not in chunk:
        contents = map(clean_outer_spaces, chunk.split(','))
        yield from (Section(section.title, content) for content in contents)
    else:
        yield section


def extract_from_parenthesis(section: Section) -> Generator[Section, None, None]:
    chunk = section.content
    if '(' in chunk and ')' in chunk:
        start, end = chunk.index('(') + 1, chunk.index(')')
        yield Section(section.title, chunk[start:end])
    else:
        yield section


def no_operation(section: Section) -> Generator[Section, None, None]:
    yield section


processes = {'Beteiligt': split_by_semicolon_or_comma,
             'Betreff': ignore,
             'Einreicher': split_by_semicolon_or_comma,
             'Federführend': split_by_semicolon_or_comma,
             'Status': extract_from_parenthesis,
             'Vorlageanlass': no_operation,
             'Vorlageart': no_operation}
