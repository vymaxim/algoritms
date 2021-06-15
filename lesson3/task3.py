"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""
import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]



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

assert switch_min_max([-1, 1]) == [1, -1]
assert switch_min_max([1, 2, 3, 4, 5]) == [5, 2, 3, 4, 1]
assert switch_min_max([1, -5, 3, 4, 66]) == [1, 66, 3, 4, -5]
assert switch_min_max([-1, -2, -3, -4, 0]) == [-1, -2, -3, 0, -4]
print('Success')



