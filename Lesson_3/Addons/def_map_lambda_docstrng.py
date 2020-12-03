# 1 ---------------------------------------------------------

mynums = [100, 200, 50]


def myargs(*args):
    """
    DOCSTRING: функция удваивает аргументы и выводит их сумму
    INPUT: args
    OUTPUT: sum(args) * 2
    """
    return f'результат вычисления - {sum(args) * 2}.'


print(myargs(100, 200, 50))
print(sum(map(lambda num: num * 2, mynums)))  # дополним lambda
print(f'{"*" * 20}')
help(myargs)


# результат вычисления - 700.
# 700
# ********************
# Help on function myargs in module __main__:
#
# myargs(*args)
#     DOCSTRING: функция удваивает аргументы и выводит их сумму
#     INPUT: args
#     OUTPUT: sum(args) * 2


# 2 ---------------------------------------------------------
