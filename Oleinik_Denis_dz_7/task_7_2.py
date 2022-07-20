"""
Отсортируйте по возрастанию методом слияния одномерный вещественный
массив, заданный случайными числами на промежутке [0; 50). Выведите
на экран исходный и отсортированный массивы.
"""
import random

# SIZE = 10
# MIN_ITEM = 0
# MAX_ITEM = 50
# array = [round(random.uniform(MIN_ITEM, MAX_ITEM), 3) for _ in range(SIZE)]
# print(array)


array = [1.759, 38.433, 45.007, 22.025, 8.834, 36.127, 34.77, 42.576, 36.212, 36.239]
print('Исходный массив:', array, sep='\n')
print()


def merge_sort(array_sorted):
    if len(array_sorted) == 0 or len(array_sorted) == 1:
        return array_sorted
    elif len(array_sorted) > 1:
        mid = len(array_sorted) // 2
        left = merge_sort(array_sorted[:mid])
        right = merge_sort(array_sorted[mid:])

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array_sorted[k] = left[i]
                i += 1
            else:
                array_sorted[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array_sorted[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array_sorted[k] = right[j]
            j += 1
            k += 1
    return array_sorted


print('Отсортированный массив:', merge_sort(array), sep='\n')
