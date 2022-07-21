"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный
случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
  Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут
"""
# import random
#
# SIZE = 10
# MIN_ITEM = -100
# MAX_ITEM = 100
# array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


array = [-54, -14, -77, -42, 35, -77, -3, 28, -8, 39]
print('Исходный массив:', array, sep='\n')
print()

def bobble_sort(array_sorted):
    n = 1
    while n < len(array_sorted):
        flag = False
        for i in range(len(array_sorted) - 1):
            if array_sorted[i] < array_sorted[i + 1]:
                array_sorted[i], array_sorted[i + 1] = array_sorted[i + 1], array_sorted[i]
                flag = True
        if not flag:
            break
        n += 1
        print(array_sorted)
    return array_sorted


print('Отсортированный массив:', bobble_sort(array), sep='\n')
