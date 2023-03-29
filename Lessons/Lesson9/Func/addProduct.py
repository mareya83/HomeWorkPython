
from Func.menu import menu
from Func.createProduct import createProduct
from Func.createProducts import createProducts

def addProduct(store, category):
    for i in range(len(category)):
        print(category[i])

    category_entered = input("Please, enter categoory:    ")

    if (category_entered in category) == False:
        print("There is no such category \n")
        new_category = menu('Do you wont to create new category?:  y/n    ').lower()

        if new_category == 'y':
           category.append(category_entered)
           create_product = createProducts([input("Enter label  ")], input("Enter price:  "), input("Enter data:  "))
           if create_product != False:
                product = {category_entered: create_product}
                store.append(product)
                print("Product added \n")

        elif new_category == 'n':
            return

        else:
            print("Incorrect choose")

    else:
        for i in store:
            for key in i:
                if key == category_entered:
                     create_product = createProduct(input("Enter label:  "), input("Enter price:  "), input("Enter data:  "))
                     if create_product != False:
                        i[key].append(create_product)
                        print("Product added \n")
    
           
    return store