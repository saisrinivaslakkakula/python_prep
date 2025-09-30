import pytest

from exercise_2.src.Calculator import Calculator


def test_calculator_add_throws_RTE_when_Invalid_input_passed():
    calc = Calculator("5", 6)
    with pytest.raises(RuntimeError) as exec:
        calc.add()
    assert str(exec.value) == "Invalid Input, numbers must be integers"


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (45, 45, 90),
    (23, 32, 55)
])
def test_calculator_add_happy_case(a, b, expected):
    calc = Calculator(a, b)
    assert calc.add() == expected, f"addition of {a}, {b} resulted {expected}"

def test_calculator_subtract_throws_RTE_when_Invalid_input_passed():
    calc = Calculator("5", 6)
    with pytest.raises(RuntimeError) as exec:
        calc.subtract()
    assert str(exec.value) == "Invalid Input, numbers must be integers"


@pytest.mark.parametrize("a, b, expected", [
    (5, 2, 3),
    (45, 45, 0),
    (23, 32, -9)
])
def test_calculator_subtract_happy_case(a, b, expected):
    calc = Calculator(a, b)
    assert calc.subtract() == expected, f"subtraction of {a}, {b} resulted {expected}"


def test_calculator_multiply_throws_RTE_when_Invalid_input_passed():
    calc = Calculator("5", 6)
    with pytest.raises(RuntimeError) as exec:
        calc.multiply_whole_nums()
    assert str(exec.value) == "Invalid Input, numbers must be integers"

def test_calculator_multiply_throws_RTE_when_negative_input_passed():
    calc = Calculator(-8, -7)
    with pytest.raises(RuntimeError) as exec:
        calc.multiply_whole_nums()
    assert str(exec.value) == "Only positive integers are allowed for multiplication"


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 2),
    (25, 25, 625),
    (15, 6, 90)
])
def test_calculator_multiply_happy_case(a, b, expected):
    calc = Calculator(a, b)
    assert calc.multiply_whole_nums() == expected, f"multiplication of {a}, {b} resulted {expected}"


def test_calculator_divide_throws_RTE_when_Invalid_input_passed():
    calc = Calculator("5", 6)
    with pytest.raises(RuntimeError) as exec:
        calc.divide()
    assert str(exec.value) == "Invalid Input, numbers must be integers"

def test_calculator_divide_throws_RTE_when_zero_input_passed():
    calc = Calculator(-8, 0)
    with pytest.raises(ZeroDivisionError) as exec:
        calc.divide()
    assert str(exec.value) == "Divisor cannot be zero"


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 0.5),
    (25, 25, 1.0),
    (15, 6, 2.5)
])
def test_calculator_divide_happy_case(a, b, expected):
    calc = Calculator(a, b)
    assert calc.divide() == expected, f"division of {a}, {b} resulted {expected}"