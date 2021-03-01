def recur_sum(n):
    if n <= 1:
        return n
    else:
        return n + recur_sum(n - 1)
num=int(input("Введите крайний член прогрессии: "))
print("Сумма всех членов от 1 до " + str(num) + " равна " + str(recur_sum(num)))
print("n*(n+1)/2 равно "+ str(num*(num+1)/2))
if recur_sum(num) == (num*(num+1)/2):
    print("Значения равны")
