import random
from Moduls.Cars_number import Cars_number
from AutoPark.Car import Truck

def truck(quantity, labels, colors):
    truck = []
    for i in range(0, quantity):
        truck.append(Truck("Truck", random.choice(labels), random.randint(2000, 200001), random.choice(colors), Cars_number()))
    return truck