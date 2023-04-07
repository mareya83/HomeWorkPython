def intMoney(money):

    try:
        return int(money)
    except ValueError:
        print("Failed money!")
        return 0