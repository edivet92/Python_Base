
class Storage:
    """  """

class OrgTech:
    def __init__(self, name, amount, weight):
        self.name = name
        self.amount = amount
        self.weight = weight  
      
    def on_storage(self):
        storage_dict[self.name] = self.amount, self.weight
    def __str__(self):
        return f'{self.name}: {self.amount} штук, по {self.weight} кг каждый'
class Printer(OrgTech):
    def __init__(self, name, amount, weight, colour):
        super().__init__(name, amount, weight)
        self.colour = colour
class Scaner(OrgTech):
    def __init__(self, name, amount, weight, definition):
        super().__init__(name, amount, weight)
        self.definition = definition
class Xerox(OrgTech):
    def __init__(self, name, amount, weight, speed):
        super().__init__(name, amount, weight)
        self.speed = speed
storage_dict = {}
canon = Printer('canon', 5, 15, 'red')
samsung = Scaner('samsung', 11, 7, 'HD')
xerox = Xerox('xerox', 56, 19, 10)

print(canon.colour)
print(samsung.weight)
print(xerox.amount)
samsung.on_storage()
canon.on_storage()
xerox.on_storage()
print(storage_dict)
print(samsung)