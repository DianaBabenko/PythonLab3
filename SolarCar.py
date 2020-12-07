from Car import Car


class SolarCar(Car):
    def __init__(self, gas_tank, engine, wheels):
        super(SolarCar, self).__init__(gas_tank, engine, wheels)

    def accelerate(self):
        print('SolarCar speed ' + str(self.speed))
        super(SolarCar, self).accelerate()

    def turn(self, side):
        print('SolarCar turns')
        super(SolarCar, self).turn(side)

    def brake(self):
        super(SolarCar, self).brake()
        print('SolarCar brake')
        print('#########################')

    def get_wheels_count(self):
        super(SolarCar, self).get_wheels_count()
