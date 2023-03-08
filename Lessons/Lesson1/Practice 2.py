# 1) get user name , if user_name length < 2 => Incorrect data , try again
# 2) user_name length > 2 => Do you want to register here ? y/n :
# 3) if "y" -> enter your email => if email contain "@" -> it's valid , otherwise -> invalid -> try again
# 4) if "n" -> goodbye
# 5) if something else -> incorrect data try again later
# 6) Programm works until user enter correct (valid) data ;

cycle = True

while cycle:
    user_name = input("Enter user name: ")
    if len(user_name) < 2:
        print("Incorrect data, try again!")

    else:
        while cycle:
            registration = input("Do you want to register here ? y/n :  ")
            if registration == "y":

                while cycle:
                    mail = input("Enter your email:  ")
                    counter = 0

                    while counter < len(mail):
                        if mail[counter] == "@":
                             adress = True
                        else:
                            adress = False
                        counter += 1

                    if adress:
                        print("It's valid!")
                        cycle = False
                    else:
                        print("Invalid! Try again!")

            elif registration == "n":
                print("Goodbye")
                cycle = False

            else:
                print("Incorrect data, try again!")




