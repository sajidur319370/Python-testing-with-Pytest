import pytest

import my_function


def test_add_string():
    result = my_function.add("Hello ", "World")
    assert result == "Hello World"


@pytest.mark.skip(reason="This feature is not needed to test")
def test_add():
    result = my_function.add(5, 7)
    assert result == 12
