import sys


def swap_min_max_idx(array):
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
    
    sm = 0
    sm += sys.getsizeof(array)
    sm += sys.getsizeof(min_index)
    sm += sys.getsizeof(max_index)
    sm += sys.getsizeof(minimum)
    sm += sys.getsizeof(maximum)
    
    print(f'Количество затраченной памяти {sm} в решаемой задачи функцией swap_min_max_idx')
    
    return array


def swap_while(array):

    swapped = True
    arr1 = array
    while swapped:
        swapped = False
        for i in range(len(arr1) - 1):
            if arr1[i] > arr1[i + 1]:
                arr1[i], arr1[i+1] = arr1[i+1], arr1[i]
                swapped = True
    array[array.index(arr1[0])], array[array.index(arr1[len(arr1)-1])] = array[array.index(arr1[len(arr1)-1])], array[array.index(arr1[0])]
    
    sm = 0
    sm += sys.getsizeof(array)
    sm += sys.getsizeof(swapped)
    sm += sys.getsizeof(arr1)
    
    print(f'Количество затраченной памяти {sm} в решаемой задачи функцией swap_while')
    
    return array
    
def swap(array):

    array[array.index(min(array))], array[array.index(max(array))] = array[array.index(max(array))], array[array.index(min(array))]
    
    
    sm = 0
    sm += sys.getsizeof(array)
    sm += sys.getsizeof(array.index(max(array)))
    sm += sys.getsizeof(array.index(min(array)))
    
    print(f'Количество затраченной памяти {sm} в решаемой задачи функцией swap')
    
    return array
    
    
array = [234, 23, 5, 34, 0]

swap_min_max_idx(array)
swap_while(array)
swap(array)