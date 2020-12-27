"""Задача 1
Реализуйте методы класса Line (линия), который принимает на вход координаты в виде двух кортежей,
и возвращает угол наклона (slope) и длину (distance) этой линии.
"""


class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1 = self.coor1[0]
        y1 = self.coor1[1]
        x2 = self.coor2[0]
        y2 = self.coor2[1]
        return f'Длина вектора: {round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 3)}'

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return f'Угол наклона вектора: {round((y2 - y1) / (x2 - x1), 3)}'


li = Line((3, 2), (8, 10))
print(li.slope())
print(li.distance())
