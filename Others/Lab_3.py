'''
Лаба №3 "Задача о простых множителях"
На вход дается одно число х, нужно вывести все числа от 1 до х, 
удовлетворяющие условию: 

3^K * 5^L * 7^M = x<sub>i<sub>

где K, L, M - натуральные числа или могут быть равны 0.
'''

def check_prime_factors(number):
    if number == 0:
        return False
        
    temp_number = number
    K, L, M = 0, 0, 0 

    
    while (temp_number % 3 == 0) or (temp_number % 5 == 0) or (temp_number % 7 == 0):
        
        if temp_number % 3 == 0:
            K += 1
            temp_number //= 3

        if temp_number % 5 == 0:
            L += 1
            temp_number //= 5
        
        if temp_number % 7 == 0:
            M += 1
            temp_number //= 7
        

    # остается 1. (т.е. в нем нет других простых множителей)
    is_valid = (temp_number == 1)
    
    return K, L, M, is_valid



result = {} # Будем хранить в виде: num: "3^K * 5^L * 7^M"

x = int(input("Введите значение x: "))


for num in range(1, x+1):
    K, L, M, is_valid = check_prime_factors(num)
    
    if is_valid:
        result[num] = f"3^{K} * 5^{L} * 7^{M}"

# Выводим результат в нужном формате
print("\nЧисла, удовлетворяющие условию (от 1 до {}):".format(x))
for num, formula in result.items():
    print(f"{num}: {formula}")
