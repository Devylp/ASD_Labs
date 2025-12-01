# Разрешение коллизии методом цепочек

import string
import hash_table as ht

class Hash_Table_CM(ht.Hash_Table): # CM -> Chain Method
    def __init__(self, size=10):
        super().__init__(size)

        self.hash_table = [[] for _ in range(self.size)]
    
    # Добавление новой записи
    def add(self, key, value) -> None:
        key = key.lower()
        key_hash = self.get_hash(key)
        chain = self.hash_table[key_hash]

        for i, (word, count) in enumerate(chain):
            if word == key:
                chain[i] = (word, count + 1)
                return
            
        chain.append((key, 1))



def process_file_and_populate_hash_table(file_path, hash_table):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            
            # 1. Приводим к нижнему регистру
            text_lower = text.lower()
            
            # 2. Очищаем текст от переносов строки и прочих пробельных символов 
            # и разбиваем на слова по пробелам
            words = text_lower.split()
            
            for word in words:
                # 3. Удаляем знаки препинания в начале и конце каждого слова
                cleaned_word = word.strip(string.punctuation)
                
                if cleaned_word: 
                    hash_table.put(cleaned_word)
                    
        print(f"Файл '{file_path}' успешно обработан.")
        
    except FileNotFoundError:
        print(f"Ошибка: Файл по пути '{file_path}' не найден.")

# --- УПРОЩЕННЫЙ БЛОК ВЫПОЛНЕНИЯ И ЗАПИСИ ---
def main():
    TEST_FILE_PATH = "input.txt"
    RESULT_FILE_PATH = "output.txt"
    
    # Создание тестового файла (упрощенный блок)
    sample_text = """
    Раз, два, три. Коллизии, коллизии, коллизии. 
    Банан, Яблоко, Арбуз. Раз-два-три.
    """
    with open(TEST_FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(sample_text)
        
    # Инициализация и заполнение
    my_hash_table = Hash_Table_CM(size=7)
    process_file_and_populate_hash_table(TEST_FILE_PATH, my_hash_table)

    # Вывод результата
    result_output = str(my_hash_table)
    print("\n--- Вывод в Консоль ---")
    print(result_output)

    # Запись в файл
    with open(RESULT_FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(result_output)

    print(f"\nРезультат записан в файл: '{RESULT_FILE_PATH}'")
