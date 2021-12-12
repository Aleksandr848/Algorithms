"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
import random
rand1 = random.randint(4, 10)
rand2 = random.randint(4, 10)
matrix = [[random.randrange(0, 40) for y in range(rand1)] for x in range(rand2)]

for mat in matrix:
    print(mat)

min_list = []
print()
reversed_matrix = [[matrix[x][y] for x in range(rand2)] for y in range(rand1)]

min_list = []
for i in range(rand1):
    min_num = reversed_matrix[i][0]
    for j in range(rand2):
        if min_num > reversed_matrix[i][j]:
            min_num = reversed_matrix[i][j]
    min_list.append(min_num)

max_num = min_list[0]
for num in min_list:
    if max_num < num:
        max_num = num

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы - {max_num}')
