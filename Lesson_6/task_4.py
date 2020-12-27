"""Урок 6 Задание 4
Реализуйте базовый класс Car . У данного класса должны быть следующие атрибуты: speed ,
color , name , is_police (булево). А также методы: go , stop , turn(direction) , которые должны
сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
дочерних классов: TownCar , SportCar , WorkCar , PoliceCar . Добавьте в базовый класс метод
show_speed , который должен показывать текущую скорость автомобиля. Для классов
TownCar и WorkCar переопределите метод show_speed . При значении скорости свыше 60
( TownCar ) и 40 ( WorkCar ) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car():
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        show_speed = self.speed

    def go(self):
        return f'{self.name} go!'

    def stop(self):
        return f'{self.name} is stop!'

    def turn(self, direction):
        return f'{self.name} is turn to {direction}!'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'{self.name} have {self.speed}! is exceed the speed limit'
        else:
            return f'{self.name} goes with speed {self.speed}!'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'{self.name} have {self.speed}! is exceed the speed limit'
        else:
            return f'{self.name} goes with speed {self.speed}!'


TownCar_1 = TownCar(50, 'black', 'KIA')
TownCar_2 = TownCar(80, 'white', 'BMW')
SportCar = Car(160, 'red', 'Tesla')
WorkCar = WorkCar(80, 'different', 'VW')
PoliceCar = Car(100, 'special', 'Dodge', True)

print(TownCar_1.go(), TownCar_1.show_speed())
print(TownCar_2.go(), TownCar_2.show_speed())
print(PoliceCar.turn('left'))
print(PoliceCar.is_police)
print(WorkCar.stop())
