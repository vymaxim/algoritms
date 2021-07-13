import random


def merge_sort(arr):

    def merge(first, second):
        lst = []
        i, j = 0, 0

        while i < len(first) and j < len(second):

            if first[i] < second[j]:
                lst.append(first[i])
                i += 1

            else:
                lst.append(second[j])
                j += 1

        lst.extend(first[i:] if i < len(first) else second[j:])

        return lst

    def div_half(lst):

        if len(lst) == 1:
            return lst

        elif len(lst) == 2:
            if lst[0] <= lst[1]:
                return lst
            else:
                return lst[::-1]

        else:
            return merge(div_half(lst[:len(lst)//2]), div_half(lst[len(lst)//2:]))

    return div_half(arr)


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print('Массив:', array, sep='\n')
array = merge_sort(array)
print('Отсортированный массив:', array, sep='\n')