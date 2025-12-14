'''
C. Сумма и делимость(сложная версия)
'''

n, k = map(int, input().split())

arr = [int(i) for i in input().split()]

result = 0
remains_count = [0]*k
for x in arr:
    current = x%k
    needed_mod = (k - current)%k

    result += remains_count[needed_mod]
    
    remains_count[current] += 1
    print(x, remains_count)


#print(result)

'''
Идея алгоритма состоит в том, чтобы ((a(i) + a(j)) mod k) = ...
1. Равнялось нулю если (a(i)mod k) = 0 и (a(j)mod k) = 0
2. Или k, если сумма (a(i)mod k) + (a(j)mod k) = k в совокупности

В случае 2 мы используем needed_mod, чтобы дополнить до необходимого случая (1 или 2)

remains_count хранит информацию о соседях. Например для числа 5 у нас remains_count = [2, 2]
remains_count[1] = 2, то есть это говорит о том, что ранее (числа 3 и 1) нашли себе пару, следовательно
число 5 нашло себе в пару 3 и 1 ((5, 3) и (5, 1)), следовательно плюс две пары

[3, 2, 1, 4, 5]
чтобы 1 + r(j) = 2, 2 = 0 or 2
нужно (2 - r(j)) mod 2 == 1 or r(j) == 1
3 % 2 = 1
nd = (2 - 3)%2 = 1

2 % 2 = 0
nd = (2 - 2)%2 = 0

...

'''