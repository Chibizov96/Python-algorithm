# Делаю задание 3-2
# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 0, 3, 4, 5 (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random
import timeit
import sys

def func1(n):
    min_item = -100
    max_item = 100
    array = [random.randint(min_item, max_item) for _ in range(n)]
    result = []
    byte_sum = 0
    for i, item in enumerate(array):
        if item % 2 == 0:
            result.append(i)
    # Использовал данный способ реализации
    # Необходимо добавлять переменные вручную в случае изменения программы
    for item in (min_item, max_item, array, result, i, n):
        byte_sum += sys.getsizeof(item)
    return array, result, byte_sum


print('*'*50)
print('Первая программа')
print(func1(10))
print(timeit.timeit('func1(10000)', number=100, globals=globals()))  # 0.8335106649999999
print('*'*50)


def func2(n):
    min_item = -100
    max_item = 100
    arr = []
    result = []
    i = 0
    byte_sum = 0
    while i < n:
        number = random.randint(min_item, max_item)
        arr.append(number)
        if number % 2 == 0:
            result.append(i)
        i += 1
    # Необходимо добавлять переменные вручную в случае изменения программы
    for item in (min_item, max_item, arr, result, i, n, number):
        byte_sum += sys.getsizeof(item)
    return arr, result, byte_sum


print('*'*50)
print('Вторая программа')
print(func2(10))
print(timeit.timeit('func2(10000)', number=100, globals=globals()))    # 1.056830118
print('*'*50)


def func3(n):
    arr = [0] * n
    even = []
    byte_sum = 0
    for i in range(n):
        arr[i] = int(random.random() * 200) - 100  # границы те же, реализация другая.
        if arr[i] % 2 == 0:
            even.append(i)
    # Необходимо добавлять переменные вручную в случае изменения программы
    for item in (arr, even, i, n):
        byte_sum += sys.getsizeof(item)
    return arr, even, byte_sum


print('*'*50)
print('Третья программа')
print(func3(10))
print(timeit.timeit('func3(10000)', number=100, globals=globals()))    # 0.34693318799999995
print('*'*50)


# Прошлый вывод #
# Вывод - наиболее удачным получается способ, когда необходимо сгенерировать число от 0 до 1,
# и дальше при помощи матических действий уже написать необходимые границы.
# Таким образом, версия функции номер 3 выходит самой быстрой, хоть и получилось, что все 3 зависимости линейные.

# Новый вывод #
# Программа номер три не только получилась самой быстрой, но и по памяти ни разу не догнала ни одну из программ.
# Это происходит благодаря снижению колчества переменных при написании программы:
# в третьей программе отсутствуют переменные min_item и max_item
# Наиболее расточительной и к ресурсам и ко времени получилась вторая программа
# Версия ос x64, Python 3.8.6