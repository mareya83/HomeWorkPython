# Until "STOP"
# data_base = [{"..." : "..."}]

# 1) Registration
# 2) Autorizaetin -> greating

data_base = []

def menu():
    menu_of_program = ["1) Registration", "2) Autorisation", "3) Data of users", "4) STOP the program"]

    for i in menu_of_program:
        print(i)
    selection = int(input("Select a menu item: "))

    if selection >= 1 and selection <= 4:
        return selection
    else:
        print("\n Not a correct choice! Try again! \n")
        menu()


def data_of_user():
    user = {"Login" : input("Enter your login: "),
            "Password": input("Enter your password: ")}
    if "@" in user["Login"] and "." in user["Login"] and int(user["Password"]) > 2:
         return user
    else:
        print("Login must contain '@' and '.' or password  > 2  \n")
        


def registratin():
    global data_base
    
    is_runing = True
    while is_runing:
        user = data_of_user()
        if user != None:
             data_base.append(user)
        is_runing = int(input("Would you like to create an account again?:  0 - Not, 1-Yes  "))

    return data_base

is_runing = True
while is_runing:
    selected = menu()
    if selected == 1:
        registratin()

    elif selected == 2:
        if data_of_user() in data_base:
            print("Hello! \n")
        else:
            print("There is no such user \n")

    elif selected == 3:
        for i in data_base:
            print(i)

    else:
        print("Goodby!")
        is_runing = False