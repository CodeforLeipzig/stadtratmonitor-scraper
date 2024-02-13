import abc


class AbcCypher(abc.ABC):
    def add_lines(self, *lines: str):
        """appends a string as newline to internal storage"""

    def build(self) -> tuple[str, dict]:
        """returns statement string and parameter dictionary"""

    def purge(self) -> tuple[str, dict]:
        """returns self.build and reinitialize self """

    def print(self):
        """prints statement string and parameter dictionary"""

    def print_merged(self):
        """prints parameters from dictionary merged into statement string"""
