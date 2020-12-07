from Driveable import Driveable


class Vehicle(Driveable):

    def __init__(self, gas_tank, engine, wheels):
        self.gas_tank = gas_tank
        self.engine = engine
        self.wheels = wheels.get_count()
        self.speed = 0

    def get_wheels_count(self):
        if self.wheels == 0:
            print("Boat doesn't have a wheels")
        else:
            print('count of wheels ' + str(self.wheels))

    def accelerate(self):
        self.speed = self.speed + self.gas_tank.get()
        print('accelerate to speed ' + str(self.speed) + 'km/h')

    def turn(self, side):
        print('turns ' + str(side))

    def brake(self):
        while self.speed != 0:
            self.speed = self.speed - (self.speed / 2)
            if self.speed == 1:
                self.speed = 0
                break
            print('speed: ' + str(self.speed) + 'km/h')
            break
        print('stop')
