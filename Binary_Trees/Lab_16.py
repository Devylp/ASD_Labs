"""
Структура бинарного дерева создается с помощь динамических переменных.

Лаба №16 “Не рекурсивный прямой обход” (реализуется с помощью стека).
В качестве выходных данных формируется строка обхода.
"""

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def nonRec_pre_order(self, node):
        if node.value is None:
            return ""

        stack = [node]
        result_arr = []
        
        while stack:
            current = stack.pop()
            result_arr.append(str(current.value))

            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)

        return "".join(result_arr)




tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)

print(tree.nonRec_pre_order(tree))