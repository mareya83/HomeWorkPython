
# 1) Image the number that u want and then put it into variable (create variable with number value)
# 2) Propose user guess this number
# 3) if user_number bigger than ur , say to user : ur number bigger than mine
# 4) if user_number less than ur , say to user : ur number less than mine
# 5) if user_number equal to our , say to user : Impossible
# 5) if user_number is not a number : WTH ?
# 6) Progam works until user guess the number

number = 10

is_running = True

while is_running == True:

    try: 
        user_number = int(input("Enter a number  :"))
    except ValueError:
        print("WTH ?")
        continue

    if user_number == number:
        print("Impossible")
        is_running = False

    elif user_number > number :
        print("ur number bigger than mine")

    elif user_number < number:
        print("ur number less than mine")