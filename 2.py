from copy import copy
def copy_sort(array):
    array = [5, 1, 4, 3, 5, 6, 8, 2]
    copy = array[:]
    sorted_copy = []
    return sorted_copy

    while len(copy) > 0:
      minimum: int = 0
    for i in range(1, len(copy)):
        if copy[i] < copy[minimum]:
                minimum = i
                sorted_copy.append(copy[minimum])
                copy.pop(minimum)


    print('\tУдаляем', copy[minimum],'\tИз', copy )
    print('Сортировка с копирование...\nМассив:', array)
    print('Копия', copy_sort(array))
    print('Массив', array)



