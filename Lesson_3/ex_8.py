"""
Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

matrix = [[int(x) for x in input('Введите четыре числа через пробел: ').split()] for y in range(4)]

for i in range(len(matrix)):
    sum_of_numbers = 0
    for j in range(len(matrix[i])):
        sum_of_numbers += matrix[i][j]
    matrix[i].append(sum_of_numbers)
for num_list in matrix:
    print(num_list)
