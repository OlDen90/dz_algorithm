"""
Вывести на экран коды и символы таблицы ASCII,
начиная с символа под номером 32 и заканчивая
127-м включительно. Вывод выполнить в табличной
форме: по десять пар "код-символ" в каждой строке.
"""
# https://drive.google.com/file/d/19ki-RLtNiuxUS2FVoIt2Tmt5R5k_YdY0/view?usp=sharing

count = 1

for i in range(32, 128):
    symbol = f'{i}-{chr(i)}\t'
    if count % 10 == 0:
        print(symbol, end='\n')
    else:
        print(symbol, end='')
    count += 1
