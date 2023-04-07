class Сart: 
    def __init__(self):
        self.products = []   
             
    def getFullPrice(self, *args):
        self.products = args
        sum_products = 0
        for i in args:
            sum_products += i.getPrice()
        return sum_products

    def getCurt(self):
        return self.products