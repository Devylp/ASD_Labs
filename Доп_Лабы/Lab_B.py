'''
B. Крош и удаления
'''

n, S = map(int, input().split())
result = 0

arr = [int(i) for i in input().split()]
arr_price = [int(j) for j in input().split()]

# Создаем упорядоченные пары
pairs = list(zip(arr, arr_price)) # zip упакует arr и arr_price в пары кортежей
pairs.sort() # сортируем пары по возрастанию

current_price = 0
for value, price in pairs:
    
    if current_price <= S:
        result = value

    else:
        break
    
    current_price += price


print(result)