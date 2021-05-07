def func(x, chet=0, nechet=0):
    if x == 0:
        return f'Количетво четных цифр - {chet}, количество нечетных цифр - {nechet}'
    else:
        y = x % 10
        x = x // 10
        if y % 2 == 0:
            chet += 1
        else:
            nechet += 1
        return func(x, chet, nechet)   
        
x = int(input('x'))
a = func(x)
print(a)
