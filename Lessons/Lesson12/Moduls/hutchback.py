import random
from Moduls.Cars_number import Cars_number
from AutoPark.Car import Hatchback

def hutchback(quantity, labels, colors):
    hatchback = []
    for i in range(0, quantity):
        hatchback.append(Hatchback("Hatchback", random.choice(labels), random.randint(2000, 200001), random.choice(colors), Cars_number()))
    return hatchback