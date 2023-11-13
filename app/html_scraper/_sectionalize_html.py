import lxml.html
from typing import Generator
from ._known_headlines import HEADERS, HEADLINES
from ._basic import Section, remove_symbols, FILTERS


class WipSection:
    def __init__(self, title=None, content=None):
        self.title: list = [title] if title else []
        self.content: list = [content] if content else []

    def finalize(self) -> Section:
        if not self.title and self.content:
            self.title.append(HEADLINES.default.name)
        return Section(' '.join(self.title), ' '.join(self.content))

    def not_empty(self):
        return self.title or self.content


class HtmlSections:
    def __init__(self, page: bytes):
        self.tree = lxml.html.fromstring(page)

    def headers(self) -> Generator[Section, None, None]:
        for header in self._extract_header():
            yield from HEADERS(header)

    def docparts(self) -> Generator[Section, None, None]:
        for docpart in self._extract_docpart():
            yield from HEADLINES(docpart)

    def _extract_header(self) -> Generator[Section, None, None]:
        for row in self.tree.xpath('.//div[@id="headLeft"]//div[@class="row"]'):
            title = remove_symbols(row.xpath('.//dt//text()'), *FILTERS, ':', '\d')
            content = remove_symbols(row.xpath('.//dd//text()'), *FILTERS)
            yield Section(title, content)

    def _extract_docpart(self) -> Generator[Section, None, None]:
        current_section = WipSection()

        for line in self._process_docpart_lines():
            if line in HEADLINES.names():
                if current_section.not_empty():
                    yield current_section.finalize()
                current_section = WipSection(line)
            else:
                current_section.content.append(line)

        if current_section.not_empty():
            yield current_section.finalize()

    def _process_docpart_lines(self) -> str:
        for doc_part in self.tree.xpath('.//div[@class="docPart"]'):
            headline = doc_part.getparent().xpath('.//*[@class="expandedTitle"]/text()')
            headline = remove_symbols(headline, *FILTERS)
            if headline: yield headline

            for line in doc_part.xpath('.//*//text()'):
                line = remove_symbols((line,), *FILTERS)
                if line: yield line
