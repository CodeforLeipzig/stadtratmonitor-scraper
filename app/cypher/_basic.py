from . import abstract


def extract(cls, *args):
    for arg in args:
        if isinstance(arg, cls):
            yield arg
        else:
            for sub_arg in extract(cls, *arg):
                yield sub_arg


def tag_generator():
    for prev in (prev for sub in (('',), tag_generator()) for prev in sub):
        for i in range(97, 123):
            yield f'{prev}{chr(i)}'


class CypherBase(abstract.CypherABC):
    def __init__(self):
        self._current_line = []
        self._lines = []
        self._parameters = {}
        self._tag_generator = tag_generator()

    def _newline(self, chunk):
        self._current_line = [chunk]
        self._lines.append(self._current_line)

    def _stage(self, chunk):
        self._current_line.append(chunk)

    def build(self) -> tuple[str, dict]:
        lines = '\n'.join((' '.join(line) for line in self._lines))
        parameter = self._parameters
        return lines, parameter

    def purge(self) -> tuple[str, dict]:
        lines, parameter = self.build()
        self._parameters, self._lines, self._current_line = {}, [], []
        return lines, parameter

    def print(self):
        statement, parameter = self.build()
        print(statement)
        [print(f'key: {key}, value:{value}') for key, value in parameter.items()]

    def print_merged(self):
        statement, parameter = self.build()
        merged = str()
        for key, value in parameter.items():
            statement = statement.replace(f'${key}', str(value))
        print(statement)
