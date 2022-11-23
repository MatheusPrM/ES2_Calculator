import calculator

def test_add():
    assert calculator.add(1, 2) == 3


def test_subtract():
    assert calculator.subtract(1, 2) == -1


def test_multiply():
    assert calculator.multiply(1, 2) == 2


def test_divide():
    assert calculator.divide(1, 2) == 0.5


def test_add_then_subtract():
    assert calculator.subtract(calculator.add(1, 2), 3) == 0


def test_multiply_then_divide():
    assert calculator.divide(calculator.multiply(1, 2), 3) == 0.6666666666666666