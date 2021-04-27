def func(n, x=1, sum=1, num='1'):
    if n == 1:
        return f'Сумма ряда {num} равна {sum}'
    else:
        x = - x / 2
        num += f', {x}'
        sum += x
        return func(n-1, x, sum, num)
        
x = int(input('Введите длинну последовательности'))
a = func(x)
print(a)
