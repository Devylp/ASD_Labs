# №4 Сортировка методом прочесывания

list = [23, 91, 558, 55, 13]
 
step = int(len(list) / 1.247)
swap = 0

while step > 1 or swap > 0:
    swap = 0
    i = 0
    
    while (i + step) < len(list):
        if list[i] > list[i + step]:
            list[i], list[i + step] = list[i + step], list[i]
            swap += 1
        i += 1

    if (step == 1 and swap == 0):
        break

    if step > 1:
        step = int(step / 1.247)


print(list)