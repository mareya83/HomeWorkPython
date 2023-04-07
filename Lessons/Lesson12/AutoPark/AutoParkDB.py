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




