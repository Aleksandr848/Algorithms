"""
Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

"""

x = int(bin(5)[2:])
y = int(bin(6)[2:])

print(f'Побитовая операция "5 И 6" - {x & y},\n'
      f'Побитовая операция "5 ИЛИ 6" - {x | y}\n'
      f'Побитовая операция "5 ТОЛЬКО ИЛИ 6" - {x ^ y}\n'
      f'Побитовый сдвиг вправо числа 5 на два знака - {5 >> 2}\n'
      f'Побитовый сдвиг влево числа 5 на два знака - {5 << 2}')
