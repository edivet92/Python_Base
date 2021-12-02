class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
class Position(Worker):
    def get_full_name(self):
        return(f'{self.surname} {self.name}, {self.position}')
    def get_total_income(self):
        return(f"{self._income['wage'] + self._income['bonus']}")
vet = Position('Denis', 'Egorov', 'Vet', 100000, 30000)
driver = Position('Maxim', 'Baranov', 'Driver', 75000, 15000)
print(vet.get_full_name())
print(driver.get_total_income())