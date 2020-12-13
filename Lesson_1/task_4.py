"""урок 1 задание 4
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

user_num = int(input('Enter your num: '))
max_digit = 0  # переменная для хранения наибольшего значения
cur_digit = 0  # переменная для хранения текущей цифры
cur_num = user_num  # сохраним исходное число
if cur_num < 10:
    max_digit = cur_num
while cur_num > 0:
    cur_digit = cur_num % 10
    cur_num = cur_num // 10
    if cur_digit > max_digit:
        max_digit = cur_digit
print(max_digit)
