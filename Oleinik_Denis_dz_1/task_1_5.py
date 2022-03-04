"""
Пользователь вводит две буквы. Определить, на каких
местах алфавита они стоят, и сколько между ними находится букв
"""
# https://drive.google.com/file/d/1vu0aaiBaaRWn0JXMEVwga_kWgNd8LtQe/view?usp=sharing

                                # Проверка на буквах 'a' и 'd'
a = ord(input('1я буква: '))    # 97
b = ord(input('2я буква: '))    # 100
a = a - ord('a') + 1            # 97-97+1
b = b - ord('a') + 1            # 100-97+1

# print(a)
# print(b)

print(f'позиции: {a} и {b}')
print('Между буквами символов:', abs(a-b)-1) # 97-100-1


