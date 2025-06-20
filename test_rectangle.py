# Class Test
import shapes


# Class Test
class TestRectangle:
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.rectangle = shapes.Rectangle(10, 20)

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.rectangle

    def test_area(self):
        original = self.rectangle.area()
        expected = self.rectangle.length * self.rectangle.width
        assert original == expected

    def test_perimeter(self):
        original = self.rectangle.perimeter()
        expected = 2 * (self.rectangle.length + self.rectangle.width)
        assert original == expected
