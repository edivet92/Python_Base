class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return(f"{self.name} goes wrum-wrum")
    def stop(self):
        return(f"{self.name}'s rare lights flash red")
    def turn(self, direction):
        return(f"{self.name} turned {direction}")
    def show_speed(self):
        return(f"{self.name}'s speed is {self.speed} m/h")
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return(f"{self.name} runnig too fast")
        else:
            return super().show_speed()
class SportCar(Car):
    """ Lambo """
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return(f"{self.name} runnig too fast")
        else:
            return super().show_speed()
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        super().__init__(speed, color, name, is_police = True)
kia_rio = PoliceCar(120, 'red', 'kia')
lada_granta = WorkCar(130, 'white', 'granta')
lotus_esprit = SportCar(330, 'yelow', 'lotus')
ford_focus = TownCar(58, 'blue', 'focus')
print(lotus_esprit.show_speed(), lotus_esprit.go())
print(kia_rio.turn('right'), kia_rio.go())
print(lada_granta.turn('left'), lada_granta.show_speed())
print(ford_focus.show_speed(), ford_focus.stop())
for i in [ford_focus, lotus_esprit, lada_granta, kia_rio]:
    print(i.is_police)