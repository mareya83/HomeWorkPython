
# 1) Greeting
# 2) Context_menu: a) Buy something, quit
# 3) a => Register new User q => exit
# 4) Show products for User
# 5) User might buy something and that somesing  must put into Cart
# 6) After every deal => "Do you wanna buy something alse?"
# 7) If n0 => get user money/ if money < something => Not enough money
# 8) Do you wanna go? a) Yes => "Goodbye" b) No => 1

# class Store: products = []

# class User: => bag, money/cash/wallet/card = $ inherit User => sayHello () => print("Hello from user")

# class Product: price, label   

# class Сart: sum_products = [] => getFullPrice(*args, **kwargs)

# class Admin: => inherit User => sayHello () => print("Hello from admin")

# class Bag: bag = []

import random
from func_tools.menu import menu
from func_tools.intMoney import intMoney



class Store: 
    def __init__(self, products):
        self.products = products

    def getStore (self):
        return self.products

    def showStore(self):
        print ("Store")
        for i in self.products:
            print(i)

        



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



class Bag: 
    def __init__(self, bag = []):
        self.bag = bag

    def addProdukt(self, product):
        self.product = product
        self.bag.append(self.product)

    def getBag(self):
        return self.bag


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





labels = ["LG", "Samsung", "HUAWEI", "Apple", "Oppo", "Xiaomi"]

store = Store(Product(labels).getProducts())

print("Hello!!!!")

register_status = False
is_runung = True

while is_runung:

    useer_choose = menu("a) User", "b) Admin")

    if useer_choose == 'a':

        is_runung_user = True

        while is_runung_user:  

            user_menu_choose = menu("a) Register or add money", "b) Show products", "c) Buy something")

            if user_menu_choose == 'a':
                if register_status == False:
                    name = input("Enter your name:   ").lower().capitalize()

                    if len(name) > 0:

                        money = intMoney(input("Enter your money:   "))
                        user = User(name, money)
                        register_status = True

                        user.seyHello()

                        print(user.showUser())

                    else:
                        print("You didn't enter a name")
                else:
                    user.addMoney(intMoney(input("Enter your money:   ")))
                    print(f"In your wallet {user.walletStatus()}")


            elif user_menu_choose == 'b':

                store.showStore()
                    

            elif user_menu_choose == 'c':

                if register_status == True:
                    bag = Bag()
                    
                    is_shoping= True
                    while is_shoping:
                        if user.walletStatus() > 0:

                            print("\n ******* You can buy something *******")
                            store.showStore()
                                

                            label = input("Please, enter label:    ")
                            price = intMoney(input("Please, enter price:    "))

                            buy_product = Product(label, price)

                            if buy_product.getProduct() in store.getStore(): 
                                if price <= user.walletStatus():
                                    
                                    
                                    bag.addProdukt(buy_product)

                                    print("Good buy!!!!")

                                    user.addMoney(-price)

                                    shoping = menu("Do you wanna buy something alse?:   pass")
                                    if shoping == 'q':
                                        is_shoping = False

                                else:
                                    is_shoping = False
                                    print("Not enough money")

                            else:
                                is_shoping = False
                                print("There is no such product")


                        else:
                            print("Your wallet is empty!")
                            user.addMoney(intMoney(input("Enter your money:   ")))
                            print(f"In your wallet {user.walletStatus()}")
                
                    user.addBag(bag.getBag())
                    print(user.showUser())

                    cart_full_sum = Сart().getFullPrice(*bag.getBag())

                    print(f"Cost:  {cart_full_sum}")

                else:
                    print("You can buy only after registration!")

            elif user_menu_choose == 'q':
                is_runung_user = False

            else:
                continue


    elif useer_choose == 'b':
        
        Admin().seyHello()


    elif useer_choose == 'q':
        print("Googby!!")
        is_runung = False

    else:
        continue