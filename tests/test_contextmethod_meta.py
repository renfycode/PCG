import pytest
from tasks.contextmethod_meta import MyOwnDBQueryBuilder


def test_contextmethod_meta():
    with pytest.raises(Exception) as excinfo:
        MyOwnDBQueryBuilder("test").execute_query_very_safety("test")
    assert "Метод требует контекста" in str(excinfo.value)


def test_contextmethod():
    with MyOwnDBQueryBuilder("localhost:5432").context as db:
        db.execute_query_very_safety("test")
