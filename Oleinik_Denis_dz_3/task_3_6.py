"""
В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами. Сами минимальный
и максимальный элементы в сумму не включать
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


min_num = 100
position_min_num = array[0]

max_num = 0
position_max_num = array[0]

num = 0

for i in array:
    if i > max_num:
        max_num = i
        position_max_num = array.index(i)
    if i < min_num:
        min_num = i
        position_min_num = array.index(i)

print(f'Минимальный элемент {min_num}, позиция {position_min_num + 1}')
print(f'Минимальный элемент {max_num}, позиция {position_max_num + 1}')

if position_min_num < position_max_num:
    position_min_num = position_min_num + 1
    for i in array[position_min_num : position_max_num]:
        num += i
else:
    position_max_num = position_max_num + 1
    for i in array[position_max_num : position_min_num]:
        num += i
print(f'Сумма элементов между min и max = {num}')
