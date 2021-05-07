from collections import deque


def alig_zero(x,y):
    q = abs(len(x) - len(y))
    if len(x) > len(y):
        for i in range(q):
            y.appendleft('0')
    elif len(x) < len(y):
        for i in range(q):
            x.appendleft('0')
    return [x, y]

def sum_16(x,y):
    x = alig_zero(x,y)[0]
    y = alig_zero(x,y)[1]
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    lst_sum = deque()
    k = 0 
    for i in range(1, len(x)+1):
        new_num_idx = num.index(x[-i].upper()) + num.index(y[-i].upper()) + k
        if new_num_idx > 15:
            k = new_num_idx // 16
            lst_sum.appendleft(num[new_num_idx - k * 16])
            if i == (len(x)):
                lst_sum.appendleft('1')
        else:
            lst_sum.appendleft(num[new_num_idx])
            k = 0
    return lst_sum
    
def mul_16(x,y):
    x = alig_zero(x,y)[0]
    y = alig_zero(x,y)[1]
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    lst_mun = deque()
    lst_num = deque('0')
    k = 0
    for j in range(1, len(y)+1):
        for i in range(1, len(x)+1):
            new_num_idx = num.index(x[-i].upper()) * num.index(y[-j].upper()) + k
            if new_num_idx > 15:
                k = new_num_idx // 16
                lst_mun.appendleft(num[new_num_idx-k * 16])
                if i == (len(x)):
                    lst_mun.appendleft(f'{num[k]}')
                    k = 0
            else:
                lst_mun.appendleft(num[new_num_idx])
                k = 0
        jj = j        
        while jj != 1:
            lst_mun.append('0')
            jj -= 1
        lst_num = alig_zero(lst_num, lst_mun)[0]
        lst_num = sum_16(lst_mun, lst_num)
        lst_mun = deque()
    return lst_num    

x = deque(input('Введите первое число в шестнадцатиричной системе: '))
y = deque(input('Введите первое число в шестнадцатиричной системе: '))
print(f'Сумма чисел равна {sum_16(x,y)}')        
print(f'Сумма чисел равна {mul_16(x,y)}')        

    
