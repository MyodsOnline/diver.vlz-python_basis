"""Урок 6 Задание 3
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name ,
surname , position (должность), income (доход). Последний атрибут должен быть
защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker .
В классе Position реализовать методы получения полного имени сотрудника ( get_full_name ) и
дохода с учетом премии ( get_total_income ). Проверить работу примера на реальных данных
(создать экземпляры класса Position , передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
"""
class Worker():
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        return f'Name - {self.name}, Surname - {self.surname}'
    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")

new_worker = Position('Andrei', 'Bitutskii', 'dinf', {"wage": 100000, "bonus": 20000})
print(new_worker.get_full_name())
print(new_worker.get_total_income())