"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

import random
import sys
import tracemalloc

tracemalloc.start()
num_of_numbers = [random.choice(range(-400000, 400000)) for x in
                  range(random.randint(10000, 20000))]  # генератор списка чисел.
x = len(num_of_numbers)
print(f'Длина списка {x}')
print(f'Объём занимаемой памяти - {sys.getsizeof(num_of_numbers)}')
negative_list = []
for num in num_of_numbers:
    if num < 0:
        negative_list.append(num)
max_num = negative_list[0]
for num in negative_list:
    if max_num < num:
        max_num = num
print(f'Максимальный отрицательный элемент - {max_num}. Его индекс - {num_of_numbers.index(max_num)}')
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)


tracemalloc.reset_peak()
tracemalloc.start()
num_of_numbers.append(0)
sort_list = quicksort(num_of_numbers)
negative_list = sort_list[:sort_list.index(0)]
print(
    f'Максимальный отрицательный элемент - {negative_list[-1]}. Его индекс - {num_of_numbers.index(negative_list[-1])}')
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

tracemalloc.reset_peak()
tracemalloc.start()
num_of_numbers.append(0)
sort_list = num_of_numbers.copy()
sort_list.sort()
negative_list = sort_list[:sort_list.index(0)]
print(
    f'Максимальный отрицательный элемент - {negative_list[-1]}. Его индекс - {num_of_numbers.index(negative_list[-1])}')
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

"""
Для эксперементов с памятью я использовал задачу для поиска максимального отрицательного элемента. Задача решена тремя
способами. На первом месте (обозначим №1) по времени исполнения - используя ф-цию sort, на втором (обозначим №2) - с
помощью дополнительного списка и поиска в нём максимального значения и на третьем месте (обозначим №3) - сортировка
Хоара. Для замера памяти я использовал модуль tracemalloc. По использованию памяти во время исполнения программы
места начиная от самой малозатратной распределились следующим образом - №2, №1 и №3. Я, конечно, был уверен, что 
сортировка Хоара ввиду своей рекурсивности пожрёт от души, но никак не предполагал, что №1, которая в три раза 
быстрее №2, на деле жрёт памяти на 50% больше, чем №2. Делая выводы можно сказать, что если память не проблема, то 
выбираем №1, а если есть проблемы с памятью, то №2. 

Python 3.9
Разрядность - 64
"""