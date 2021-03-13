# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за квартал для каждого.
# Программа должна определить среднюю прибыль и
# вывести наименования предприятий, чья прибыль выше среднего.
# Отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple
Company = namedtuple('Company', ['name', 'quaters', 'profit'])
all_companies = set()
PERIOD = 4
total_profit = 0

num = int(input('Введите количество компаний: '))
for i in range(1, num + 1):
    profit = 0
    quaters = []
    name = input(f'Введите название предприятия {i}: ')
    for j in range (PERIOD):
        quaters.append(int(input(f'Прибыль за {j+1}-й квартал: ')))
        profit += quaters[j]
        comp = Company(name=name, quaters=tuple(quaters), profit=profit)
    all_companies.add(comp)
    total_profit += profit

# print(all_companies)
avg = total_profit/num

for comp in all_companies:
    if comp.profit > avg:
        print(f'Компания {comp.name} имеет средниюю прибыль выше среднего значения ')
    elif comp.profit < avg:
        print(f'Компания {comp.name} имеет средниюю прибыль ниже среднего значения ')
    else:
        print(f'Компания {comp.name} имеет средниюю прибыль равную среднему значению ')
