"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
"""
import math

# number = input('Введите число: ')
# i = len(number)
# reversed_number = 0
# for num in number:
#     reversed_number += int(num) * math.pow(10, len(number) - i)
#     i -= 1
# print(int(reversed_number))

number = int(input('Введите число: '))
reversed_number = 0
i = len(str(number))
for j in range(i):
    reversed_number += (number % 10) * math.pow(10, i - j - 1)
    number = number // 10
print(int(reversed_number))

