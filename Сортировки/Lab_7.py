# №7 Шелла (улучшенный вариант сортировки вставками)
# В отличие от классической сортировки вставками, здесь мы сравниваем элементы
# на расстоянии (есть схожесть с сортировкой прочесыванием), но в отличие от
# расчески скорость сортировки Шелла составляет (N*Log(N)^2), а худшее (N^2). 
# Скорость расчески составляет (N*LogN) а в худшем (N^2)

def Shell_sort(array):
    gap = len(array) // 2

    while gap > 0:
        for i in range(gap, len(array)):
            
            for j in range(i, 0, -gap):
                if array[j] < array[j-gap]:
                    array[j], array[j-gap] = array[j-gap], array[j]   

        gap //= 2

    return array

list = [64, 34, 25, 12, 22, 11, 90, 5, 53, 1]
print(Shell_sort(list))