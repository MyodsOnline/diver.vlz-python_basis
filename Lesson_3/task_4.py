"""урок 3 задание 4
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора.
Второй — более сложная реализация без оператора, предусматривающая использование цикла.
"""

# strange way
x = int(input('Enter x: '))
y = int(input('Enter y: '))
while x <= 0:
    x = int(input('Enter x: '))
while y >= 0:
    y = int(input('Enter y: '))
print(f'x = {x}, y = {y}')


def my_func(x, y):
    return round((x ** y), 3)


print(my_func(x, y))

# main way
def my_func(x, y):
    try:
        x, y = int(x), int(y)
        if x > 0 and y < 0:
            return round((x ** y), 3)
        else:
            return 'Data error!'
    except ValueError:
        print('Wrong data!')


print(my_func(input('Enter x: '), input('Enter y: ')))


# anoter way, with cycle
def my_func(x, y):
    try:
        x, y = int(x), int(y)
        if x < 0 or y > 0:
            return 'Data error!'
        else:
            result = 1
            for _ in range(abs(y)):
                result /= x
            return round(result, 3)
    except ValueError:
        return 'Data error'


print(my_func(input('Enter a real positive x: '), input('Enter a negative y: ')))