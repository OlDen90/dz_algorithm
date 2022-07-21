"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный»
и «максимальный отрицательный». Это два абсолютно разных значения.
"""

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


position_num = array[0]
max_negative = -10**6 - 1

for i in array:
    if 0 > i > max_negative:
        max_negative = i
        position_num = array.index(i)
print(f'Максимальный отрицательный элемент {max_negative} имеет позицию {position_num + 1}')
