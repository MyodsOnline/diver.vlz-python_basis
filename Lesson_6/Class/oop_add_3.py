"""Задача 3
В этом задании создайте класс банковского счёта, который имеет два атрибута:
owner - владелец, balance - баланс
и два метода:
deposit - внести средства, withdraw - снять средства
Дополнительное условие - сумма снятия не должна превышать доступный баланс.
Создайте экземпляр класса, сделайте несколько внесений и снятий средств, а также проверьте,
что баланс счёта не может уходить в минус при снятии средств.
"""


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print(f'{self.owner}, Вам доступно: {self.balance}.')

    def deposit(self, income):
        try:
            self.balance = self.balance + int(income)
            return f'Баланс пополнен на {income}. Текущий остаток: {self.balance}'
        except ValueError:
            return f'Data error! Вам доступно: {self.balance}'

    def withdraw(self, withdraw):
        try:
            if int(withdraw) > self.balance:
                return f'У вас недостаточно срдств. Вам доступно: {self.balance}'
            else:
                self.balance = self.balance - int(withdraw)
                return f'Баланс уменьшен на {withdraw}. Текущий остаток: {self.balance}'
        except ValueError:
            return f'Data error! Вам доступно: {self.balance}'


user_1 = Account(input('Введите имя: '), int(input('Текущий баланс: ')))
print(user_1.deposit(input('Введите сумму пополнения: ')))
print(user_1.withdraw(input('Сколько хотите снять: ')))
