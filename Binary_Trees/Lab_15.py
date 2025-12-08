"""
Структура бинарного дерева создается с помощь динамических переменных.

Лаба №15 Рекурсивные обходы (прямой, центральный, концевой)
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Прямой обход
    def pre_order(self, node):
        if node:
            print(node.value)
            self.pre_order(node.left)
            self.pre_order(node.right)
    
    # Обратный обход (концевой)
    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value)

    # Центрированный обход
    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.value)
            self.in_order(node.right)


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)

print(tree.pre_order(tree), end='\n')
print(tree.post_order(tree), end='\n')
print(tree.post_order(tree), end='\n')