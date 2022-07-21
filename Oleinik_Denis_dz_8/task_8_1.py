"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных
подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:
>>> func("papa")
6
>>> func("sova")
9
"""
import hashlib


def number_of_substrings(string):
    string = str(string.lower())
    hashes = set()

    for i in range(len(string) + 1):
        for j in range(i + 1, len(string) + 1):
            if string[i:j] != string:
                hashes.add(hashlib.sha1(string[i:j].encode('utf-8')).hexdigest())
    return len(hashes)


text = 'papa'
print(f'В строке {text} количество подстрок - {number_of_substrings(text)}')
