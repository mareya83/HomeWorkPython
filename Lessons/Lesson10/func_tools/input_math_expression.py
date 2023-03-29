from  func_tools.num_Int_or_Float import  num_Int_or_Float

def input_math_expression():
    
    expression = input("Please, enter mathematical expression: a+b, a-b, a*b, a/c, if square: a**:    ")

    math_operatin = None
    index = None

    math_operatins = ['**', '+', '-','*','/',]
    for i in  math_operatins:
        if i in expression:

            index = expression.index(i)

            math_operatin = i

            num1 = num_Int_or_Float(expression[0 : index])
  
            num2 = num_Int_or_Float(expression[index + len(math_operatin) :])

            if  num1 == False or (math_operatin == '**' and num2 != False) or (math_operatin != '**' and num2 == False):
                math_operatin = False
                print("Incorrect expression!")
            return math_operatin, num1, num2

    print("Incorrect expression!")
    return math_operatin, num1, num2