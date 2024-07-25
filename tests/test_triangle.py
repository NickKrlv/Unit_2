import unittest
from shapes.triangle import Triangle


class TestTriangle(unittest.TestCase):
    def test_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.area(), 6)

    def test_is_right_angled(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angled())

        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right_angled())


if __name__ == '__main__':
    unittest.main()
