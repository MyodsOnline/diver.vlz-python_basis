import time
try:
    f = open('testfile', 'w', encoding='utf-8')
    f.write(f'Записываем строку в файл {time.ctime()}')
    print('Готово!')
except OSError:
    print('Ошибка OSError')
finally:
    print('Эта строка вывполняется в любом случае')

# ------
def ask_for_int():
    while True:
        try:
            result = int(input('Enter a num, please: '))
        except ValueError:
            print("I'm asking a int")
            continue
        else:
            print(result)
            break
        finally:
            print('Done!')
ask_for_int()