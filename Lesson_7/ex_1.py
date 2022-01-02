"""
 Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
 на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована
 в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random

num_of_numbers = random.sample(range(-100, 100), random.randint(20, 100))
print(num_of_numbers)


def buble_sort(numbers):
    is_changed = True  # Добавляем переменную, которая остановит цикл, если перемен больше не будет
    for i in range(len(numbers)):
        if not is_changed:
            break
        for j in range(0, len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                is_changed = True
            else:
                is_changed = False
    return numbers


print(buble_sort(num_of_numbers))
