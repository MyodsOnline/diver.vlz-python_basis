"""урок 3 задание 5
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после несколькихчисел, то вначале нужно добавить сумму этих чисел
к полученной ранее сумме и после этого завершить программу.
"""

def summ_func():
    total_sum = 0
    while True:
        sum_list = list((input('Enter nums or "q" to exit: ')).split())
        for el in sum_list:
            if el == 'q' or el == 'Q':
                return (f'Stop. Final sum: {total_sum}')
            else:
                try:
                    total_sum += int(el)
                except ValueError:
                    print('Data error!')
        print(f'{total_sum}')


print(summ_func())

# anoter way, with MAP
num = 0
try:
    while num != '#':
        for i in map(int, input("Для выхода наберите '#'\nВведите числа, используя пробел: ").split()):
            num += i
        print(num)
except ValueError:
    print(f'Data error. Final summ is - {num}')