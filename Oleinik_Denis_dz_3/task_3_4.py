"""
Определить, какое число в массиве встречается чаще всего.
"""

import random

SIZE = 50
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


num = array[0]
max_often = 1
for i in range(SIZE - 1):
    often = 1
    for j in range(i + 1, SIZE):
        if array[i] == array[j]:
            often += 1
        if often > max_often:
            max_often = often
            num = array[i]

if max_often > 1:
    print(f'Число {num} встречается {max_often}')
else:
    print('Все элементы уникальны')
