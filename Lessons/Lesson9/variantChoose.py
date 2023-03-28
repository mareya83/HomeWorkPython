
def variantChoose(list):
    for i in range(len(list)):
        print(i, ") ", list[i])

    variant = input("Choose variant, else 'q'   :    ").lower()

    while True:

        try:
            variant = int(variant)
            if variant >= 0 and variant < len(list):
                return variant
            else:
                print("Icorrect choose")
                variant = input("Try again, else 'q'   :     ").lower()

        except ValueError:
            if variant == 'q': 
                return variant
                        
            else:
                print("Icorrect choose")
                variant = input("Try again, else 'q'   :     ").lower()
