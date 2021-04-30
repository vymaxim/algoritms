"""Определить, какое число в массиве встречается чаще всего."""
import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def check_num_max(array):

    maximum = 0
    for j in set(array):
        check = 0
        for i in range(len(array)):
            if array[i] == j:
                check += 1
        if check > maximum:
            maximum = check
            maximum_num = j
    return maximum_num


assert check_num_max([1]) == 1
assert check_num_max([1, 2]) == 1
assert check_num_max([1, 2, 1]) == 1
print('Success')