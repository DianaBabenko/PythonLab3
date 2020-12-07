# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from Boat import Boat
from Car import Car
from SolarCar import SolarCar
from GasTank import GasTank
from Engine import Engine
from Wheels import Wheels


def test_drive(driveable):
    driveable.get_wheels_count()
    driveable.accelerate()
    driveable.turn('LEFT')
    driveable.turn('RIGHT')
    driveable.brake()

if __name__ == '__main__':
    boat = Boat(GasTank(30), Engine(20), Wheels(0))
    car = Car(GasTank(30), Engine(35), Wheels(4))
    solarCar = SolarCar(GasTank(50), Engine(25), Wheels(4))

    vehicles = [boat, car, solarCar]

    for i in vehicles:
        test_drive(i)



