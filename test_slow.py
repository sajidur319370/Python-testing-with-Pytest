from time import sleep
import pytest
import my_function


def test_add():
    result = my_function.add(5, 7)
    assert result == 12


def test_add_string():
    result = my_function.add("Hello ", "World")
    assert result == "Hello World"


def test_divide():
    result = my_function.divide(10, 2)
    assert result == 5


def test_devide_by_zero():
    with pytest.raises(ValueError):
        result = my_function.divide(10, 0)
    assert True


def test_slowly():
    sleep(5)
    result = my_function.divide(100, 10)
    assert result == 10
