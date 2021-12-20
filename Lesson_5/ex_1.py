"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
чья прибыль ниже среднего.
"""

companies_profit = {}
n = int(input("Количество компаний: "))
s = 0
for i in range(n):
    company_name = input(str(i + 1) + "-я компания: ")
    profit = list(input("Доход по кварталам через пробел: ").split())
    companies_profit[company_name] = profit
    for p in profit:
        s += int(p)
print(companies_profit)
average_profit = s / n
print(f'\nСредний доход по предприятиям: {average_profit}.')
print('Компании с доходом выше среднего: ')
for i in companies_profit:
    sum_q = 0
    for p in companies_profit[i]:
        sum_q += int(p)
    if sum_q > average_profit:
        print(i)

print('Компании с доходом ниже среднего: ')
for i in companies_profit:
    sum_q = 0
    for p in companies_profit[i]:
        sum_q += int(p)
    if sum_q < average_profit:
        print(i)

"""
Сложность O(n+n+n) = O(3*n), так как программа трижды пробегает цикл n раз. Константу можно убрать - остаётся O(n)
"""