from time import sleep
class TrafficLight:
    __color = None
    def running(self):
        while True:
            print('Red')
            sleep(7)
            print('Yellow')
            sleep(2)
            print('Green')
            sleep(3)
lights = TrafficLight()
lights.running()