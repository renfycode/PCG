class MetaAttrSaver(type):
    def __new__(cls, name, bases, namespace):
        current_annotations = namespace.get('__annotations__', {})
        parents_attributes = {}

        for base in bases:
            if hasattr(base, '_parents_attributes'):
                parents_attributes.update(base._parents_attributes)
            if hasattr(base, '_current_attributes'):
                parents_attributes.update(base._current_attributes)
                
        namespace['_current_attributes'] = current_annotations
        namespace['_parents_attributes'] = parents_attributes
        
        return super().__new__(cls, name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        instance = super().__call__()
        
        for key, value in kwargs.items():
            if key in cls._current_attributes:
                setattr(instance, key, value)
            else:
                raise AttributeError(
                    f"'{key}' is not allowed. "
                    f"Class {cls.__name__} only accepts: {list(cls._current_attributes.keys())}"
                )
        
        return instance


class A(metaclass=MetaAttrSaver):
    name: str

class B(A):
    age: int

class C(B):
    score: float
