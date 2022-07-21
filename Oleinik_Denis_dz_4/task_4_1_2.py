import timeit
import cProfile

"""
Задание на исходную задачу:
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры
"""

# Рекурсия + список


def func(n, i=1, result=None):
    if result is None:
        result = []
    if n > 0:
        result.append(i)
        return func(n - 1, -i / 2, result)
    return sum(result)


# print(func(20))

print(timeit.timeit('func(50)', number=1000, globals=globals()))  # 0.009882300160825253
print(timeit.timeit('func(100)', number=1000, globals=globals()))  # 0.019113499904051423
print(timeit.timeit('func(150)', number=1000, globals=globals()))  # 0.029158700024709105
print(timeit.timeit('func(200)', number=1000, globals=globals()))  # 0.03901629988104105
print(timeit.timeit('func(250)', number=1000, globals=globals()))  # 0.050384400179609656

cProfile.run('func(991)')

"""         1987 function calls (996 primitive calls) in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
    992/1    0.001    0.000    0.001    0.001 task_4_1_2.py:13(func)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
      991    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""
