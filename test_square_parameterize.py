import shapes
import pytest


@pytest.mark.parametrize("side_length,  expected_area", [(5, 25), (4, 16), (7, 49)])
def test_multiple_square_area(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize(
    "side_length,  expected_perimeter", [(5, 20), (4, 16), (7, 28)]
)
def test_multiple_square_perimeter(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter
