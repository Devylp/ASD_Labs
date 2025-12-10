'''
Лаба №17 “Операции над БДН: поиск, добавление, удаление”

Пример: 8 (3 (1, 6 (4,7)), 10 (, 14(13,)))
'''
import Lab_17_Header as head

def main():
    print("Введите дерево в линейно-скобочной форме:")
    input_string = input("Дерево: ").strip()

    # Парсинг дерева
    root = head.build_tree_from_expression(input_string)
    print(f"\nНачальное дерево: {head.tree_to_string(root)}")

    # Основной цикл
    while True:
        head.display_menu()
        choice = input("Выберите операцию: ").strip()

        # Поиск вершины
        if choice == '1':
            try:
                value = int(input("Введите значение для поиска: "))
                if root.search(root, value):
                    print(f"Вершина со значением {value} присутствует")
                else:
                    print(f"Вершина со значением {value} отсутствует")
            except ValueError:
                print("Ошибка: введите целое число")

        # Добавление вершины
        elif choice == '2':
            try:
                value = int(input("Введите значение для добавления: "))
                root = root.insert(root, value)
                print(f"Вершина {value} добавлена")
                print(f"Текущее дерево: {head.tree_to_string(root)}")
            except ValueError:
                print("Ошибка: введите целое число")

        # Удаление вершины
        elif choice == '3':
            try:
                value = int(input("Введите значение для удаления: "))
                if root.search(root, value):
                    root = root.delete(root, value)
                    print(f"Вершина {value} удалена")
                    print(f"Текущее дерево: {head.tree_to_string(root)}")
                else:
                    print(f" Вершина {value} не найдена")
            except ValueError:
                print("Ошибка: введите целое число")

        # Показать дерево
        elif choice == '4':
            pass
            print(f"\nТекущее дерево: {head.tree_to_string(root)}")

        # Выход
        elif choice == '5':
            print("\n" + "=" * 45)
            print("ИТОГОВОЕ ДЕРЕВО:")
            print(f"{head.tree_to_string(root)}")
            print("=" * 45)
            break

        # Пользователь невнимательно прочитал условие
        else:
            print("Неверный выбор. Выберите от 1 до 5")

if __name__ == "__main__":
    main()