"""
Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке
и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""

while True:
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))
    while True:
        operation = input('Введите действие "+", "-", "*" или "/". Или "0", если хотите закончить: ')
        if operation not in ("+", "-", "*", "/", "0"):
            print('Хватит самодеятельности, введите то, что Вас просят!')
            continue
        break
    if operation == '0':
        break
    if operation == '/' and number_2 == 0:
        print('На ноль делить нельзя!')
        continue
    if operation == '+':
        print(number_1 + number_2)
    if operation == '-':
        print(number_1 - number_2)
    if operation == '*':
        print(number_1 * number_2)
    if operation == '/':
        print(number_1 / number_2)
