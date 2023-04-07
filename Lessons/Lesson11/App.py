
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


from func_tools.menu import menu
from func_tools.intMoney import intMoney
from Store.Store import Store
from Store.Product import Product
from Store.User import User, Admin
from Store.Bag import Bag
from Store.Cart import Сart


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