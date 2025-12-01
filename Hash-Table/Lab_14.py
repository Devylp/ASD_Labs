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


def process_file(file_path, hash_table):
    """Считывает файл, очищает его от пунктуации и заполняет хеш-таблицу"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

            # Приводим текст к нижнему регистру
            text_lower = text.lower()

            # Разбиваем на слова (по пробельным символам)
            words = text_lower.split()

            for word in words:
                # Очищаем каждое слово от знаков препинания в начале и конце
                cleaned_word = word.strip(string.punctuation)

                # Добавляем слово в хеш-таблицу, если оно не пустое
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
RESULT_FILE_PATH = "output_cm.txt"

# Инициализация и заполнение
my_hash_table = Hash_Table_CM(size=30)

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
            

