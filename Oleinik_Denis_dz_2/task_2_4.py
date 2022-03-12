"""
Найти сумму n элементов следующего ряда
чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры
"""
# https://drive.google.com/file/d/19ki-RLtNiuxUS2FVoIt2Tmt5R5k_YdY0/view?usp=sharing

n = int(input("Введите число: "))
a = 1
b = 0
for i in range(n):
    b += a
    a /= -2
print(b)
