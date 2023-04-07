import random


def Cars_number():
    number = ''
    for i in range(0, 12):
        number += str(random.randint(0, 9))
    return number