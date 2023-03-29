
from Func.exeptInt import exeptInt

def createProduct(label, price, desk = None):

    if label == '' or price == '':
        print("\nUnable to create this product!")
  
        if label == '':
              print("Incorrect label!")

        if price == '':
              print("Incorrect price!\n")
        return False
     
    if desk == '':
          desk = None

    exeptInt(price)
          
    product = {'Label': label,
               'Price': price,
               'Desc': desk
             }

    return(product)