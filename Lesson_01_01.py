# https://drive.google.com/file/d/1BmWpoz6MKdRZw4Dv6urC-K7O78-v0io1/view?usp=sharing #

n = int(input("Введите трехзначное положительное число: "))

d1 = n % 10
d2 = n % 100 // 10
d3 = n // 100

print("Сумма цифр числа:", d1 + d2 + d3)
print("Произведение цифр числа:", d1 * d2 * d3)
