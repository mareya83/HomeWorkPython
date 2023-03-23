# 								Homework

# 1) Register:
# - email , login , password

# Email : 
# - must contain “@” and “.”

# Password : 
# - more than 6 symbols 
# - must contain upper and lower -case letters
# - must contain number , or symbols as : “@” , “!” , etc.

# Name : 
# - more or equal to 2 symbols 
# - first letter must be in uppercase 

# 2) Practice with me -> Look at last lesson (04.03.2023)

def find_element(finded, password):
    find_element = False
    for i in finded:
        if str(i) in password:
            find_element = True
            break
    return find_element

def email():
    
    is_runing = True
    while is_runing:
        email = input("Enter Email:  ")
        if "@" in email and "." in email:
            is_runing = False
        else:
            print("Incorrect email!")
    return email

def password():
    is_runing = True
    while is_runing:
        password = input("Enter password:  ")

        if len(password) < 6:
            print("Password must be more than 6 symbols ")
            continue
        
        if find_element(list(range(10)), password) == False:
            print("Password must contain number!")
            continue

        if find_element(('!', '@', '#', '$', '%', '&'), password) == False:
            print("Password must contain '!', '@', '#', '$', '%', '&'")
            continue

        if password.islower() == True:
            print("Password must contain uppercase characters") 
            continue   

        if password.isupper() == True:
            print("Password must contain lowercase characters")
            continue

        if password.islower() == False and password.isupper() == False:
            is_runing = False

    return password

def name():
    name = input("Enter name:  ")
    is_runing = False
    while is_runing:
        if len(name) >= 2:
            is_runing = True
        else:
            print("Incorrect name!")
            name = input("Enter name:  ")
    return name.lower().title()

def register(email, password, name):
    user = {
        "email" : email,
        "password" : password,
        "name" : name
    }
    return user


user_email = email()
user_password = password()
user_name = name()

print("\n************************************************************\n")

user = register(user_email, user_password, user_name)
for key, value in user.items():
    print(key, " - ", value)