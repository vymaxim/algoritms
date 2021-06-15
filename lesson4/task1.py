"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""
import random
import timeit
import cProfile
from operator import itemgetter


def array(SIZE, MIN_ITEM, MAX_ITEM):
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    return array

def switch_min_max(array):
    min_index = 0
    max_index = 0
    minimum = array[0]
    maximum = array[0]
    for i in range(len(array)):
        if array[i] < minimum:
            minimum = array[i]
            min_index = i
        if array[i] > maximum:
            maximum = array[i]
            max_index = i
    array[min_index], array[max_index] = array[max_index], array[min_index]
    return array


def sw(array):
    # arr1 = sorted(array)
    swapped = True
    arr1 = array
    while swapped:
        swapped = False
        for i in range(len(arr1) - 1):
            if arr1[i] > arr1[i + 1]:
                arr1[i], arr1[i+1] = arr1[i+1], arr1[i]
                swapped = True
    array[array.index(arr1[0])], array[array.index(arr1[len(arr1)-1])] = array[array.index(arr1[len(arr1)-1])], array[array.index(arr1[0])]
    return array


def swap1(array):
    array[:] = map(lambda x: min(array) if x == max(array) else max(array) if x == min(array) else x, array)
    return array


print(f"Функция switch_min_max \n\n{cProfile.run('switch_min_max(array(80,-99,99))')}")
print(f"Функция swap1 \n\n{cProfile.run('swap1(array(80,-99,99))')}")
print(f"Функция sw \n\n{cProfile.run('sw(array(80,-99,99))')}")


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


arr_x = []
arr_y, arr_y2, arr_y3 = [], [], []

for x in range (1, 200, 5):
    y = round(timeit.timeit(f'switch_min_max(array({x},-99,99))', number=100, globals=globals()), 5)
    y2 = round(timeit.timeit(f'swap1(array({x},-99,99))', number=100, globals=globals()), 5)
    y3 = round(timeit.timeit(f'sw(array({x},-99,99))', number=100, globals=globals()), 5)
    arr_x.append(x)
    arr_y.append(y)
    arr_y2.append(y2)
    arr_y3.append(y3)


df = pd.DataFrame(
    {
        "x": arr_x,
        "timeit switch_min_max": arr_y,
        "timeit swap1": arr_y2,
        "timeit sw": arr_y3
    })
print(df)

fig, ax = plt.subplots(figsize=(12, 6))

ax.set_title("switch_min_max", fontsize=16)
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("timeit", fontsize=14)
ax.scatter(arr_x, arr_y, c="red",  marker="D", linewidths=3, alpha=0.3, s=100, label ='switch_min_max')
ax.scatter(arr_x, arr_y2, c="green",  marker="*", linewidths=3, alpha=0.3, s=100, label ='swap1')
ax.scatter(arr_x, arr_y3, c="yellow",  marker="P", linewidths=3, alpha=0.3, s=100, label ='sw')

ax.legend(title='function: ')
ax.grid(True)
plt.show()


"""
timeit result

i     x  timeit switch_min_max  timeit swap1  timeit sw
0     1                0.00033       0.00029    0.00029
1     6                0.00088       0.00137    0.00159
2    11                0.00190       0.00245    0.00264
3    16                0.00255       0.00337    0.00456
4    21                0.02075       0.00521    0.00683
5    26                0.00344       0.00692    0.01278
6    31                0.00675       0.01449    0.01588
7    36                0.00479       0.01039    0.01691
8    41                0.00654       0.01266    0.02300
9    46                0.00601       0.01436    0.02720
10   51                0.00732       0.02457    0.03260
11   56                0.00695       0.02201    0.03838
12   61                0.00762       0.03237    0.04527
13   66                0.00833       0.02545    0.05127
14   71                0.01019       0.04291    0.09524
15   76                0.01396       0.03593    0.09699
16   81                0.01119       0.04691    0.07612
17   86                0.01097       0.04317    0.10373
18   91                0.01252       0.05041    0.10824
19   96                0.01294       0.05918    0.11309
20  101                0.01833       0.06393    0.13182
21  106                0.01466       0.06230    0.14239
22  111                0.01387       0.06606    0.14198
23  116                0.01424       0.06604    0.16759
24  121                0.01610       0.07723    0.19148
25  126                0.01680       0.10215    0.21678
26  131                0.01703       0.11100    0.20739
27  136                0.01788       0.09456    0.22481
28  141                0.01817       0.10395    0.24003
29  146                0.02015       0.10627    0.25270
30  151                0.02131       0.12588    0.31043
31  156                0.01962       0.13688    0.31036
32  161                0.02350       0.13584    0.32556
33  166                0.02823       0.15478    0.34279
34  171                0.02507       0.18106    0.45075
35  176                0.02925       0.18673    0.46366
36  181                0.03037       0.19420    0.41547
37  186                0.03710       0.17954    0.43573
38  191                0.02542       0.17476    0.47022
39  196                0.02942       0.20967    0.45125"""
