from ._sectionalize_html import Section

HEADER_TITLES = ('Beteiligt', 'Betreff', 'Einreicher', 'Federführend', 'Status', 'Vorlageanlass', 'Vorlageart')


# Beteiligt
def involved(section: Section):
    # check for semicolons, commas
    # split if necessary
    pass


# Betreff
def subject(section: Section):
    # ignore
    pass


# Einreicher
def submitter(section: Section):
    # check for semicolons, commas
    # split if necessary
    pass


# Federführend
def leading(section: Section):
    # check for semicolons, commas
    # split if necessary
    pass


# Status
def status(section: Section):
    # extract chunk in parentheses
    pass


# Vorlageanlass
def submission_occasion(section: Section):
    # return content
    pass


# Vorlageart
def submission_type(section: Section):
    # return content
    pass
