sum = 0
mul = 1
x = int(input('Введите трехзначное число: '))
y = x % 10
sum += y
mul *= y
x = x // 10
y = x % 10
sum += y
mul *= y
x = x // 10
y = x % 10
sum += y
mul *= y
print(f'Сумма цифр числа равна {sum}')
print(f'Произведение цифр числа равна {mul}')
