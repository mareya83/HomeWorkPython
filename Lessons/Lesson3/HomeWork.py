user = {
    "name": "John",
    "age": 23,
    "friends": [
        "Mike", "Bob", "Joe"
    ],
    "skills": ("HTML", "CSS", "JS"),
}

# 1) Find Mike into the user , than if u found Mike create a variable for him
# 2) Print Mike at the console

if ("Mike" in user["friends"]) == True:
    mike = user["friends"][user["friends"].index("Mike")]
    print(mike)

# 3) Get age of user , and guess when he was born

print("Was born :  ", 2023-int(user["age"]))

# 4) Skills must look as : Python , QA , Selenium

user["skills"] = "Python" , "QA" , "Selenium"
print(user["skills"])

# 5) Sort john's friends

user["friends"] = sorted(user["friends"])
print(user["friends"])

# 6) After sort find index position of "Bob"

print("Bobs imdex :  ", user["friends"].index("Bob"))

# 7) Add new friends to friends : "Taras" , "Danya" , "Bidden"

user["friends"] = user["friends"] + ["Taras" , "Danya" , "Bidden"]
print("Friends:  ",user["friends"] )

# 8) Show how much skills user has

print("User has skills:  ", len(user["skills"]))