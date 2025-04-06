import pytest
from tasks.pydantic_example import A, B, C

def test_parent_class_attributes():
    assert A._current_attributes == {'name': str}
    assert A._parents_attributes == {}

def test_child_class_attributes():
    assert B._current_attributes == {'age': int}
    assert B._parents_attributes == {'name': str}

def test_grandchild_class_attributes():
    assert C._current_attributes == {'score': float}
    assert C._parents_attributes == {'name': str, 'age': int}

def test_parent_instance_creation():
    a = A(name="Gleb")
    assert a.name == "Gleb"
    assert a.__dict__ == {'name': 'Gleb'} # Содержит только свои атрибуты, больше никаких в __dict__

def test_child_instance_creation():
    b = B(age=25)
    assert b.age == 25
    assert b.__dict__ == {'age': 25} # Содержит только свои атрибуты, больше никаких в __dict__

def test_grandchild_instance_creation():
    c = C(score=90.5)
    assert c.score == 90.5
    assert c.__dict__ == {'score': 90.5} # Содержит только свои атрибуты, больше никаких в __dict__

def test_parent_attr_in_child_raises_error():
    with pytest.raises(AttributeError) as excinfo:
        B(name="Bob", age=30)
    assert "'name' is not allowed" in str(excinfo.value)
    assert "only accepts: ['age']" in str(excinfo.value)

def test_parent_and_grandparent_attrs_in_grandchild_raises_errors():
    with pytest.raises(AttributeError) as excinfo:
        C(name="Charlie", score=80)
    assert "'name' is not allowed" in str(excinfo.value)
    
    with pytest.raises(AttributeError) as excinfo:
        C(age=20, score=80)
    assert "'age' is not allowed" in str(excinfo.value)

def test_invalid_attribute_raises_error():
    with pytest.raises(AttributeError) as excinfo:
        A(invalid_attr="test")
    assert "'invalid_attr' is not allowed" in str(excinfo.value)
    assert "only accepts: ['name']" in str(excinfo.value)
