"""Урок 5 Задание 2
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке.
"""
with open("text_2.txt", "r", encoding='utf-8') as f_obj:
    usefulness = [f'{line}. {" ".join(count.split())} - {len(count.split())} слов' for line, count in enumerate(f_obj, 1)]
    print(*usefulness, f"Всего строк - {len(usefulness)}.", sep="\n")

# another way
with open("text_2.txt", encoding='utf-8') as f:
    my_line = f.readlines()
    for index, value in enumerate(my_line, 1):
        number_of_words = len(value.split())
        print(f'Строка {index} содержит {number_of_words} слов')