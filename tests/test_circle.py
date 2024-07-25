import unittest
from shapes.circle import Circle


class TestCircle(unittest.TestCase):
    def test_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483)


if __name__ == '__main__':
    unittest.main()
