import re
import lxml.html
from typing import NamedTuple, Iterable, Generator

FILTERS = ('\s', '\n', '\r', '\t', '\xa0')
HEADLINES = ('Sachverhalt', 'Beschlussvorschlag', 'Begründung des Antrags')


class Section(NamedTuple):
    title: str
    content: str


class WipSection:
    def __init__(self, title=None, content=None):
        self.title: list = [title] if title else []
        self.content: list = [content] if content else []

    def finalize(self):
        if not self.title and self.content:
            self.title.append(HEADLINES[0])
        return Section(' '.join(self.title), ' '.join(self.content))

    def not_empty(self):
        return self.title or self.content


def process_html_page(page_content: bytes) -> list[Section]:
    tree = lxml.html.fromstring(page_content)
    headers = (section for section in process_header(tree))
    docparts = (section for section in process_docpart(tree))
    return [*headers, *docparts]


def remove_symbols(chunks: Iterable[str], *filters: str) -> str:
    regex = f'[^{"".join(filters)}]+'
    survivors = []
    for chunk in chunks:
        survivors.extend(re.findall(regex, chunk))
    return ' '.join(survivors)


def process_header(tree) -> Generator[Section]:
    for row in tree.xpath('.//div[@id="headLeft"]//div[@class="row"]'):
        title = remove_symbols(row.xpath('.//dt//text()'), *FILTERS, ':', '\d')
        content = remove_symbols(row.xpath('.//dd//text()'), *FILTERS)
        yield Section(title, content)


def process_docpart(tree) -> Generator[Section]:
    current_section = WipSection()

    for line in process_docpart_lines(tree):
        if line in HEADLINES:
            if current_section.not_empty():
                yield current_section.finalize()
            current_section = WipSection(line)
        else:
            current_section.content.append(line)

    if current_section.not_empty():
        yield current_section.finalize()


def process_docpart_lines(tree) -> str:
    for doc_part in tree.xpath('.//div[@class="docPart"]'):
        headline = doc_part.getparent().xpath('.//*[@class="expandedTitle"]/text()')
        headline = remove_symbols(headline, *FILTERS)
        if headline: yield headline

        for line in doc_part.xpath('.//*//text()'):
            line = remove_symbols((line,), *FILTERS)
            if line: yield line
