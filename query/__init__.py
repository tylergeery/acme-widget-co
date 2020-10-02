from typing import Generic, List, TypeVar


T = TypeVar('T')


class Queryable(Generic[T]):
    def __init__(self, items: List[T]):
        self.items = items or []

    @staticmethod
    def is_valid(item: T, **kwargs) -> bool:
            for prop, val in kwargs.items():
                if getattr(item, prop, None) != val:
                    return False

            return True

    def get(self, **kwargs):
        if not self.items:
            return None

        valid_items = self.all(**kwargs)
        if not valid_items:
            return None

        return valid_items[0]

    def all(self, **kwargs) -> List[T]:
        return [item for item in self.items if self.is_valid(item, **kwargs)]