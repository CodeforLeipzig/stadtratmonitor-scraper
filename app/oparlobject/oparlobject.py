import inspect

from app.abstract.oparl import AbcOparlObject, AbcOparlProperty
from app.oparlobject.propertystore import PropertyStore


class OparlObject(AbcOparlObject):
    def __init__(self, content: dict):
        self.__content = content

    def __init_subclass__(cls, factory=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if not factory: return

        factory.register(cls.BADGE, cls)
        parents = filter(lambda x: issubclass(x, AbcOparlObject), cls.mro())
        for parent in parents:
            keys = filter(lambda x: x.isupper(), inspect.get_annotations(parent))
            for key in keys:
                if isinstance(getattr(cls, key, None), AbcOparlProperty) or \
                        not (property_key := getattr(PropertyStore, key, None)): continue
                setattr(cls, key, property_key)

    @property
    def content(self) -> dict:
        return self.__content

    async def resolve(self):
        pass

    def is_resolvable(self) -> bool:
        url = self.ID
        return isinstance(url, str) and url.startswith('http')

    def is_valid(self) -> bool:
        return self.ID and self.TYPE and self.CREATED and self.MODIFIED and self.DELETED is not None

    def is_deleted(self) -> bool:
        deleted = self.DELETED
        return deleted or deleted is None
