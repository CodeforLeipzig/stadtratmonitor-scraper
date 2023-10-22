from app.oparl.fakerequest import FakeHtmlRequest as request
from app.html_scraper._sectionalize_html import process_html_page
from app.html_scraper._header_processes import processes

if __name__ == '__main__':
    examples = ['https://ratsinformation.leipzig.de/allris_leipzig_public/vo020?VOLFDNR=2012504',
                'https://ratsinformation.leipzig.de/allris_leipzig_public/vo020?VOLFDNR=2012503',
                'https://ratsinformation.leipzig.de/allris_leipzig_public/vo020?VOLFDNR=2012502',
                'https://ratsinformation.leipzig.de/allris_leipzig_public/vo020?VOLFDNR=2012481',
                'https://ratsinformation.leipzig.de/allris_leipzig_public/vo020?VOLFDNR=2012457',
                'https://ratsinformation.leipzig.de/allris_leipzig_public/vo020?VOLFDNR=2012455']

    for e in examples:
        page = request.get(e)
        for section in process_html_page(page):
            process = processes.get(section.title)
            if process:
                [print(chunk) for chunk in process(section.content)]
            print(section)
