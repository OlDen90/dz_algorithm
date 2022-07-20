"""
В массиве случайных целых чисел поменять местами
минимальный и максимальный элементы
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


num_min = 100
num_max = 0

for i in array:
    if i > num_max:
        num_max = i
    if i < num_min:
        num_min = i

print(num_min)
print(num_max)

for i in range(len(array)):
    if array[i] == num_max:
        array[i] = num_min
    elif array[i] == num_min:
        array[i] = num_max
print(array)
