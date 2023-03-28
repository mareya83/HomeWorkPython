from createProducts import createProducts

def createStore(category, label, price = None, desk = None ):
    store = []
    for i in category:
          product = {i: createProducts(label, price, desk)}
          store.append(product)
    return store