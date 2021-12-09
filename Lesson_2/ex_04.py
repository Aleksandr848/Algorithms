"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""
import math

number = int(input('Введите количество элементов: '))
numbers = [1 / x for x in [math.pow(2, y) * math.pow(-1, y) for y in range(number)]]
print(numbers)
sum_of_numbers = 0
for num in numbers:
    sum_of_numbers += num
print(sum_of_numbers)

