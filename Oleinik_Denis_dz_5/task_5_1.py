from collections import defaultdict

n = int(input('Введите количество предприятий: '))

my_dict = defaultdict(list)
print(my_dict)
for i in range(1, n + 1):
    firm = input(f'Введите название предприятия {i}: ')
    my_dict[firm].append(i)
    counter = 0
    for j in range(1, 5):
        quarter = float(input(f'Введите прибыль предприятия за {j}й квартал: '))
        counter += quarter
    my_dict[firm] = counter
print(my_dict)

counter = 0
for i in my_dict:
    counter += my_dict[i]
print(counter)

average = counter / n
more = []
less = []
for i in my_dict:
    if my_dict[i] >= average:
        more.append(i)
    elif my_dict[i] < average:
        less.append(i)

print(f'Средняя прибыль всех предприятий: {average}')
print('Предприятия чья прибыль выше среднего:')
print(*more, sep=', ')
print('Предприятия чья прибыль ниже среднего:')
print(*less, sep=', ')


"""Подскажите, как правильно выводить на печать в одну строку с текстом перечень предприятий чтобы он был без [] и ''?
Т.е. при таком выводе: 
print(f'Предприятия чья прибыль выше среднего: {more}')
получается:
Предприятия чья прибыль выше среднего: ['Предприятие один', 'Предприятие два', 'Предприятие три'],
а хочется сделать:
Предприятия чья прибыль выше среднего: Предприятие один, Предприятие два, Предприятие три
"""


# Вариант без модуля collections

# n = int(input('Введите количество предприятий: '))
#
# my_dict = {}
# for i in range(1, n + 1):
#     firm = input(f'Введите название предприятия {i}: ')
#     my_dict[firm] = 0
#     counter = 0
#     for j in range(1, 5):
#         quarter = float(input(f'Введите прибыль предприятия за {j}й квартал: '))
#         counter += quarter
#     my_dict[firm] = counter
# print(my_dict)
#
# counter = 0
# for i in my_dict:
#     counter += my_dict[i]
# print(counter)
#
# average = counter / n
# more = []
# less = []
# for i in my_dict:
#     if my_dict[i] >= average:
#         more.append(i)
#     elif my_dict[i] < average:
#         less.append(i)
#
# print(f'Средняя прибыль всех предприятий: {average}')
# print('Предприятия чья прибыль выше среднего:')
# print(*more, sep=', ')
# print('Предприятия чья прибыль ниже среднего:')
# print(*less, sep=', ')

