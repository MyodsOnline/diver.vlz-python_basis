"""урок 3 задание 3
Реализовать функцию my_func() , которая принимает три позиционных аргумента, и
возвращает сумму наибольших двух аргументов.
"""


def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    try:
        my_list.remove(min(my_list))
        return f'my_list - {my_list}; sum - {sum(my_list)}'
    except TypeError:
        return "Invalid data!"


print(my_func(2, 11, -30))


# anoter way with sorted
def my_sort_func(arg1, arg2, arg3):
    return sum(sorted([arg1, arg2, arg3])[1:])


print(my_sort_func(2, 11, -30))


# anoter way with lambda
my_lambda_func = lambda arg_1, arg_2, arg_3: (arg_1 + arg_2 + arg_3) - min(arg_1, arg_2, arg_3)

print(my_lambda_func(2, 11, -30))
