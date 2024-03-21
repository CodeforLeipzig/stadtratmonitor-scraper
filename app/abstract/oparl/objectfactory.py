class ObjectFactory:
    def __call__(self, item):
        if isinstance(item, str):
            pass
        elif isinstance(item, dict):
            pass
        else:
            return None

