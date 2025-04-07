import pytest
from tasks.pydantic_example import A, B, C

def test_parent_class_attributes():
    assert A.__fields__ == {'name': str}

def test_child_class_attributes():
    assert B.__fields__ == {'age': int, 'name': str}

def test_grandchild_class_attributes():
    assert C.__fields__ == {'score': float, 'age': int, 'name': str}

def test_parent_instance_creation():
    a = A(name="Gleb")
    assert a.name == "Gleb"
    assert a.__dict__ == {'name': 'Gleb'}

def test_child_instance_creation():
    b = B(age=25)
    assert b.age == 25
    assert b.__dict__ == {'age': 25}

def test_grandchild_instance_creation():
    c = C(score=90.5)
    assert c.score == 90.5
    assert c.__dict__ == {'score': 90.5}

def test_invalid_attribute_raises_error():
    with pytest.raises(AttributeError) as excinfo:
        A(invalid_attr="test")
    assert "'invalid_attr' is not allowed" in str(excinfo.value)
    assert "only accepts: ['name']" in str(excinfo.value)
