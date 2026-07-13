# Q14 Circle area and circumference - @JIYO P V 2026-07-13
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius * self.radius

    def get_circumference(self):
        return 2 * math.pi * self.radius


c = Circle(5)
print("Area:", c.get_area())
print("Circumference:", c.get_circumference())
