import random
from exeptInt import exeptInt

def createProducts(label = None, price = None, desk = None):
    products = []
    labels = label.copy()

    if label == '' or price == '':
        print("\nUnable to create this product!")
  
        if label == '':
              print("Incorrect label!")

        if price == '':
              print("Incorrect price!\n")
        return False
     
    if desk == '':
          desk = None
               

    for i in labels:
          if price == None:
               price = random.randint(1000, 10000)

          else:
               exeptInt(price)

          label = labels[random.randint(0, len(labels)-1)]        

          product = {'Label': label,
               'Price': price,
               'Desc': desk
             }
          products.append(product)
          price = None

    return(products)