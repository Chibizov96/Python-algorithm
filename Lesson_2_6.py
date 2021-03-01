from random import random
n = round(random() * 100)
i = 1
print("Отгадайте число от 0 до 100. У вас 10 попыток")
while i <= 10:
    u = int(input(str(i) + '-я попытка: '))
    if u > n:
        print('Вы ввели слишком большое число')
    elif u < n:
        print('Вы ввели слишком маленькое число')
    else:
        print('Вы угадали с %d-й попытки' % i)
        break
    i += 1
else:
    print('Вы исчерпали 10 попыток. Было загадано', n)
