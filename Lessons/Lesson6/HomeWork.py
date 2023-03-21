
# 1) Create a store [] with objects : { label : “kit-kat” , price : 200 } , and other by example 

# 2) Register user , and ask how much money user has 

# 3) Take a list of products to user 

# 4) User might buy every products he wants if he had enough money 

# Otherwise we must say : “Sorry , your pockets are empty”

# 5) User can exit in start-menu

user = {}
user_status = False

def menu(*args):
    for i in args:
        print(i)
    return int(input("Plese, select a menu item:  "))


def user_register():
    user = {"name": input("Enter your name:  "),
            "pockets": int(input("Enter your money:  "))}
    return user, True


def store(key, value):
    product = {"label": key,
               "price": int(value)}
    return product

        
products = [store("Kit-kat", 20), 
            store("Snikers", 30),
            store("Twix", 40)]


is_runing = True
while is_runing:
    user_select = menu("\n1) Registration", "2) View products", "3) Buy products", "4) Balance", "5) Quit ") 

    if user_select == 1:
        user, user_status = user_register()

    elif user_select == 2:
        for i in range(len(products)):
            print(products[i]["label"], ":", products[i]["price"])

    elif user_select == 3:
        if user_status == True :
            cycle = True
            while cycle:
                if user["pockets"] == 0:
                    print("Sorry , your pockets are empty")
                    break   

                product_availability = False
                product_buy = input("\n Enter product:  ")

                for i in range(len(products)):
                    if product_buy in products[i].values():
                        product_buy = products[i]
                        product_availability = True
                        break

                if product_availability == True :
                    if user["pockets"] >= product_buy["price"]:
                        user["pockets"] = user["pockets"] - product_buy["price"]
                        print("Successfully")
                    else:
                        print("Not enough money!")
                else:
                    print("The product is not available\n")


                shopping = input("Do you want to continue shopping? Y/N  :\n")
                if shopping == "N":
                    cycle = False

        else:
            print("\n Please register! \n")


    elif user_select == 4:
        if user_status == True :
                print("Your balance ", user["pockets"])
        else:
            print("\n Please register! \n")
            

    elif user_select == 5:
        print("\n Goodbye!!! \n")
        break

    else:
        print("\n Incorrect selection, try again! \n")
        continue
