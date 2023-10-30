from app.oparl import Oparl
from app.oparl.fakerequest import FakeHtmlRequest as request
from app.html_scraper._sectionalize_html import HtmlSections

MARKER = '#' * 20
FILEPATH = './log_sections.txt'


def save(*strings):
    with open(FILEPATH, 'a', encoding='utf-8') as file:
        for string in strings:
            file.write(f'{string}\n')


def print_(*strings):
    for string in strings:
        print(f'{string}')


if __name__ == '__main__':
    '''examples = ['https://ratsinformation.leipzig.de/allris_leipzig_public/vo020?VOLFDNR=2012504',
                'https://ratsinformation.leipzig.de/allris_leipzig_public/vo020?VOLFDNR=2012503',
                'https://ratsinformation.leipzig.de/allris_leipzig_public/vo020?VOLFDNR=2012502',
                'https://ratsinformation.leipzig.de/allris_leipzig_public/vo020?VOLFDNR=2012481',
                'https://ratsinformation.leipzig.de/allris_leipzig_public/vo020?VOLFDNR=2012457',
                'https://ratsinformation.leipzig.de/allris_leipzig_public/vo020?VOLFDNR=2012455']'''

    for paper in Oparl.pagination():
        url = paper.web_url
        page_content = request.get(url)
        to_save = [MARKER, url, '\n']

        if page_content:
            html_sections = HtmlSections(page_content)

            before = ''
            for header in html_sections.headers():
                title = header.title
                not_same_section = title != before
                if not_same_section: to_save.append(MARKER)
                to_save.append(f'{title}: {header.content}')
                if not_same_section: to_save.append('')
                before = title

            for docpart in html_sections.docparts():
                to_save.extend((MARKER, docpart.title, '', docpart.content, ''))

        # print(url)
        # save(*to_save, '', '')
        print_(*to_save, '', '')
