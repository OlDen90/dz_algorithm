"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным
образом. Найдите в массиве медиану. Медианой называется элемент ряда,
делящий его на две равные части: в одной находятся элементы, которые
не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но
если это слишком сложно, используйте метод сортировки, который не
рассматривался на уроках (сортировка слиянием также недопустима).
"""
import random


def generator_array(m):
    size = m * 2 + 1
    min_item = 0
    max_item = 100
    array_ = [random.randint(min_item, max_item) for _ in range(size)]
    return array_


num = int(input('Введите число: '))
array = generator_array(num)
print('Исходный массив:', array, sep='\n')


def gnome_sort(array_sort):
    index = 1
    i = 0
    while i < len(array_sort) - 1:
        if array_sort[i] <= array_sort[i + 1]:
            i, index = index, index + 1
        else:
            array_sort[i], array_sort[i + 1] = array_sort[i + 1], array_sort[i]
            i -= 1
            if i < 0:
                i, index = index, index + 1
    return array

array_sorted = gnome_sort(array)
print('Отсортированный массив:', array_sorted, sep='\n')

median = len(array_sorted) // 2
print('Медиана:', array_sorted[median])

lst_less = []
lst_more = []

for k in range(len(array_sorted)):
    if k < median:
        lst_less.append(array_sorted[k])
    elif k > median:
        lst_more.append(array_sorted[k])


print('Элементы меньше медианы:', lst_less)
print('Элементы больше медианы:', lst_more)