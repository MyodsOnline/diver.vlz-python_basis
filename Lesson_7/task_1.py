"""Урок 7 Задание 1
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__() ), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

m_1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m_2 = [[5, 7, 23], [9, 23, -54], [12, 3, 16]]


class Matrix_1:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join('\t'.join([str(itm) for itm in line]) for line in self.data)

    def __add__(self, other):
        try:
            add = [[int(self.data[line][itm]) + int(other.data[line][itm]) for itm in range(len(self.data[line]))]
                   for line in range(len(self.data))]
            return Matrix_1(add)
        except IndexError:
            return f'Data error'


mtx_1 = Matrix_1(m_1)
mtx_2 = Matrix_1(m_2)
mtx_3 = mtx_1 + mtx_2

print(f'---first way---')
print(f'{mtx_1}\n{"*" * 15}')
print(f'{mtx_2}\n{"*" * 15}')
print(f'{mtx_3}')


# another way
class Matrix_2:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join(map(str, self.data))

    def __add__(self, other):
        add = []
        for el_i in range(len(self.data)):
            add.append([])
            for el_j in range(len(self.data[0])):
                add[el_i].append(self.data[el_i][el_j] + other.data[el_i][el_j])
        return '\n'.join(map(str, add))


mtx_4 = Matrix_2(m_1)
mtx_5 = Matrix_2(m_2)
mtx_6 = mtx_4 + mtx_5
print(f'\n---second way---')
print(f'{mtx_4}\n{"*" * 15}')
print(f'{mtx_5}\n{"*" * 15}')
print(f'{mtx_6}')


# another way
class Matrix_3:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join(map(lambda r: '\t'.join(map(str, r)), self.data)) + '\n'

    def __add__(self, other):
        return Matrix_3(map(lambda r_1, r_2: map(lambda x, y: x + y, r_1, r_2), self.data, other.data))

mtx_7 = Matrix_2(m_1)
mtx_8 = Matrix_2(m_2)
mtx_9 = mtx_7 + mtx_8
print(f'\n---third way---')
print(f'{mtx_7}\n{"*" * 15}')
print(f'{mtx_8}\n{"*" * 15}')
print(f'{mtx_9}')