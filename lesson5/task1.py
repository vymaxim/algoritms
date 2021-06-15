from collections import namedtuple

lst = []
manuf = namedtuple('manuf', 'name, first, second, third, fourth, profit')
x = int(input('Введите количество фирм'))
for i in range(1, x+1):
    name = input('Введите название фирмы: ')
    first = int(input('прибыль в первом квартале: '))
    second = int(input('прибыль в втором квартале: '))
    third = int(input('прибыль в третьем квартале: '))
    fourth = int(input('прибыль в четвертом квартале: '))
    profit = first + second + third + fourth
    lst.append(manuf(name, first, second, third, fourth, profit))
print(lst)

full_profit = 0
for i in lst:
    full_profit += i.profit
avg_profit = full_profit / len(lst)

lst_profit_up_avg = []
lst_profit_down_avg =[]

for i in lst:
    if i.profit < avg_profit:
        lst_profit_down_avg.append(i.name)
        # print(f'Фирма {i.name} имеет прибыль {i.profit}, которая ниже средней {avg_profit}')
    else:
        lst_profit_up_avg.append(i.name)
# for i in lst:
#     if i.profit >= avg_profit:        
#         print(f'Фирма {i.name} имеет прибыль {i.profit}, которая больше или равна средней {avg_profit}')

print(f'Фирмы с средней прибылью меньше средней: {lst_profit_down_avg}')
print(f'Фирмы с средней прибылью больше или равной средней: {lst_profit_up_avg}')
