from tasks.singltone import MyClass

def test_singltone():
    class_example_first = MyClass(value=1)
    class_example_second = MyClass(value=2)

    assert class_example_first.value == 1
    assert class_example_second.value == 1
    assert class_example_second is class_example_first
