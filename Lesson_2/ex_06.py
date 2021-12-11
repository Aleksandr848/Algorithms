"""
В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, то вывести загаданное число.
"""
import random

number = random.randint(0, 100)
user_num = int(input('Угадай число от 0 до 100: '))
try_num = 1

while try_num < 10:
    if user_num == number:
        print('Ты угадал!')
        break
    elif user_num != number:
        if user_num < number:
            print('Загаданное число больше!')
            user_num = int(input('Пробуй ещё: '))
            try_num += 1
            continue
        else:
            print('Загаданное число меньше!')
            user_num = int(input('Пробуй ещё: '))
            try_num += 1
            continue
if try_num == 10:
    print(f'Ты не угадал! Загаданное число - {number}')