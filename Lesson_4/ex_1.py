"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

import random
import time
from datetime import timedelta

start_time = time.monotonic()

num_of_numbers = [random.choice(range(-400000, 400000)) for x in
                  range(random.randint(10000, 20000))]  # генератор списка чисел.
#  print(f'\n{num_of_numbers}')

negative_list = []
for num in num_of_numbers:
    if num < 0:
        negative_list.append(num)
max_num = negative_list[0]
for num in negative_list:
    if max_num < num:
        max_num = num

print(f'Максимальный отрицательный элемент - {max_num}. Его индекс - {num_of_numbers.index(max_num)}')
end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))

"""
В данной реализации сложность определяется количеством элементов (n) в списке. Имеется в программе два цикла, в худшем 
случае оба будут работать n раз, итого - 2*n раз. Значит сложность - O(n) или линейная сложность.
"""


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)


start_time = time.monotonic()
num_of_numbers.append(0)
sort_list = quicksort(num_of_numbers)
negative_list = sort_list[:sort_list.index(0)]
print(
    f'Максимальный отрицательный элемент - {negative_list[-1]}. Его индекс - {num_of_numbers.index(negative_list[-1])}')
end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))

"""
Выше используется алгоритм сортировки Хоара. Его сложность в данном случае O(n*logn). Это видно и по времени выполнения
программы - оно более чем в пять раз медленнее, чем в первом случае.
"""

start_time = time.monotonic()
num_of_numbers.append(0)
sort_list = num_of_numbers.copy()
sort_list.sort()
negative_list = sort_list[:sort_list.index(0)]
print(
    f'Максимальный отрицательный элемент - {negative_list[-1]}. Его индекс - {num_of_numbers.index(negative_list[-1])}')
end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))

"""
И в третьем варианте я использую встроенную функцию sort() для сортировки списка. Его сложность в худшем случае 
O(n*logn), в лучшем - O(n). И время выполнения оказывается
более чем в два раза быстрее, чем в первом случае и в 12 раз быстрее с сортировкой Хоара при больших значениях длины 
списка. Оно и понятно - sort - не рекурсивная функция.
"""
