class Store: 
    def __init__(self, products):
        self.products = products

    def getStore (self):
        return self.products

    def showStore(self):
        print ("Store")
        for i in self.products:
            print(i)