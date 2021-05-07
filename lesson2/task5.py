for i in range(33, 127, 10):
    x = ''
    for n in range(i, i+10):
        if n >= 127:
            break
        else:
            x += f'{n} - {chr(n)} '
    print(x)
