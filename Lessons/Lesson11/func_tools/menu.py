def menu(*args):
    for i in args:
        print(i)
    print("q) Quit")
    choose = input("Select menu item:   ").lower()
    return choose