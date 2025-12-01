# Разрешение коллизии методом открытой адресации

import string
import hash_table as ht

class Hash_Table_OA(ht.Hash_Table): # OA -> Open Addressing
    
    def __init__(self, size=10):
        super().__init__(size)

        self.hash_table = [(None, None, None) for _ in range(self.size)]
    
    
    # Добавление новой записи
    def add(self, key, value):
        key_hash = self.get_hash(key)

        # Проверка на наличие места в таблице
        if self.hash_table[key_hash] is None:
            self.hash_table[key_hash] = (key_hash, key, value)

        # Произошла коллизия (используем линейное пробирование)
        else:
            new_hash = None
            
            for i in range(key_hash + 1, self.size + key_hash):
                tmp = i % self.size

                if self.hash_table[new_hash] is None:
                    new_hash = tmp
                    break
            
            if new_hash is None:
                raise RuntimeError("Недостаточно места в хеш-таблице")
            
            self.hash_table[new_hash] = (new_hash, key, value)

            
                
                

                