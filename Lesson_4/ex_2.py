import math
import time
from datetime import timedelta

n = int(input())  # число, до которого хотим найти простые числа
start_time = time.monotonic()
numbers = list(range(2, n + 1))
for number in numbers:
    if number != 0:
        for candidate in range(2 * number, n + 1, number):
            numbers[candidate - 2] = 0
print(*list(filter(lambda x: x != 0, numbers)))
end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))

"""
Выше - алгоритм решето Эратосфена. Его сложность - O(n*log(log n)) (данные из википедии) В принципе можно оставить 
только O(n), так как остальная часть незначительна. Ниже программа без алгоритма Эратосфена. Её сложность по моей 
интуитивной оценке - O(n*log n). При большом значении n видно, что Эратосфен прожил жизнь не зря.

"""


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


start_time = time.monotonic()
for x in range(1, n + 1):
    if is_prime(x):
        print(x, end=" ")
end_time = time.monotonic()
print(f'\n{timedelta(seconds=end_time - start_time)}')
