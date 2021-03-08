# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

start_num = 2
end_num = 99
start_div = 2
end_div = 9

# вариант 1 без "массивов"
for i in range(start_div, end_div + 1):
    frequency = 0
    for j in range(start_num, end_num + 1):
        if j % i == 0:
            frequency += 1
    print(f'Числу {i} кратно {frequency} чисел')
