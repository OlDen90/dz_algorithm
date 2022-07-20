"""
Посчитать четные и нечетные цифры введенного натурального
числа. Например, если введено число 34560, в нем 3 четные
цифры (4, 6 и 0) и 2 нечетные (3 и 5)
"""
# https://drive.google.com/file/d/19ki-RLtNiuxUS2FVoIt2Tmt5R5k_YdY0/view?usp=sharing

x = int(input('Введите целое число: '))

even = 0    # четное
odd = 0     # не четное

while x > 0:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
    x = x // 10

print(f'Четных цифр {even}, не четных цифр {odd}')
