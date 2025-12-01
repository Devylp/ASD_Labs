# №11 Быстрая сортировка

list = [2, -1, 8, 0, 7, 76, 1, 0 -23]


def quick_sort(array):
    # Условие выхода и рекурсии
    if len(array) <= 1:
        return array

    # Создаем опорный элемент
    pivot = array[(len(array)//2)]

    left = [i for i in array if i<pivot] # Все элементы меньше pivot
    center = [i for i in array if i == pivot] # Центр массива (он же просто pivot)
    right = [i for i in array if i>pivot] # Все элементы больше pivot

    return quick_sort(left) + center + quick_sort(right)

print(quick_sort(list))


