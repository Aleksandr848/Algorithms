"""
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

input_numbers = int(input('Введите количество вводимых чисел: '))
number = int(input('Введите цифру, которую надо найти: '))
i = 0
sequence_of_numbers = ''
while i < input_numbers:
    sequence_of_numbers += input('Введите число: ')
    i += 1

num_of_numbers = 0
for n in sequence_of_numbers:
    if int(n) == number:
        num_of_numbers += 1
print(f'Количество цифр "{number}" - {num_of_numbers}')
