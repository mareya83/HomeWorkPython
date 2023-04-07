import random
from Moduls.Cars_number import Cars_number
from AutoPark.Car import Sedan


def sedan(quantity, labels, colors):
    sedan = []
    for i in range(0, quantity):
        sedan.append(Sedan("Sedan", random.choice(labels), random.randint(2000, 200001), random.choice(colors), Cars_number()))
    return sedan