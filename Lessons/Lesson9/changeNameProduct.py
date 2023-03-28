
from variantChoose import variantChoose

def changeNameProduct(store, category):
    categoryChoose = variantChoose(category)

    if categoryChoose == 'q':
        return

    products_in_category = store[categoryChoose][category[categoryChoose]]

    variant = variantChoose(products_in_category)

    if variant == 'q':
        return
    else:
        products_in_category[variant]['Label'] = input("Please, enter new name:  ")
        print("The name has been changed")

    