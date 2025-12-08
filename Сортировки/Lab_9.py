"""№9 Пирамидальная (heap sort)

Термины:
Полное бинарное дерево (куча) - это стуктура данных типа дерево, где
у каждого узла есть два потомка. Полным называется дерево, если оно строится
слево-направо (без "дырок")

Шаги:
1. Небходимо построить max-кучу (функция Create_MAX_Heap)
2. Отсортировать полученную кучу (функция HeapSort)
"""

arr = [7, 8, 0, -98, 124, 2, 4, 6, 4, -1]
lenght = len(arr)

# функция восстанавливает свойство кучи, то есть родитель всегда больше или равен своему дочерему узлу
def Create_MAX_Heap(i,end, array): # end = len(array)
    largest = i # родитель в поддереве
    left_child = i*2 + 1
    right_child = i*2 + 2

    # Условия гарантируют, что элементы не покинут кучу
    if left_child < end and array[largest] < array[left_child]:
        largest = left_child
    
    if right_child < end and array[largest] < array[right_child]:
        largest = right_child
            
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        Create_MAX_Heap(largest,end, array)

    return array


def HeapSort(heap):
    lenght_heap = len(heap)
    
    for i in range(lenght_heap//2-1,-1,-1):
        Create_MAX_Heap(i,lenght_heap, heap)
        
    j = lenght_heap
    for i in range(lenght_heap-1,-1,-1):
        heap[0], heap[i] = heap[i], heap[0]
        j-=1
        Create_MAX_Heap(0,j, heap)
            
                
    return heap


print(HeapSort(arr))

#print(Create_MAX_Heap(0, lenght, arr))
# Было: [7, 8, 0, -98, 124, 2, 4, 6, 4, -1]
# Стало: [8, 124, 0, -98, 7, 2, 4, 6, 4, -1]