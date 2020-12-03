# *args, enumerate
def itrrgs(*args):
    """
    	DOCSTRING: функция печатает нумерованй список аргументов
    	INPUT: args
    	OUTPUT: print(el)
    """
    for el in enumerate(args, 1):
        print(el)


itrrgs((-1 + 0j), 1, 2.2, True, None, 'String', [3, 4],
       (5, 6, 6.5), {7: 'seven', 8: 'eight'}, {9, 10},
       frozenset(), range(11), b'twelve', bytearray(b'thirteen'),
       zip(*[(14, 15), (16, 17), ('a', 'b')]), TypeError)


# *args, **kwargs
def together(*args, **kwargs):
    print(f'i would like {args[0]} {kwargs["food"]}')


together(12, 10, 34, fruit='orange', food='eggs')

# map
mylist = [1, 2, 3, 4, 5, 6]


def sq(myli):
    """
    	DOCSTRING: функция будет вызвана
    """
    return myli ** 2


mysqlist = list(map(sq, mylist))
print(mysqlist)


# map
def sliser(name):
    if len(name) % 2 == 0:
        return 'ok'
    else:
        return name[1].upper()


names = ['andy', 'billy', 'cyndy', 'dill']

print(list(map(sliser, names)))


# evencheck
def evencheck(nums):
    return nums % 2 == 0


mynums = [1, 2, 3, 4, 5, 6]
print(list(filter(evencheck, mynums)))

# map, filter
mynums = [1, 2, 3, 4, 5, 6]
print(list(map(lambda num: num ** 2, mynums)))
print(list(filter(lambda nums: nums % 2 == 0, mynums)))


# capitalize vowel letters
def cap(sentance):
    ssent = []
    for el in sentance:
        if el in 'eyuioa':
            ssent.append(el.upper())
        else:
            ssent.append(el)
    return ''.join(ssent)


print(cap('apple'))
print(cap('i will no sleep'))

# генератор списка/синтаксический сахар
my_list = [1, 2, 3, 4, 10, 15, 20, 25, 30, 35]
mew_list = [el + 10 for el in my_list]
new_list = [el for el in my_list if el % 2 == 0]

print(f'my_list - {my_list}\nmew_list - {mew_list}\nnew_list - {new_list}')

# генератор списка
generator = (param * param for param in range(0, 5))
for el in generator:
    print(el)
