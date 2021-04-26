a = int(input('введите число a'))
b = int(input('введите число b'))
c = int(input('введите число c'))
if a < b < c or c < b < a:
    print(f'среднее число {b}')
elif b < a < c or c < a < b:
    print(f'среднее число {a}')
else:
    print(f'среднее число {c}')
