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