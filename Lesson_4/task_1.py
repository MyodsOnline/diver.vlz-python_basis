"""урок 4 задание 1
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в
час) + премия. Для выполнения расчета для конкретных значений необходимо запускать
скрипт с параметрами.
"""
from sys import argv


def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f"Salary - {time * rate + bonus}")
    except ValueError:
        print("Enter all 3 numbers. Not string or empty character.")


salary()