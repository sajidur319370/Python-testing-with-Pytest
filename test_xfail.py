import pytest

import my_function


@pytest.mark.xfail(reason="We know We cannot add string with number")
def test_add_string_to_number():
    my_function.add("Hello ", 5)
   
