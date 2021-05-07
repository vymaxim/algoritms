def calc(a,b,operation):
    calc = {"+": a + b, "-": a - b, "*": a * b, "/": a / b}
    return calc[operation]
    
while True:
    operation = input('Введите операцию +,-,*,/ или 0 для выхода')
    if operation != "0":
        a = int(input('Введите число а'))
        b = int(input('Введите число b'))
        calc = calc(a,b,operation)
        print(calc)
    else:
        print(f'Вы вышли из калькулятора')    
        break
        

