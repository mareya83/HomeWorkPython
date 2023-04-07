
class User:
    
    def __init__(self, name, wallet = 0, bag = []):
        self.name = name
        self.wallet = wallet
        self.bag = bag

    def showUser(self):
        return {"Name": self.name, "Wallet": self.wallet, "Bag": self.bag}

    def walletStatus(self):
        return self.wallet

    def bagStatus(self):
        return self.bag

    def addMoney(self, money):
        self.money = money
        self.wallet += self.money

    def addBag(self, add_bag):
        for i in add_bag:
            self.bag.append(i.__dict__)
        

    def seyHello(self):
        print("Hello from user")



class Admin(User):
    def __init__(self):
        super().__init__(self)
     
    def seyHello(self):
        print("Hello from admin")