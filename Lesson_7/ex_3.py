"""
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
"""
import random

num_of_numbers = random.sample(range(0, 100), 2 * random.randint(2, 10) + 1)
print(num_of_numbers)

for i in range(len(num_of_numbers)):
    n = 0
    k = 0
    for j in range(len(num_of_numbers)):
        if num_of_numbers[i] > num_of_numbers[j]:
            n += 1
        elif num_of_numbers[i] < num_of_numbers[j]:
            k += 1
    if n == k:
        print(f'Медиана массива - {num_of_numbers[i]}')
        break
