"""
В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9
"""

range_1_min = 2
range_1_max = 9
range_2_min = 2
range_2_max = 99


for i in range(range_1_min, range_1_max + 1):
    counter = 0
    for j in range(range_2_min, range_2_max + 1):
        if j % i == 0:
            counter += 1
    print(f'Числу {i} кратно {counter} чисел(ла)')


# Для проверки количества чисел:

# range_1_min = 2
# range_1_max = 9
# range_2_min = 2
# range_2_max = 99
#
#
# for i in range(range_1_min, range_1_max + 1):
#     print(f'Числу {i} кратны: ')
#     for j in range(range_2_min, range_2_max + 1):
#         if j % i == 0:
#             print(j, end=' ')
#     print()