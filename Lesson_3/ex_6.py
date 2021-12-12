"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

num_of_numbers = [random.choice(range(0, 40)) for x in range(random.randint(10, 20))]  # генератор списка чисел.
print(f'\n{num_of_numbers}')

max_index = 0
min_index = 0
for i in range(len(num_of_numbers)):
    if num_of_numbers[max_index] < num_of_numbers[i]:
        max_index = i
    if num_of_numbers[min_index] > num_of_numbers[i]:
        min_index = i
sum_of_numbers = 0
if abs(max_index - min_index) == 1:
    print("Между максимальным и минимальным элементом нет элементов.")
elif max_index < min_index:
    for num in num_of_numbers[max_index + 1: min_index]:
        sum_of_numbers += num
elif max_index > min_index:
    for num in num_of_numbers[min_index + 1: max_index]:
        sum_of_numbers += num
else:
    print('Все элементы массива равны.')

while sum_of_numbers:
    print(f'Сумма элементов, находящихся между минимальным и максимальным элементами - {sum_of_numbers}')
    break
