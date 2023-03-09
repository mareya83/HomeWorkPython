# 1) Create an empty array [] (Don't forget about names for variables)
# 2) Create an empty string and then save it in variable "register_data"
# 3) Get login and password from user and then => save data into "register_data"
# 4) if logon length less than 5 print an Error
# 5) if password contains more than 10 symbols throw an Error

# USE: split, slice, create other variables. Do everything than you want to, but remember
# that all data above must exist.

empty_array = []

empty_string = ""
register_data = empty_string
# register_data = {}
# register_data['ampty_string'] = empty_string

login = input("Enter your login : ")
password = input("Enter your password : ")

i = True
while i:
    if len(login) == 0:
        login = input("Enter your login : ") 
    elif len(password) == 0:
        password = input("Enter your password : ")
    else:
        i = False

# register_data['login'] = login
# register_data['password'] = password

register_data = register_data + login + password

print(register_data)

if len(login) < 5:
    print("Login ERROR!")

if len(password) > 10:
    print("Password ERROR!")


