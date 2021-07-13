import random

def median_search(lst, first, last):

    lst = lst.copy()
    len_centre = len(lst) // 2

    if first >= last:
        return lst[len_centre]

    centre = lst[len_centre]
    i = first
    j = last

    while i <= j:

        while lst[i] < centre:
            i += 1

        while lst[j] > centre:
            j -= 1

        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1

    if len_centre < i:
        lst[len_centre] = median_search(lst, first, j)

    elif j < len_centre:
        lst[len_centre] = median_search(lst, i, last)

    return lst[len_centre]
    
    
MIN_ITEM = 0
MAX_ITEM = 50
MIN_SIZE = 5
MAX_SIZE = 10

m = random.randint(MIN_SIZE, MAX_SIZE)
size = 2 * m + 1

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]

print(f'Массив из 2*{m}+1 = {size}  элементов:', array, sep='\n')

median = median_search(array, 0, len(array) - 1)
print(f'Медиана: {median}')    