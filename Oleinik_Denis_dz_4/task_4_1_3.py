import timeit
import cProfile

"""
Задание на исходную задачу:
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры
"""

# Создание списка


def func(n):
    l = []
    for i in range(n):
        if i%2 ==0:
            l.append(1/2**i)
        else:
            l.append(-(1/2**i))
    return sum(l)


# print(func(20))

print(timeit.timeit('func(50)', number=1000, globals=globals()))  # 0.015990399988368154
print(timeit.timeit('func(100)', number=1000, globals=globals()))  # 0.040091299917548895
print(timeit.timeit('func(150)', number=1000, globals=globals()))  # 0.06690649990923703
print(timeit.timeit('func(200)', number=1000, globals=globals()))  # 0.09864199999719858
print(timeit.timeit('func(250)', number=1000, globals=globals()))  # 0.13003099989145994

cProfile.run('func(100_000)')

"""         100005 function calls in 9.233 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    9.233    9.233 <string>:1(<module>)
        1    9.225    9.225    9.233    9.233 task_4_1_3.py:13(func)
        1    0.000    0.000    9.233    9.233 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
   100000    0.008    0.000    0.008    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""