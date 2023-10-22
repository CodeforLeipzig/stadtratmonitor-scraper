def ignore(_):
    # noinspection PyUnreachableCode
    if False:
        yield


def clean_outer_spaces(chunk: str):
    if chunk.startswith(' '):
        return clean_outer_spaces(chunk[1:])
    elif chunk.endswith(' '):
        return clean_outer_spaces(chunk[:-1])
    else:
        return chunk


def split_by_semicolon_or_comma(chunk: str):
    if ';' in chunk:
        for chunk in map(clean_outer_spaces, chunk.split(';')):
            yield chunk
    elif ',' in chunk and 'und' not in chunk:
        for chunk in map(clean_outer_spaces, chunk.split(',')):
            yield chunk
    else:
        yield chunk


def extract_from_parenthesis(chunk: str):
    if '(' in chunk and ')' in chunk:
        start, end = chunk.index('(') + 1, chunk.index(')')
        yield chunk[start:end]
    else:
        yield chunk


def no_operation(chunk: str):
    yield chunk


pipelines = {'Beteiligt': split_by_semicolon_or_comma,
             'Betreff': ignore,
             'Einreicher': split_by_semicolon_or_comma,
             'Federführend': no_operation,
             'Status': extract_from_parenthesis,
             'Vorlageanlass': no_operation,
             'Vorlageart': no_operation}