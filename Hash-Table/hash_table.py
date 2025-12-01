from abc import ABC, abstractmethod

class Hash_Table(ABC):
    
    def __init__(self, size = 10):
        self.size = size


    def get_hash(self, key) -> int:
        return sum(ord(char) for char in str(key)) % self.size 
    
    @abstractmethod
    def add(self, key, value) -> None:
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def delete(self, key):
        pass