# Делаю задание 3-2
# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 0, 3, 4, 5 (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random
import timeit
import cProfile


def func1(n):
    min_item = -100
    max_item = 100
    array = [random.randint(min_item, max_item) for _ in range(n)]
    result = []
    for i, item in enumerate(array):
        if item % 2 == 0:
            result.append(i)
            return array, result


print(func1(5))
print(timeit.timeit('func1(10)', number=100, globals=globals()))    # 0.001003968000000001
print(timeit.timeit('func1(100)', number=100, globals=globals()))   # 0.008494274999999999
print(timeit.timeit('func1(1000)', number=100, globals=globals()))  # 0.082224767
print(timeit.timeit('func1(10000)', number=100, globals=globals()))  # 0.8335106649999999
cProfile.run('func1(100000)')
#          527043 function calls in 0.183 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.183    0.183 <string>:1(<module>)
#         1    0.000    0.000    0.182    0.182 Lesson_3_2.py:11(func1)
#         1    0.030    0.030    0.182    0.182 Lesson_3_2.py:14(<listcomp>)
#    100000    0.055    0.000    0.121    0.000 random.py:200(randrange)
#    100000    0.031    0.000    0.152    0.000 random.py:244(randint)
#    100000    0.047    0.000    0.066    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.183    0.183 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#    100000    0.009    0.000    0.009    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    127037    0.011    0.000    0.011    0.000 {method 'getrandbits' of '_random.Random' objects}


def func2(n):
    min_item = -100
    max_item = 100
    arr = []
    result = []
    i = 0
    while i < n:
        number = random.randint(min_item, max_item)
        arr.append(number)
        if number % 2 == 0:
            result.append(i)
        i += 1
    return arr, result


print(func2(5))
print(timeit.timeit('func2(10)', number=100, globals=globals()))       # 0.0010769830000001424
print(timeit.timeit('func2(100)', number=100, globals=globals()))      # 0.010491070999999907
print(timeit.timeit('func2(1000)', number=100, globals=globals()))     # 0.10479159999999998
print(timeit.timeit('func2(10000)', number=100, globals=globals()))    # 1.056830118
cProfile.run('func2(100000)')
# 677263 function calls in 0.242 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.001    0.001    0.242    0.242 <string>:1(<module>)
#        1    0.064    0.064    0.240    0.240 Lesson_3_2.py:42(func2)
#   100000    0.059    0.000    0.131    0.000 random.py:200(randrange)
#   100000    0.032    0.000    0.163    0.000 random.py:244(randint)
#   100000    0.049    0.000    0.071    0.000 random.py:250(_randbelow_with_getrandbits)
#        1    0.000    0.000    0.242    0.242 {built-in method builtins.exec}
#   150011    0.013    0.000    0.013    0.000 {method 'append' of 'list' objects}
#   100000    0.011    0.000    0.011    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   127248    0.011    0.000    0.011    0.000 {method 'getrandbits' of '_random.Random' objects}


def func3(n):
    arr = [0] * n
    even = []
    for i in range(n):
        arr[i] = int(random.random() * 200) - 100  # границы те же, реализация другая.
        if arr[i] % 2 == 0:
            even.append(i)
    return arr, even


print(func3(5))
print(timeit.timeit('func3(10)', number=100, globals=globals()))        # 0.0003997300000002646
print(timeit.timeit('func3(100)', number=100, globals=globals()))       # 0.0034892890000000065
print(timeit.timeit('func3(1000)', number=100, globals=globals()))      # 0.03506614900000038
print(timeit.timeit('func3(10000)', number=100, globals=globals()))     # 0.3567570710000001
cProfile.run('func3(100000)')
#       150123 function calls in 0.060 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.001    0.001    0.060    0.060 <string>:1(<module>)
#      1    0.046    0.046    0.058    0.058 Lesson_3_2.py:64(func3)
#      1    0.000    0.000    0.060    0.060 {built-in method builtins.exec}
#  50119    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 100000    0.009    0.000    0.009    0.000 {method 'random' of '_random.Random' objects}

# Вывод - наиболее удачным получается способ, когда необходимо сгенерировать число от 0 до 1,
# и дальше при помощи матических действий уже написать необходимые границы.
# Таким образом, версия функции номер 3 выходит самой быстрой, хоть и получилось, что все 3 зависимости линейные.
# Писал функцию, выводящую затраченное время с шагом в 10 значений(график хотел построить) - где-то все же путаюсь.
# Не принимается значение i в timeit :(
# def _picture3(n):
#     arr = [0] * n
#     i = 0
#     while i < n:
#         i+=10
#         arr.append(timeit.timeit(f"func3(i)", number=100, globals=globals()))
#     return (arr)
#
# print(_picture3(100))
