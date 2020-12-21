"""урок 3 задание 6
Реализовать функцию int_func() , принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""

def int_func(text):
    b = []
    for el in text.split():
        b.append(el.capitalize())
    return ' '.join(list(b))


print(int_func(input('Type the text here: ')))


# anoter way
text = input('Type the text here: ')


def int_func(text):
    return text[:1].upper() + text[1:]


for el in text.split():
    result = int_func(el)
    print(''.join(result))


# IDDQD mode
int_func = lambda word: word.title()
print(' '.join(map(int_func, input("Enter phrase: ").split())))