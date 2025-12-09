# №10 Слиянием

# Работаем по принципу "Разделяй и властвуй"
# То есть, разбиваем рекурсивно исходный массив до атомарных единиц и в
# merge_two_list собираем финальный массив

# Вспомогательная функция для слияния двух списков (из рекурсии (*))
def merge_two_list(a, b):
    result_merge = []
    i = j = 0

    # Проверяем, достигли ли указатели конца массивов
    while i < len(a) and j < len(b):
        # Сортируем слиянием
        
        if a[i] < b[j]:
            result_merge.append(a[i])
            i += 1
        else:
            result_merge.append(b[j])
            j += 1
    
    # Рассматриваем случаи, когда какой-то указатель не дошел до конца массива
    # Просто добавляем остаток к result_merge
    
    if i < len(a):
        result_merge += a[i:]

    if j < len(b):
        result_merge += b[j:]
    
    return result_merge

def merge_sort(array):
    # Рекурсия (*)

    # Рекурсивное условие выхода (**)
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    
    # Делим исходный массив пополам до тех пор, пока не сработает (**)
    left_piece = merge_sort(array[:mid])
    right_piece = merge_sort(array[mid:])

    # Возврат результат слияния двух отсортированных списков
    return merge_two_list(left_piece, right_piece)



print(merge_sort([7, 5, 2, 3, 9, 8, 6, 1, 19, 10, 132, 2, 89, 0, -6, -98]))
# 7, 5, 2, 3, 9, 8, 6, 1, 19, 10, 132, 2, 89, 0, -6, -98