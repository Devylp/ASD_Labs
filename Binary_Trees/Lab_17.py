'''
Лаба №17 “Операции над БНП: поиск, добавление, удаление”
Дерево вводится в программу в формате линейно-скобочной записи.
Затем появляется меню, в котором доступна операция добавления, удаления и поиска вершины БДП.
После выполнения операции программа должна возвращаться снова в меню.
При выходе их него до завершения программы на экран должно быть выведено
БДН любым способом (в виде линейно-скобочной записи или в графической форме).

Пример: 8 (3 (1, 6 (4,7)), 10 (, 14(13,)))
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def search(self):
        pass

    def add(self):
        pass

    def delete(self):
        pass

def get_node_tokens(expression):
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

        elif symbol in "()":
            i += 1

        else:
            i += 1

    return tokens

def display_menu() -> None:
    pass

#print(get_node_tokens("8 (3 (1, 6 (4,7)), 10 (, 14(13,)))"))
# -> ['8', '3', '1', '6', '4', '7', '10', '14', '13'] без tokens.append(symbol)
# -> ['8', '(', '3', '(', '1', '6', '(', '4', '7', ')', ')', '10', '(', '14', '(', '13', ')', ')', ')'] с tokens.append(symbol)