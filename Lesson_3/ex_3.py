"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random
num_of_numbers = random.sample(range(0, 100), random.randint(5, 20))  # генератор случайного списка натуральных чисел.
print(f'\n{num_of_numbers}')
max_index = 0
min_index = 0
for i in range(len(num_of_numbers)):
    if num_of_numbers[max_index] < num_of_numbers[i]:
        max_index = i
    if num_of_numbers[min_index] > num_of_numbers[i]:
        min_index = i
num_of_numbers[max_index], num_of_numbers[min_index] = num_of_numbers[min_index], num_of_numbers[max_index]
print(num_of_numbers)
