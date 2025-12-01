# Разрешение коллизии методом открытой адресации

import string
import hash_table as ht

class Hash_Table_OA(ht.Hash_Table): # OA -> Open Addressing
    
    def __init__(self, size=10):
        super().__init__(size)

        self.hash_table = [None] * self.size

    def get(self, key):
        pass

    def delete(self, key):
        pass

    def add(self, key):
        key = key.lower()
        start_hash = self.get_hash(key)

        # Линейное пробирование
        for i in range(self.size):
            index = (start_hash + i) % self.size
            current = self.hash_table[index]

            if current is None:
                self.hash_table[index] = (key, 1)
                return

    def __str__(self):
        """Форматированный вывод содержимого таблицы."""
        output = []
        output.append("Содержимое хеш-таблицы (Линейное Пробирование)")

        for i, item in enumerate(self.hash_table):
            if item is not None:
                key, count = item
                output.append(f"Индекс {i:2}: '{key}': {count}")
            else:
                output.append(f"Индекс {i:2}: None")

        return "\n".join(output)


def process_file(file_path, hash_table):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

            text_lower = text.lower()
            words = text_lower.split()

            for word in words:
                cleaned_word = word.strip(string.punctuation)

                if cleaned_word:
                    hash_table.add(cleaned_word)

        print(f"Файл '{file_path}' успешно обработан.")
        return True

    except FileNotFoundError:
        print(f"Ошибка: Входной файл по пути '{file_path}' не найден. Пожалуйста, создайте его.")
        return False
    except Exception as e:
        print(f"Произошла ошибка при обработке файла: {e}")
        return False



# Имя файла, который нужно прочитать. Убедитесь, что он существует!
INPUT_FILE_PATH = "input.txt"
RESULT_FILE_PATH = "output_oa.txt"

# Инициализация и заполнение
my_hash_table = Hash_Table_OA(size=30)  # Уменьшим размер для наглядности коллизий

# Процесс считывания файла
if process_file(INPUT_FILE_PATH, my_hash_table):
    # Вывод результата
    result_output = str(my_hash_table)

    print("Результат (Консольный вывод):")
    print(result_output)

    # Запись в файл
    with open(RESULT_FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(result_output)

    print(f"Результат работы хеш-таблицы записан в файл: '{RESULT_FILE_PATH}'")
                