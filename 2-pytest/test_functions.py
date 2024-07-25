# pip install pytest  # noqa
from functions import add


def test_add():
    assert add(10, 2) == 12
    assert add(4, 2) == 6
    assert add(4, 2) != 8


def test_add_2():
    assert add(10, 2) == 13
