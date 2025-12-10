class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def search(self, node, value):
        if node is None: return None

        if node.value == value: return node

        if value < node.value:
            return self.search(node.left, value)

        else:
            return self.search(node.right, value)

    def insert(self, node, value):
        if node is None:
            return Node(value)

        if value == node.value:
            return node

        elif value < node.value:
            node.left = self.insert(node.left, value)

        elif value > node.value:
            node.right = self.insert(node.right, value)

        return node

    def find_min_node(self, node):
        if node.left is None:
            return node
        return self.find_min_node(node.left)

    def delete(self, node, value):
        if node is None: return node

        if value < node.value: node.left = self.delete(node.left, value)

        elif value > node.value: node.right = self.delete(node.right, value)

        else:
            # Случай 1: У узла нет потомков или только один потомок
            if not node.left: return node.right
            elif not node.right: return node.left

            # Случай 2: У узла два потомка
            # Находим минимальный узел в правом поддереве
            temp = self.find_min_node(node.right)
            node.value = temp.value
            node.right = self.delete(node.right, temp.value)

        return node



def build_tree_from_expression(s):
    if not s or s == ',':
        return None

    i = 0
    while i < len(s) and s[i] not in '(,)':
        i += 1

    if i == 0:
        return None

    node = Node(int(s[:i]))

    if i < len(s) and s[i] == '(':
        balance = 0
        j = i
        while j < len(s):
            if s[j] == '(':
                balance += 1
            elif s[j] == ')':
                balance -= 1
            elif s[j] == ',' and balance == 1:
                left_str = s[i + 1:j]
                right_str = s[j + 1:len(s) - 1] if s[-1] == ')' else s[j + 1:]

                node.left = build_tree_from_expression(left_str)
                node.right = build_tree_from_expression(right_str)
                break
            j += 1

    return node

def tree_to_string(root):
    if not root:
        return ""

    result = str(root.value)

    if root.left or root.right:
        result += "(" + tree_to_string(root.left) + "," + tree_to_string(root.right) + ")"

    return result

def display_menu():
    print("\n" + "=" * 45)
    print("Выберите операцию над деревом (Choose operation over tree)")
    print("=" * 45)
    print("1. Поиск вершины (Search node)")
    print("2. Добавление вершины (Insert node)")
    print("3. Удаление вершины (Remove node)")
    print("4. Показать текущее дерево (Show current tree)")
    print("5. Выход (Exit)")
    print("=" * 45)

