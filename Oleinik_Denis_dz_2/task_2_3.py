"""
Сформировать из введенного числа обратное по порядку
входящих в него цифр и вывести на экран. Например,
если введено число 3486, то надо вывести число 6843
"""
# https://drive.google.com/file/d/19ki-RLtNiuxUS2FVoIt2Tmt5R5k_YdY0/view?usp=sharing


def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
a = str(input('Введите строку: '))
print(reverse(a))

# -----------------------------------

# n = int(input('Введите число: '))
# m = 0
# while n > 0:
#     m = m * 10 + n % 10
#     n = n // 10
# print(m)

# -----------------------------------

# a = input('Введите число: ')
# print(a[::-1])