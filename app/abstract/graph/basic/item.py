import abc


class AbcItem(abc.ABC):
    """item is the base class for graph properties, nodes and relations"""
    @abc.abstractmethod
    def __eq__(self, other) -> bool:
        """a graph item is comparable"""

