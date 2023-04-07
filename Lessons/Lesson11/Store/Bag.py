
class Bag: 
    def __init__(self, bag = []):
        self.bag = bag

    def addProdukt(self, product):
        self.product = product
        self.bag.append(self.product)

    def getBag(self):
        return self.bag