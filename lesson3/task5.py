"""В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве"""

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def max_negative_num(array):
    negative_array = []
    for i in array:
        if i < 0:
            negative_array.append(i)
    if len(negative_array) == 0:
        return None
    else:
        maximum = negative_array[0]
        for i in range(len(negative_array)):
            if negative_array[i] > maximum:
                maximum = negative_array[i]
        for i in range(len(array)):
            if array[i] == maximum:
                index = i
                break
        return [maximum, index]


assert max_negative_num([1]) == None
assert max_negative_num([-1, 1, 0]) == [-1, 0]
assert max_negative_num([-1, -2, 0]) == [-1, 0]
assert max_negative_num([-2, 5, 5, -1, -1, 0]) == [-1, 3]
assert max_negative_num([-25, 20, 1, 54, -99, 34, -4, 0]) == [-4, 6]
print('Success')