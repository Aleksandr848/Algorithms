"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

import random

num_of_numbers = [random.choice(range(-40, 40)) for x in range(random.randint(10, 20))]  # генератор списка чисел.
print(f'\n{num_of_numbers}')

negative_list = []
for num in num_of_numbers:
    if num < 0:
        negative_list.append(num)
max_num = negative_list[0]
for num in negative_list:
    if max_num < num:
        max_num = num
print(f'Максимальный отрицательный элемент - {max_num}. Его индекс - {num_of_numbers.index(max_num)}')
