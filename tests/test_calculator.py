from src.calculator import add, divide
import pytest


def test_add():
    assert add(2, 3) == 5


def test_divide():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
