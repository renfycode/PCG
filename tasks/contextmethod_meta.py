from functools import wraps
import inspect

frame = inspect.currentframe()

def contextmanager(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        frame = inspect.currentframe()
        try:
            while frame:
                if frame.f_code.co_name == '__enter__':
                    return func(*args, **kwargs)
                frame.f_back
        finally:
            del frame
        raise NotImplementedError
    return wrapper


class MyClassWith:
    def __init__(self):
        self.example = 1
    
    def __enter__(self):
        print("enter")

    def __exit__(self, exc_type, exc_value, traceback):
        print("exit")

    def __call__(self, *args, **kwargs):
        print("call")

    @contextmanager
    def my_func(self):
        pass


example = MyClassWith()

with example.my_func():
    pass
