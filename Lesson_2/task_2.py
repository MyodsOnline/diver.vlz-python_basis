"""Урок 2 Задание 2
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
сохранить на своем месте. Для заполнения списка элементов необходимо использовать
функцию input()
"""
my_str = input("Enter the list's elements (with spaces): ").split()
print(f'Original list - {my_str}')
for el in range(1, len(my_str), 2):
    my_str[el - 1], my_str[el] = my_str[el], my_str[el - 1]
print(f'New list - {my_str}')
