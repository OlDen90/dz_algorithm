# https://drive.google.com/file/d/1vu0aaiBaaRWn0JXMEVwga_kWgNd8LtQe/view?usp=sharing

n = int(input('Введите число от 100 до 999 - '))

c = n % 10
b = n % 100 // 10
a = n // 100

s = a + b + c
m = a * b * c

print('Сумма ваших чисел -', s)
print('Произведение ваших чисел -', m)


