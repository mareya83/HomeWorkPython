def printStore(store):
    for i in store:
        for key, value in i.items():
            print(key)
            for product in value:
                print(product)