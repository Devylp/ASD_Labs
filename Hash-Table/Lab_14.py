# Разрешение коллизии методом цепочек

import string
import hash_table as ht

class Hash_Table_CM(ht.Hash_Table): # CM -> Chain Method
    def __init__(self, size=10):
        super().__init__(size)

        self.hash_table = [[] for _ in range(self.size)]

    def get(self, key):
        pass

    def delete(self, key):
        pass

    # Добавление новой записи
    def add(self, key) -> None:
        key = key.lower()
        key_hash = self.get_hash(key)
        chain = self.hash_table[key_hash]

        for i, (word, count) in enumerate(chain):
            if word == key:
                chain[i] = (word, count + 1)
                return
            
        chain.append((key, 1))

    def __str__(self):
        output = []
        output.append("Содержимое хеш-таблицы (Метод Цепочек)")

        for i, chain in enumerate(self.hash_table):
            if chain:
                # Форматирование цепочки: 'слово': счетчик; 'слово2': счетчик
                chain_str = "; ".join([f"'{word}': {count}" for word, count in chain])
                output.append(f"Бакет {i:02}: {chain_str}")

        return "\n".join(output)


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

        elif symbol in "()":  # Оставляем только скобки для структуры
            tokens.append(symbol)
            i += 1

        # Удаляем "elif symbol == '=': break"

        else:  # Обработка пробелов, запятых или других символов - просто пропускаем
            i += 1

    return tokens

def process_file(file_path, hash_table):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            expression = f.read()

            # 1. Токенизация с помощью функции ОПН
            tokens = get_node_tokens(expression)

            # 2. Обработка токенов и заполнение хеш-таблицы
            for token in tokens:
                # Добавляем только числовые узлы (состоящие только из цифр)
                if token.isdigit():
                    hash_table.add(token)

        print(f"Файл '{file_path}' успешно обработан.")
        return True

    except FileNotFoundError:
        print(f"Ошибка: Входной файл по пути '{file_path}' не найден. Пожалуйста, создайте его.")
        return False
    except Exception as e:
        print(f"Произошла ошибка при обработке файла: {e}")
        return False


INPUT_FILE_PATH = "input.txt"
RESULT_FILE_PATH = "output_cm.txt"


my_hash_table = Hash_Table_CM(15)  

# Процесс считывания файла
if process_file(INPUT_FILE_PATH, my_hash_table):
    result_output = str(my_hash_table)
    print("Результат:")
    print(result_output)

    # Запись в файл
    with open(RESULT_FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(result_output)

    print(f"Результат работы хеш-таблицы записан в файл: '{RESULT_FILE_PATH}'")