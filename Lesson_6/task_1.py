"""Урок 6 Задание 1
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
— на ваше усмотрение. Переключение между режимами должно осуществляться только в
указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""
from time import sleep
from itertools import cycle


# easy way
class TrafficLight():
    def __init__(self, color):
        self.color = color

    def switch(self):  # advanced way
        for i in cycle(self.color):
            print(i)
            sleep(2)

    def click(self):  # easy way
        while True:
            print('red')
            sleep(7)
            print('yellow')
            sleep(2)
            print('green')
            sleep(7)
            print('yellow')
            sleep(2)


tl = TrafficLight(['red', 'yellow', 'green', 'yellow'])
tl.switch()

# cool way
import time
import itertools


class TrafficLight:
    __color = [["red", [7, 31]], ["yellow", [2, 33]], ["green", [7, 32]], ["yellow", [2, 33]]]

    def running(self):
        for light in itertools.cycle(self.__color):
            print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")
            time.sleep(light[1][0])


trafficlight_1 = TrafficLight()
trafficlight_1.running()
