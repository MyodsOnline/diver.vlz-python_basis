# Напишите функцию, которая возвращает меньшее из двух чисел, если оба эти числа чётные.
# Иначе возвращает большее из двух чисел, если одно или оба числа нечётные.

def ledd(num_1, num_2):
    if num_1 % 2 == 0 and num_2 % 2 == 0:
        return min(num_1, num_2)
    else:
        return max(num_1, num_2)


print(ledd(int(input('enter first: ')), int(input('enter second: '))))


# Напишите функцию, которая получает на входе строку из двух слов,
# и возвращает True если оба слова начинаются с одной и той же буквы.

def animal_crackers(text):
    my_list = text.split()
    return my_list[0][0] == my_list[1][0]


print(animal_crackers('Levelheaded Llama'))


# На входе два числа, функция возвращает True если сумма этих чисел равна 20
# или если одно из чисел равно 20. В противном случае, возвращает False

def makes_twenty(n1, n2):
    try:
        n1, n2 = int(n1), int(n2)
        return (n1 + n2) == 20 or n1 == 20 or n2 == 20
    except ValueError:
        return 'ValueError'


print(makes_twenty(input('enter first num: '), input('enter second num: ')))


# Напишите функцию, которая переводит в верхний регистр первую и четвёртую буквы имени.

def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'word is too short'


print(old_macdonald('macdonald'))


# На входе фраза, на выходе вернуть слова в обратном порядке.

def master_yoda(text):
    return ' '.join(text.split()[::-1])


print(master_yoda(input('enter your string: ')))


# на входе число n, вернуть True если n находится не далее чем на 10 от чисел 100 или 200.
def almost_there(n):
    return 90 <= n <= 110 or 190 <= n <= 210
    # return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


print(almost_there(int(input('enter num: '))))


# На входе список чисел, вернуть True если массив содержит где-нибудь 3 рядом с 3.
def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True


print(has_33([1, 3, 3, 1]))


# На входе строка, вернуть строку где каждый символ исходной строки повторяется три раза.
def paper_doll(text):
    my_pd_list = ''
    for el in text:
        my_pd_list += el * 3
    return my_pd_list


print(paper_doll(input('enter your sting: ')))


# На входе три числа от 1 до 11. Если их сумма меньше или равна 21, то вернуть их сумму.
# Если сумма больше 21 и среди чисел есть 11, то уменьшить общую сумму на 10.
# И наконец, если сумма (в том числе после уменьшения) превышает 21, вернуть 'BUST'.
def blackjack(a, b, c):
    if sum((a, b, c)) <= 21:
        return sum((a, b, c))
    elif sum((a, b, c)) > 21 and 11 in (a, b, c):
        return sum((a, b, c)) - 10
    else:
        return 'BUST'


print(blackjack(9, 9, 9))


# Вернуть сумму чисел в массиве, кроме набора чисел который начинается с 6 и
# продолжается до 9 (для каждого числа 6 далее где-то будет число 9).
# Вернуть 0 если чисел нет.

def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


print(summer_69([2, 1, 6, 9, 11]))


# Напишите функцию, которая берёт список чисел, и возвращает True,
# если в списке содержатся числа 0 0 7 в указанном порядке.
def spy_game(nums):
    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)

    return len(code) == 1


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
