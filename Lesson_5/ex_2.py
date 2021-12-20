"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
коллекция, элементы которой это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

"""
import collections

numbers16_list = collections.deque('0123456789ABCDEF')
numbers10_dict = dict(zip(numbers16_list, range(16)))  # {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
# 'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

"""
Сложность функции сложения O(n), где n - количество цифр в длиннейшем числе.
"""


def sum_of_numbers(first_number, second_number):
    first_number = first_number.copy()
    second_number = second_number.copy()
    if len(first_number) < len(second_number):
        first_number, second_number = second_number, first_number
    for _ in range(len(first_number) - len(second_number)):
        second_number.extendleft('0')

    sum_of_num = collections.deque()
    k = 0
    for x in range(len(first_number) - 1, -1, -1):
        num_1 = numbers10_dict[first_number[x]]
        num_2 = numbers10_dict[second_number[x]]
        result_num = num_1 + num_2 + k
        if result_num > 15:
            k = 1
            result_num -= 16
        else:
            k = 0
        sum_of_num.appendleft(numbers16_list[result_num])
    if k == 1:
        sum_of_num.appendleft('1')
    return sum_of_num


"""
Сложность функции умножения O(n**2), так как тут уже вложенный цикл.
"""


def mult_of_numbers(first_number, second_number):
    first_number = first_number.copy()
    second_number = second_number.copy()
    if len(first_number) < len(second_number):
        first_number, second_number = second_number, first_number
    for _ in range(len(first_number) - len(second_number)):
        second_number.extendleft('0')

    multiplication = collections.deque('0')
    for x in range(len(first_number) - 1, -1, -1):
        num_2 = numbers10_dict[second_number[x]]
        interim = collections.deque('0')
        for _ in range(num_2):
            interim = sum_of_numbers(interim, first_number)
        interim.extend('0' * (len(first_number) - x - 1))
        multiplication = sum_of_numbers(multiplication, interim)
    return multiplication


first = collections.deque(input('Первое число: ').upper())
second = collections.deque(input('Второе число: ').upper())

print(sum_of_numbers(first, second))
print(mult_of_numbers(first, second))
