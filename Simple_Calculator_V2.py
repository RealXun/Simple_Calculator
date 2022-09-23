import sys
#Here we define the operations
def multiplication(num1, num2):
    return num1 * num2
def addition(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def divide(num1, num2):
    return num1 / num2
def modulus_operation(num1, num2):
    return num1 % num2
def division_operation(num1, num2):
    return num1 // num2

#Here we create the first input
def first_number():
    #First we check if it is integner, if it is integer we get the number, if there is a ValueError we check if is it float
    while True:
        number1 = input("\nIntroduce the First number: ")
        try:
            number1 = int(number1)
            return number1
        except ValueError:
            try:
                number1 = float(number1)
                return number1
            except ValueError:
                print('T\The value provided is not a number. Try again.')
                continue

#Here we create operation input
def what_operation():
    while True:
        operation = input('\nPlease enter what operation you would like to do, / is divide, * is multiply, + is plus and - is minus, % Modulus, // Floor Division: ')
        if operation in {'+', '-', '/', '*', '//', '%'}:
            return operation
        else:
            print(f'Not a valid answer: {operation}, try again')
        continue

#Here we create the second input
def second_number(number2):
    while True:
        number2 = input("\nIntroduce the Second number: ")
        try:
            number2 = int(number2)
            return number2
        except ValueError:
            try:
                number2 = float(number2)
                return number2
            except ValueError:
                print('T\The value provided is not a number. Try again.')
                continue

def exit_continue():
    while True:
        question = input("\nDo you wanna continue?: y/n: ")
        if question in {'y', 'Y', 'n', 'N',}:
            if question == "n" or question == "N":
                return sys.exit(-1)
            elif question == "Y" or question == "y":
                break
        print(f'Not a valid answer: {question}, try again') 

while True:
    print("""Available Operations in this calculator:
    Addition(+)-->Adds the values on either side of the operator.
    Subtraction(-)-->Subtracts the value on the right from the one on the left.
    Multiplication(*)-->Multiplies the values on either side of the operator.
    Division(/)-->Divides the value on the left by the one on the right. Notice that division results in a floating-point value.
    Floor Division(//)-->Divides and returns the integer value of the quotient. It dumps the digits after the decimal.
    Modulus(%)-->Divides and returns the value of the remainder.
    """)    
    n1=first_number()
    
    operation=what_operation()

    n2=first_number()

    #Here the math operation starts: SUM, Subtraction, division, Multiplication,Modulus operation, Floor Divisiong
    if operation in {'+'}:
    	print ("\nThe sum of", n1, "plus", n2, "is:",addition(n1, n2))
    
    if operation in {'-'}:
    	print ("\nThe Subtraction of", n1, "minus", n2, "is:",subtraction(n1, n2))
    
    if operation in {'/'}:
    	print ("\nThe division of", n1, "divided by", n2, "is:",divide(n1, n2))
    
    if operation in {'*'}:
    	print ("\nThe multiplication of", n1, "mulpiplty by", n2, "is:",multiplication(n1, n2))
    
    if operation in {'%'}:#Modulus operation
    	print ("\nThe Modulus of", n1, "and", n2, "is;",modulus_operation(n1, n2))
    
    if operation in {'//'}:
    	print ("\nThe Floor Division of", n1, "and", n2, "is:",division_operation(n1, n2))

    #Here we create the question to exit or continue
    exit=exit_continue()