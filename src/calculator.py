def add(a: int, b: int) -> int:
    # BUG: returns string instead of int
    return str(a + b)


def divide(a, b):
    # BUG: division by zero not handled
    return a / b
