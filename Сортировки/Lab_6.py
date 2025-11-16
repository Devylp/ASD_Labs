# №6 Посредством выбора

list = [-3, 5, 0, -8, 1, 10]

for i in range(len(list)-1):
    min = list[i]
    p = i

    # Поиск минимального элемента
    for j in range(i+1, len(list)):
        if min > list[j]:
            min = list[j]
            p = j
    
    if p != i:
        list[i], list[p] = list[p], list[i]

print(list)