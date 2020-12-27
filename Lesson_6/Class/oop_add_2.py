"""Задача 2
Реализуйте методы класса.
"""


class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return f'Площадь цидиндра: {2 * self.pi * self.radius * self.height + 2 * self.pi * self.radius ** 2}'

    def surface_area(self):
        return f'Объём цидиндра: {self.pi * self.radius ** 2 * self.height}'


cylinder = Cylinder(2, 3)
print(cylinder.volume())
print(cylinder.surface_area())
