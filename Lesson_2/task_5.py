"""Урок 2 Задание 5
Реализовать структуру « Рейтинг » , представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же
значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3 , 2.
Пользователь ввел число 8. Результат: 8 , 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1 .
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3,3, 2].
"""

# main way
my_list = [7, 5, 3, 3, 2]
new_el = float(input('Enter your num: '))
cnt = 0
for el in my_list:
    if el >= new_el:
        cnt += 1
my_list.insert(cnt, new_el)
print(my_list)

# another, short way
my_list = [7, 5, 3, 3, 2]
my_list.append(float(input('Enter your num: ')))
new_list = sorted(my_list, reverse=True)
print(new_list)

# another, long way
my_list = [7, 5, 3, 3, 2]
while True:
    n = input('Enter new element, or press "q" for exit: ')
    if n.lower() != 'q':
        if n.isdigit():
            n = float(n)
            cnt = 0
            for el in my_list:
                if el >= n:
                    cnt += 1
            my_list.insert(cnt, n)
            print(f"New element added. Now we have - {my_list}")
        else:
            print(f"'{n}' - Is not a digit. Our list still - {my_list}")
    else:
        print(f'We finished. Final list is - {my_list}')
        break
