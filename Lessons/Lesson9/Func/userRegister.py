from Func.userAddMoney import userAddMoney

def userRegister():

    user = {"name" : input("Enter your name:   ").lower().title(),
            "money" : 0 ,
            "bag" : []}
    
    print("\nHello ", user['name'], "!\n", "You are registered!!! \n", "You money:  ", user["money"], "\n" ) 

    userAddMoney(user)

    return user, True

