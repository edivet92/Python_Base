from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, size):
        self.size = size
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("Размер должен быть целым числом")
        elif size <= 0:
            raise ValueError("Размер должен быть больше ноля")
        self._size = size
    @abstractmethod
    def consumption(self):
        return 'Hocus-pocus'
    def __add__(self, other):
        return round(self.consumption() + other.consumption(), 2)
    def __str__(self):
        return f"{round(self.consumption(), 2)}"    

class Coat(Clothes):
    def consumption(self):
        return self.size/6.5 + 0.5
class Costume(Clothes):
    def consumption(self):
        return self.size*2 + 0.3

coat = Coat(65)
costume = Costume(9)
print(coat)
print(costume)
print(coat + costume)