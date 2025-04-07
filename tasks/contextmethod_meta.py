from contextlib import contextmanager
from functools import wraps


class ContextMethodMeta(type):
    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        instance._context = False

        @contextmanager
        def _context():
            instance._context = True
            try:
                yield instance
            finally:
                instance._context = False

        instance.context = _context()
        return instance

def contextmethod(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not getattr(self, '_context', False):
            raise Exception("Метод требует контекста")
        return func

    return wrapper


class MyOwnDBQueryBuilder(metaclass=ContextMethodMeta):
    def __init__(self, url: str) -> None:
        self.url = url

    @contextmethod
    def execute_query_very_safety(self, query) -> str:
        print(f"Выполнение запроса: {query} в БД {self.url}")
