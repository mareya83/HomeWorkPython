from func_tools.divide import divide
from func_tools.sum import sum
from func_tools.subtruct import subtruct
from func_tools.multiply import multiply
from func_tools.square import squere
from func_tools.input_math_expression import input_math_expression

# 1) Calculator -> + , * , / , -
# 2) square
# 3) Error handling : try , except , finally


is_running = True
while is_running :
    user_choose = input("Do you want to work with calc? y/n : ")

    if user_choose == "y":
        
        math_operatin, num1, num2 = input_math_expression()

        if math_operatin == "+":
                print(sum(num1, num2))

        elif math_operatin == "-":
                print(subtruct(num1, num2))

        elif math_operatin == "*":
                print(multiply(num1, num2))

        elif math_operatin == "/":
                print(divide(num1, num2))

        elif math_operatin == "**": 
                print(squere(num1))

        else:
            continue
        
    elif user_choose == "n":
        is_running = False
    else :
        continue