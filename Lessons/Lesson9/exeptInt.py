def exeptInt(values):
    while True:
        try: 
            values = int(values)
            return values
        except ValueError:
            print("Incorrect price!")
            values = input("Enter int value:      ")

            
        