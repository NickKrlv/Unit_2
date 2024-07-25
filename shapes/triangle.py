from .shape import Shape
import math


class Triangle(Shape):
    """ Triangle class. """

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angled(self):
        sides = [self.a, self.b, self.c]
        sides.sort()
        return round(sides[0] ** 2 + sides[1] ** 2, 5) == round(sides[2] ** 2, 5)
