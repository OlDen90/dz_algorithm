"""
Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.
"""
# https://drive.google.com/file/d/1vu0aaiBaaRWn0JXMEVwga_kWgNd8LtQe/view?usp=sharing

n = int(input('Введите номер буквы в алфавите: '))
n = ord('a') + n - 1
print('Ваша буква', chr(n))
