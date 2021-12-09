"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""


def sum_of_numbers(number: int):
    s = 0
    i = len(str(number))
    for _ in range(i):
        s += number % 10
        number = number // 10
    return s


natural_numbers = input('Введите числа через пробел: ').split()
print(natural_numbers)

max_sum = natural_numbers[0]
for num in natural_numbers:
    if sum_of_numbers(int(num)) > sum_of_numbers(int(max_sum)):
        max_sum = num
print(max_sum)
