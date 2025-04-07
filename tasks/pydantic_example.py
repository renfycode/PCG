class MetaAttrSaver(type):
    def __new__(cls, name, bases, namespace):
        current_annotations = namespace.get('__annotations__', {})
        __fields__ = {}

        for base in bases:
            if hasattr(base, '__fields__'):
                __fields__.update(base.__fields__)
        __fields__.update(current_annotations)
        namespace['__fields__'] = __fields__
        
        return super().__new__(cls, name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        instance = super().__call__()
        
        for key, value in kwargs.items():
            if key in cls.__fields__:
                setattr(instance, key, value)
            else:
                raise AttributeError(
                    f"'{key}' is not allowed. "
                    f"Class {cls.__name__} only accepts: {list(cls.__fields__.keys())}"
                )
        
        return instance


class A(metaclass=MetaAttrSaver):
    name: str

class B(A):
    age: int

class C(B):
    score: float
