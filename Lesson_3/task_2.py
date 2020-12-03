"""урок 3 задание 2
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о
пользователе одной строкой.
"""

# вариант через *args
def user_info(*args):
    return f'name = {args[0]}, lastname = {args[1]}, birthday = {args[2]}, city = {args[3]}, email = {args[4]}, phone = {args[5]}'


print(user_info(input('name - '), input('lastname - '), input('birthday - '), input('city - '), input('email - '),
                input('phone - ')))


# другой вариант через *kwargs
def personal_info(**kwargs):
    return ' '.join(kwargs.values())


print(personal_info(name=input("name - "), surname=input("lastname - "),
      birthday=input("birthday - "), city=input("city - "), email=input("email - "),
      phone_number=input("phone - ")))


# другой вариант через позиционные параметры
def person_inf(name, surname, birthday, city, email, phone):
    return f"Name - {name}; Surname - {surname}; birthday - {birthday}; city - {city};" \
           f" email - {email}; phone - {phone}"


print(person_inf(name=input("name - "), surname=input("lastname - "), birthday=input("birthday - "), city=input("city - "),
                 email=input("email - "), phone=input("phone - ")))