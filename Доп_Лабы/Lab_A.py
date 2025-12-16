'''
A. Крош и строка
'''

n = int(input("").strip())
input_string = input("").strip()
result_arr = [] # массив для хранения предыдущих значении input_string (на основе стека)

top = -1 # значение -1 указывает на пустоту result_arr
for current_symbol in input_string:
    # Если result_arr не пустой и current_symbol совпадает с предыдущим (result_arr[top])
    if top >= 0 and result_arr[top] == current_symbol:
        result_arr.pop()
        top -= 1

    else:
        result_arr.append(current_symbol)
        top += 1


print(1 if top == -1 else 0)


'''
Работа на примере abccba (n = 6)
i| c  t  r[t(i)]   r
1| a -1  []     [a]     # a != ''
2| b  1  [a]    [a, b]  # b != a
3| c  2  [b]    [a, b, c] # c != b
4| c  1  [c]    [a, b]  # c == c удаляем пару из result_arr
5| b  0  [b]    [a]     # b == b удаляем пару из result_arr
6| a -1  [a]    []      # a == a удаляем пару из result_arr

output >> top == -1 # значит, что все необходимые пары удалены

Примечание:
Решить данную задачу можно было бы при помощи двух указателей,
но сложно бы упала до О(N^2) из-за наличия двух циклов for
'''
