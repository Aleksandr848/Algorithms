"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import random

num_of_numbers = [random.choice(range(0, 200)) for x in range(random.randint(10, 20))]  # генератор списка чисел.
print(f'\n{num_of_numbers}')

min_list = []
while True:
    min_num = num_of_numbers[0]
    for num in num_of_numbers:
        if num < min_num:
            min_num = num
    min_list.append(min_num)
    if len(min_list) == 2:
        break
    num_of_numbers.remove(min_num)
if min_list[0] == min_list[1]:
    print(f'Два наименьших элемента равны между собой. Это {min_list[0]}')
else:
    print(f'Два наименьших элемента - {min_list[0]} и {min_list[1]}')
