from src.validator import is_positive


def test_positive():
    assert is_positive(10) is True


def test_negative():
    assert is_positive(-5) is False
