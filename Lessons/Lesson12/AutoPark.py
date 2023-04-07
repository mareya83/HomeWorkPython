# 1) Create AutoPark
# 2) DB for AutoPark
# 3) Auto
# 4) Sedan , Truck , Hatchback
# 5) Sedan , Truck , Hatchback  : add fafa Method => Sedam => bibi , Truck => fafa , Hatchback => meep-meep

import random

class Car:
    def __init__(self, category, label, price, color, number, weels = 4):
        self._category = category
        self._label = label
        self._price = price
        self._color = color
        self._number = number
        self._weels = weels
    
    def getCategory(self):
        return self._category

    def getPrice(self):
        return self._price

    def fafa(self):
        print("fa-fa")



class Sedan (Car):
    def __init__(self, category, label, price, color, number, weels = 4):
        super().__init__(category, label, price, color, number, weels)

    def fafa(self):
        print("bi-bi")



class Truck (Car):
    def __init__(self, category, label, price, color, number, weels = 4):
        super().__init__(category, label, price, color, number, weels)



class Hatchback (Car):
    def __init__(self, category, label, price, color, number, weels = 4):
        super().__init__(category, label, price, color, number, weels)

    def fafa(self):
        print("meep-meep")


class AutoParkDB :
 
    _cars = {
                "Sedan" : [],
                "Truck" : [],
                "Hatchback" : []
            }


    def getCars (self) :
        return self._cars

    def saveCar (self, car, category) :
        self._cars[category].append(car)

    def show(self):
        for i in self._cars:
            print(i)
            for n in self._cars[i]:
                print(n.__dict__)



class AutoPark:
    _instance = None

    def __new__(cls, autoParkDB):
        if cls._instance is None :
            cls._instance = super().__new__(cls)
            cls._instance.autoParkDB = autoParkDB

        return cls._instance

    

autoParkDB = AutoParkDB
autoPark = AutoPark(autoParkDB)
print(autoPark.autoParkDB().getCars)



colors = ['red' , 'green' , 'black' , 'yellow' , 'blue']
labels = ['Audi', 'Bmw', 'Ford', 'Honda', 'Hyundai', 'Kia', 'Mazda']


def number():
    number = ''
    for i in range(0, 12):
        number += str(random.randint(0, 9))
    return number

def sedan(quantity):
    sedan = []
    for i in range(0, quantity):
        sedan.append(Sedan("Sedan", random.choice(labels), random.randint(2000, 200001), random.choice(colors), number()))
    return sedan


def truck(quantity):
    truck = []
    for i in range(0, quantity):
        truck.append(Truck("Truck", random.choice(labels), random.randint(2000, 200001), random.choice(colors), number()))
    return truck


def hutchback(quantity):
    hatchback = []
    for i in range(0, quantity):
        hatchback.append(Hatchback("Hatchback", random.choice(labels), random.randint(2000, 200001), random.choice(colors), number()))
    return hatchback


def fill_auto_park(*args):
    for items in args:
        for item in  items :
            autoPark.autoParkDB().saveCar(item, item.getCategory())


def sort(condition):
    for items in autoParkDB().getCars():
        for item in autoParkDB().getCars()[items]:
            if condition in item.__dict__.values():
                print(item.__dict__)


def print_dict(dict):
    for i in dict:
        print(i)
        for j in dict[i]:
            print(j)


def sort_price(price_choose):
    
    cheap = {"Cheap" : []}
    medium = {"Medium": []}
    expensive = {"Expensive": []}
    

    for items in autoParkDB().getCars():
        for item in autoParkDB().getCars()[items]:
            price = item.getPrice()
            if price >= 2000 and price < 20000:
                cheap["Cheap"].append(item.__dict__)
            if price >= 20000 and price < 100000:
                medium["Medium"].append(item.__dict__)
            if price >= 100000 and price <= 200000:
                expensive["Expensive"].append(item.__dict__)

    if price_choose == '1':
        print_dict(cheap)
    elif price_choose == '2':
        print_dict(medium)
    elif price_choose == '3':
        print_dict(expensive)
    else:
        print("Incorrect choose")
        


def menu(*args):
    for i in args:
        print(i)
    
    chooce = input("Enter your choose:   ")
    try:
        int(chooce)
    except ValueError:
        chooce = 0
    return chooce


sedan = sedan(2)
truck = truck(3)
hutchback = hutchback(5)

fill_auto_park(sedan, truck, hutchback)

autoPark.autoParkDB().show()

is_runing = True
while is_runing:
    chooce = menu("1) Sort by labels", "2) Sort by colors", "3) Sort by price", "4) Quit")

    if chooce == '1':
        
        print(labels)
        label = input("Enter label:     ")

        if label in labels:
            sort(label)
            
        else:
            print("Incorrect label")
        
    elif chooce == '2':
        print(colors)
        color = input("Enter color:     ")

        if color in colors:
            sort(color)
            
        else:
            print("Incorrect color")

    elif chooce == '3':

        chooce_price = menu("1) cheap", "2) medium", "3) expensive")
        sort_price(chooce_price)

    elif chooce == '4':
        print("Goodby!")
        is_runing = False

    else:
        print("Incorrect chooce!")
