class Auto:
    def __init__(self, p_1, p_2):
        self.p_1 = p_1
        self.p_2 = p_2

# перезагрузка метода del
    def __del__(self):
        print('Object deleted!')

# перезагрузка метода print
    def __str__(self):
        return f'a_1 is {self.p_1}, a_2 is {self.p_2}'

# перезагрузка метода add
    def __add__(self, other):
        return Auto(self.p_1 + other.p_1, self.p_2 + other.p_2)

# перезагрузка метода call
    def __call__(self, new_p_1):
        self.p_1 = new_p_1

a_1 = Auto(23, 34)
a_2 = Auto(27, 66)
a_3 = Auto(1, 1)

print(f'# перезагрузка метода del:')
del a_3
print(f'# перезагрузка метода print():\n{a_1}')
print(f'# перезагрузка метода add:\n{a_1 + a_2}')

a_1('New param #1')
print(f'# перезагрузка метода call:\n{a_1}')

class oop:
    def __setattr__(self, key, value):
        self.__dict__[key] = value
        print(self.__dict__)

ex_1 = oop()
ex_2 = oop()
ex_1.lol = 66
ex_2.lil = 111
#print(ex_1.lol)