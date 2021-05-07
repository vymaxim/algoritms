def func(x, revnum=''):
    if x == 0:
        return f'Число обратное первоначальному - { int(revnum)}'
    else:
        y = x % 10
        x = x // 10
        revnum += str(y)
        return func(x, revnum)  
        
x = int(input('Введите любое число'))
a = func(x)
print(a)
