"""

Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

"""
number = int(input('Введите трёхзначное число: '))

digit_1 = number // 100
digit_2 = (number - digit_1 * 100) // 10
digit_3 = (number - digit_1 * 100) % 10

print(f'Сумма цифр равна - {digit_1 + digit_2 + digit_3}.\nПроизведение цифр равно - {digit_1 * digit_2 * digit_3}')
