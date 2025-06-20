import pytest
import shapes


@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(5, 6)


@pytest.fixture
def other_rectangle():
    return shapes.Rectangle(20, 30)


# Test my rectangle area
def test_area(my_rectangle):
    assert my_rectangle.area() == 5 * 6


# Test my rectangle perimeter
def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 2 * (5 + 6)


def test_not_equal(my_rectangle, other_rectangle):
    assert my_rectangle.area() != other_rectangle.area()
