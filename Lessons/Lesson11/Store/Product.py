import random


class Product:  
    def __init__(self, label, price = 0):
        self.price = price
        self.label = label
    
    def getProduct(self):
        return {"Label": self.label, "Price" : self.price}

    def getProducts(self):
        products = []
        for i in self.label:
            products.append(Product(random.choice(self.label), random.randint(100,4000)).getProduct())
        return products

    def getPrice(self):
        return self.price