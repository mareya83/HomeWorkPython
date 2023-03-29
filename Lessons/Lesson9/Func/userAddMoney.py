def userAddMoney(user): 
    is_runing = True
    add_money = input("Do you want to add money! y/n:     ").lower()
    while is_runing:
        
        if add_money == 'y':
             money = input("Add money:    ")
             try:
                 user['money'] = user['money'] + int(money)
                 print("\n Money added! \n Youre balance",  user['money'], "\n")
                 is_runing = False
                 return user
        
             except ValueError:
                 print("The value entered is incorrect, try again")
            

        elif add_money == 'n':
            is_runing = False

        else:
            print("Incorrect choose")