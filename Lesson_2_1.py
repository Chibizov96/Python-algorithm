# https://drive.google.com/file/d/127-FAYKFvmwb4AQJZfp3IOPmXbsFLQsi/view?usp=sharing #

print("Ноль в качестве знака операции завершит работу программы")
while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        a = int(input("a=: "))
        b = int(input("b=: "))
    if s == '+':
        print(a + b)
    elif s == '-':
        print(a - b)
    elif s == '*':
        print(a * b)
    elif s == '/':
        if b != 0:
            print(a / b)
        else:
            print("Деление на ноль!")
    else:
        print("Неверный знак операции!")
