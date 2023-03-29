from Func.productByCategory import productByCategory
from Func.exeptInt import exeptInt

def deleteProduct(store, category):
    
    categoryChoose = productByCategory(store, category)

    if categoryChoose == 'q':
        return

    products_in_category = store[categoryChoose][category[categoryChoose]]

    label = input("Enter label:    ")
    prise = exeptInt(input("Enter price:    "))

    find_product = False
    index = None
    for i in products_in_category:
        if label in i.values() and prise in i.values():
            find_product = True
            index = products_in_category.index(i)

    if find_product == False:
        print("This product is not available in the store \n")
    else:
        products_in_category.pop(index)
        print("\n The product has been removed \n")