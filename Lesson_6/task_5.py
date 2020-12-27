"""Урок 6 Задание 5
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
(название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
реализовать переопределение метода draw . Для каждого из классов метод должен выводить
уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра.
"""


class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Start drawing'


class Pen(Stationery):
    def draw(self):
        return f'{self.title} start drawing'


class Pencil(Stationery):
    def draw(self):
        return f'{self.title} start drawing'


class Handle(Stationery):
    def draw(self):
        return f'{self.title} start drawing'


pen = Pen('Pen')
print(pen.draw())
pencil = Pencil('Pencil')
print(pencil.draw())
handle = Handle('Handle')
print(handle.draw())
