"""
Определить, какое число в массиве встречается чаще всего.
"""
import random

num_of_numbers = [random.choice(range(3, 8)) for x in range(random.randint(10, 20))]  # генератор списка чисел.
print(f'\n{num_of_numbers}')
flag = 0
while True:
    max_count = 1
    number = num_of_numbers[0]
    for i in range(len(num_of_numbers) - 1):
        count = 1
        for j in range(i + 1, len(num_of_numbers)):
            if num_of_numbers[i] == num_of_numbers[j]:
                count += 1
        if count > max_count:
            max_count = count
            number = num_of_numbers[i]
    if flag > max_count:
        break
    if max_count > 1:
        print(f'\nЧисло {number} встречается {max_count} раз(-а)')
    else:
        print('Все числа встречаются одинаковое число раз')
    flag = max_count
    for _ in range(num_of_numbers.count(number)):
        num_of_numbers.remove(number)
