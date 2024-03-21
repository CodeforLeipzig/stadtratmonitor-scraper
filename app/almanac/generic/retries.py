class Retries:
    def __init__(self, n: int, *ignores):
        self.__n = n
        self.__ignores = ignores

    def __enter__(self):
        if self.__n: return True
        else: return False

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type and exc_type not in self.__ignores:
            raise exc_type(exc_val, exc_tb)
        self.__n = max(0, self.__n-1)
