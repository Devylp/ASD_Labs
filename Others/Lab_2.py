'''
Лаба №2 "Задача об арифметическом выражении"
На вход подаётся математическое выражение. Элементы - числа. 
Операции - "+ - * /". Также есть скобочки. Окончанием выражения служит "=". 
Программа должна вывести результат выражения

Пример ввода:
2+7*(3/9)-5=

Замечание:
Программа также должна делать "проверку на дурака": 
нет деления на 0, все скобки стоят верно (см лабу №1) и т.п.
'''

def tokenize_expression(expression):
    
    tokens = []
    i = 0
    while i < len(expression):
        symbol = expression[i]
        
        if symbol.isdigit():
            num_str = ''
            while i < len(expression) and expression[i].isdigit():
                num_str += expression[i]
                i += 1
            
            tokens.append(num_str)
            
        elif symbol in "+-*/()":
            tokens.append(symbol)
            i += 1
            
        elif symbol == "=":
            break
        
        else: # Обработка пробелов или неизвестных символов
            i += 1 

    return tokens
                

# RPN - Reverse Poland Notification (ОПЗ - Обратная Польская Запись)
def convert_to_rpn(tokens_list):
    # 1. Создаем массивы для работы
    rpn_out = []
    stack_operators = []
    priority_operators = {"+": 1, "-": 1, "*": 2, "/": 2}

    # 2. Начинаем перебирать все символы token_list
    for token in tokens_list:
        
        # 2.1 Если token число
        if token.isdigit():
            rpn_out.append(token)
        
        # 2.2 Если token (
        elif token == "(":
            stack_operators.append(token)

        # 2.3 Если token оператор +-*/
        elif token in priority_operators:
            # Пока стек не пуст и на вершине стека не '(':
            while stack_operators and stack_operators[-1] != '(':
                
                # Сравниваем приоритет операторов
                if priority_operators.get(stack_operators[-1], 0) >= priority_operators[token]:
                    rpn_out.append(stack_operators.pop())
                else:
                    break
            
            stack_operators.append(token)

        # 2.4 Если token )
        elif token == ")":
            while stack_operators and stack_operators[-1] != "(":
                rpn_out.append(stack_operators.pop())
            
            if stack_operators:
                stack_operators.pop()

    # 3. Очищаем стек, если остались элементы
    while stack_operators:
        if stack_operators[-1] == '(':
             raise ValueError("Ошибка: Неправильно расставлены скобки.")
        rpn_out.append(stack_operators.pop())

    # 4. Возвращаем выходной массив
    return rpn_out
    

    
def evaluate_rpn(rpn_list):
    result = None
    stack_operand = []

    for symbol in rpn_list:

        if symbol.isdigit():
            stack_operand.append(float(symbol))

        elif symbol in "+-*/":
            # Нужно минимум два операнда для вычисления
            if len(stack_operand) < 2:
                raise ValueError(f"Ошибка ОПЗ: Недостаточно операндов для оператора '{symbol}'.")
            
            # Извлекаем операнды (ВАЖНЫЙ ПОРЯДОК! LIFO)
            # Последний пришедший — правый операнд (B)
            B = stack_operand.pop()
            # Предпоследний пришедший — левый операнд (A)
            A = stack_operand.pop()
            
            # Выполняем операцию
            if symbol == '+':
                result = A + B
            
            elif symbol == '-':
                result = A - B
            
            elif symbol == '*':
                result = A * B
            
            elif symbol == '/':
                # Проверка деления на ноль
                if B == 0:
                    raise ZeroDivisionError("Ошибка: Деление на ноль.")
                result = A / B
                
            # Помещаем результат обратно в стек
            stack_operand.append(result)

    if len(stack_operand) == 1:
        return stack_operand[0]
    else:
        # Это произойдет, если в выражении осталось слишком много операндов
        raise ValueError("Ошибка ОПЗ: Неверное выражение (слишком много операндов).")





#string_in = input("Введите математическое выражение: ")

s = "2+7*((27/9-1)-5)="
#s = "2+3*4="
s1 = tokenize_expression(s)
s2 = convert_to_rpn(s1)

print(evaluate_rpn(s2))
