n1 = int(input('Введите первое целое положительное число '))
n2 = int(input('Введите второе целое положительное число '))
n3 = int(input('Введите третье целое положительное число '))

if n1 > n2:
    if n1 < n3:
        print('Средним числом является', n1)
    elif n2 > n3:
        print('Средним числом является', n2)
    else:
        print('Средним числом является', n3)
elif n2 > n3:
    if n1 > n3:
        print('Средним числом является', n1)
    else:
        print('Средним числом является', n3)
else:
    print('Средним числом является', n2)
