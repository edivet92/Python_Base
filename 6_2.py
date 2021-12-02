class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def count_mass(self, weight = 3, height = 4):
        return(f'{self._length}м * {self._width}м * {weight}кг * {height}см ='
               f'{self._length * self._width * weight * height / 1000}т')
road = Road(5000, 6)
print(road.count_mass())