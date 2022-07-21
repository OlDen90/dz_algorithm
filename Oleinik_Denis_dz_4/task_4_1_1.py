import timeit
import cProfile

"""
Задание на исходную задачу:
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры
"""

# Цикл


def func(n):
    a = 1
    b = 0
    for i in range(n):
        b += a
        a /= -2
    return b


# print(func(20))

print(timeit.timeit('func(50)', number=1000, globals=globals()))  # 0.0040213000029325485
print(timeit.timeit('func(100)', number=1000, globals=globals()))  # 0.007100600050762296
print(timeit.timeit('func(150)', number=1000, globals=globals()))  # 0.009906999999657273
print(timeit.timeit('func(200)', number=1000, globals=globals()))  # 0.012887600110843778
print(timeit.timeit('func(250)', number=1000, globals=globals()))  # 0.016472599934786558

cProfile.run('func(10_000_000)')

"""         4 function calls in 0.696 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.696    0.696 <string>:1(<module>)
        1    0.696    0.696    0.696    0.696 task_4_1_1.py:11(func)
        1    0.000    0.000    0.696    0.696 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""
