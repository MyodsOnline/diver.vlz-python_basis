"""урок 1 задание 5
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность
выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и
определите прибыль фирмы в расчете на одного сотрудника.
"""

revenue = float(input('Enter the revenue value: '))
costs = float(input('Enter the cost value: '))
profit = revenue - costs
if revenue == costs:
    print('The profit and cost values are equal.')
elif profit > 0:
    print(f'The company profit is: {profit}, congratulations!\nThe return on revenue is: {profit / revenue:.2}.')
    headcount = int(input('Enter the number of employees: '))
    print(f'The profit per employee is: {profit / headcount:.2f}.')
else:
    print(f'The company worked at a loss: {profit}.')
