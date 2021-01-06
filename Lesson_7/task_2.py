"""Урок 7 Задание 2
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда , которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм . У этих типов одежды существуют
параметры: размер (для пальто ) и рост (для костюма ). Это могут быть обычные числа: V и
H , соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5) , для костюма (2*H + 0.3) . Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property .
"""

from abc import ABC, abstractmethod

class Outfit(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption

class Coat(Outfit):
    @property
    def consumption(self):
        print(f'Coat.consumption - {round(self.value / 6.5 + 0.5, 2)}')
        return round(self.value / 6.5 + 0.5, 2)

class Suit(Outfit):
    @property
    def consumption(self):
        print(f'Coat.consumption - {round(self.value * 2 + 0.3, 2)}')
        return round(self.value * 2 + 0.3, 2)

a = Coat(int(input('Coat size - ')))
b = Suit(int(input('Suit heigth - ')))

print(a + b)



# with setter method
class Сlothes(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def raschet(self):
        pass

    def __add__(self, other):
        return self.raschet + other.raschet


class Coat(Сlothes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            print('Min size - 40')
            self.__size = 40
        elif size > 60:
            print('Max size - 60')
            self.__size = 60
        else:
            self.__size = size

    @property
    def raschet(self):
        return self.__size / 6.5 + 0.5


class Сostume(Сlothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 100:
            print('Min height - 100')
            self.__height = 150
        elif height > 240:
            print('Maz height - 240')
            self.__height = 240
        else:
            self.__height = height

    @property
    def raschet(self):
        return 2 * (self.__height / 100) + 0.3


coat_1 = Coat(int(input('Enter coat size - ')))
print(f'You need - {coat_1.raschet:.2f}')
costume_1 = Сostume(int(input('Enter suit size - ')))
print(f'You need - {costume_1.raschet:.2f}')
print(f'Total consumption - {coat_1 + costume_1:.2f}')