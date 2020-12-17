"""Урок 2 Задание 3
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""
seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
user_choise = int(input('Enter number of mounth: '))
if 0 < user_choise <= 12:
    if user_choise in (3, 4, 5):
        print(f'Season from list - {seasons_list[1]}\n'
              f'Seaon from dict - {seasons_dict[2]}')
    elif user_choise in (6, 7, 8):
        print(f'Season from list - {seasons_list[2]}\n'
              f'Seaon from dict - {seasons_dict[3]}')
    elif user_choise in (9, 10, 11):
        print(f'Season from list - {seasons_list[3]}\n'
              f'Seaon from dict - {seasons_dict[4]}')
    else:
        print(f'Season from list - {seasons_list[0]}\n'
              f'Seaon from dict - {seasons_dict[1]}')
else:
    print('Wrong data')

# another way:
while True:
    user_month = input('Введите номер месяца от 1 до 12: ')
    if user_month.isdigit() and 0 < int(user_month) <= 12:
        season_1 = ['зима', 'весна', 'лето', 'осень', 'зима']
        season_2 = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень', 4: 'зима'}
        print(f'Список сезонов - {season_1[int(user_month) // 3]}\nСловарь сезонов - {season_2[int(user_month) // 3]}')
        break
    else:
        print("Error!!!")
