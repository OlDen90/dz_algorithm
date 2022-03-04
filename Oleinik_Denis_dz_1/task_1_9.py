"""
Вводятся три разных числа. Найти, какое из них
является средним (больше одного, но меньше другого)
"""
# https://drive.google.com/file/d/1vu0aaiBaaRWn0JXMEVwga_kWgNd8LtQe/view?usp=sharing

a = float(input('Введите число №1: '))
b = float(input('Введите число №2: '))
c = float(input('Введите число №3: '))

if b < a < c or c < a < b:
    print(a)
elif a < b < c or c < b < a:
    print(b)
else:
    print(c)
