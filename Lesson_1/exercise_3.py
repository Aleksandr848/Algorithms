from fractions import Fraction
"""
По введенным пользователем координатам двух точек вывести уравнение прямой вида
y = kx + b, проходящей через эти точки.

"""

x1, y1 = int(input('Введите координаты х1: ')), int(input('Введите координату y1: '))
x2, y2 = int(input('Введите координаты х2: ')), int(input('Введите координату y2: '))

k = Fraction((y1 - y2),(x1 - x2))
b = y2 - k * x2

print(f'y = {k}x + {b}')
