# 1) Create AutoPark
# 2) DB for AutoPark
# 3) Auto
# 4) Sedan , Truck , Hatchback
# 5) Sedan , Truck , Hatchback  : add fafa Method => Sedam => bibi , Truck => fafa , Hatchback => meep-meep

from Moduls.menu import menu
from Moduls.sedan import sedan
from Moduls.truck import truck
from Moduls.hutchback import hutchback
from Moduls.print_dict import print_dict

from AutoPark.AutoParkDB import AutoParkDB, AutoPark


autoParkDB = AutoParkDB
autoPark = AutoPark(autoParkDB)
print(autoPark.autoParkDB().getCars)

def fill_auto_park(*args):
    for items in args:
        for item in  items :
            autoPark.autoParkDB().saveCar(item, item.getCategory())


def sort_cars(condition):
    for items in autoParkDB().getCars():
        for item in autoParkDB().getCars()[items]:
            if condition in item.__dict__.values():
                print(item.__dict__)




def sort_price(price_choose):
    
    cheap = {"Cheap" : []}
    medium = {"Medium": []}
    expensive = {"Expensive": []}
    

    for items in autoParkDB().getCars():
        for item in autoParkDB().getCars()[items]:
            price = item.getPrice()
            if price >= 2000 and price < 20000:
                cheap["Cheap"].append(item.__dict__)
            if price >= 20000 and price < 100000:
                medium["Medium"].append(item.__dict__)
            if price >= 100000 and price <= 200000:
                expensive["Expensive"].append(item.__dict__)

    if price_choose == '1':
        print_dict(cheap)
    elif price_choose == '2':
        print_dict(medium)
    elif price_choose == '3':
        print_dict(expensive)
    else:
        print("Incorrect choose")




colors = ['red' , 'green' , 'black' , 'yellow' , 'blue']
labels = ['Audi', 'Bmw', 'Ford', 'Honda', 'Hyundai', 'Kia', 'Mazda']


sedan = sedan(2, labels, colors)
truck = truck(3, labels, colors)
hutchback = hutchback(5, labels, colors)

fill_auto_park(sedan, truck, hutchback)

autoPark.autoParkDB().show()

is_runing = True
while is_runing:
    chooce = menu("1) Sort by labels", "2) Sort by colors", "3) Sort by price", "4) Quit")

    if chooce == '1':
        
        print(labels)
        label = input("Enter label:     ")

        if label in labels:
            sort_cars(label)
            
        else:
            print("Incorrect label")
        
    elif chooce == '2':
        print(colors)
        color = input("Enter color:     ")

        if color in colors:
            sort_cars(color)
            
        else:
            print("Incorrect color")

    elif chooce == '3':

        chooce_price = menu("1) cheap", "2) medium", "3) expensive")
        sort_price(chooce_price)

    elif chooce == '4':
        print("Goodby!")
        is_runing = False

    else:
        print("Incorrect chooce!")
