# Auto-park

# DB ->
#       named as auto =>
#                       [ scheme of auto :
#                           {
#                              "label" : ... ,
#                              "price" : ... ,
#                              "wheels" : ... ,
#                              "color" : ... ,
#                              "number" : "random value"
#                           }
#                        ]

# Amount of auto > 10

# color : red , green , black , yellow , blue

# label : more than 5

# price : from 2000 till 200 000

# number and number length > 12

# Form category dictionary :
# dynamic

# cheap (2000 - 20000) , expensive(100000 - 200000) , medium - (20000 - 100000) - class car
# def sort_car_by_price (arr)
# return {
#   cheap : [],
#   medium : [],
#   expensive : []
# }


# print( cars that we have : for poor , rich , and medium-lvl persons )
# input -> sort : color -> choose on of : blue , green , ... ;  price , label


# for , while

import random

auto_park = []
size_of_auto_park = 15

colors = {'red' , 'green' , 'black' , 'yellow' , 'blue'}
labels = {'Audi', 'Bmw', 'Ford', 'Honda', 'Hyundai', 'Kia', 'Mazda'}
class_cars = ['cheap', 'expensive', 'medium']


# [{'cheap': random.randint(2000,20000)}, 
#              {'expensive': random.randint(100001,200001)}, 
#              {'medium': random.randint(20001,100000)}]

def menu(*args):
    for i in args:
        print(i)
    chooce = input("Please, chooce variant:   ")
    return chooce

def autopark(labels, class_car, colors, size_of_auto_park):
    i = 0
    while i < size_of_auto_park:    
        auto_park.append(car(rend_choose(labels), price(class_cars), rend_choose(colors), number()))
        i += 1
    return auto_park

def car(label,price ,color, number):
    car = {
            "label" : label,
            "price" : price,
            "wheels" : 4,
            "color" : color,
            "number" : number
        }
    return car

def rend_choose(set):
    choose = random.randrange(len(set))
    count = 0
    for i in set:
        if count == choose:
            return i
        count += 1

def price(class_car):
    choose = rend_choose(class_car)
    value = 0
    if choose == 'cheap':
        value = random.randint(2000,20000)
    if choose == 'expensive':
                value = random.randint(100000,200001)
    if choose == 'medium':
                value = random.randint(20000,100000)
    return {choose: value}

def number():
    i = 0
    number = ''
    while i <= 12:
        number += str(random.randint(0, 10))
        i += 1
    return number

def sort_car_by_price(auto_park, class_car):
    sort_car_by_price = []
    count = 0
    for clas in class_car:
        sort_car_by_price.append({clas: []})
        sort_car_by_price[count][clas] = sort_car(auto_park, clas, 'price')
        count += 1
    return sort_car_by_price

def sort_car(auto_park, condition, key):
    sort = []
    for i in auto_park:
        if condition in i[key]:
            sort.append(i)
    return sort

auto_park = autopark(labels, class_cars, colors, size_of_auto_park)
for i in auto_park:
    print (i)

print("********************************************************************")

for i in sort_car_by_price(auto_park, class_cars):
    for key, value in i.items():
        print(key)
        for v in value:
            print(v)


is_runing = True
while is_runing:
    chooce = int(menu("1) Sort by labels", "2) Sort by colors", "3) Sort by price", "4) Quit"))

    if chooce == 1:
        label = menu(labels)
        for i in  sort_car(auto_park, label.lower().title(), "label"):
            print(i)

    elif chooce == 2:
        color = menu(colors)
        for i in  sort_car(auto_park, color.lower(), "color"):
            print(i)

    elif chooce == 3:
        price = menu(class_cars)
        for i in  sort_car(auto_park, price.lower(), 'price'):
            print(i)

    elif chooce == 4:
        print("Goodby!")
        is_runing = False

    else:
        print("Incorrect chooce!")
