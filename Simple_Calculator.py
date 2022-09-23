while True:
    print("""Available Operations in this calculator:
    Addition(+)-->Adds the values on either side of the operator.
    Subtraction(-)-->Subtracts the value on the right from the one on the left.
    Multiplication(*)-->Multiplies the values on either side of the operator.
    Division(/)-->Divides the value on the left by the one on the right. Notice that division results in a floating-point value.
    Floor Division(//)-->Divides and returns the integer value of the quotient. It dumps the digits after the decimal.
    Modulus(%)-->Divides and returns the value of the remainder.
    """)   
    # take input for the first number from the user and check if the input is an integer or float.
    n1 = input("Introduce the First number: ")
    
    #First we check if it is integner, if it is integer we get the number, if there is a ValueError we check if is it float
    try:
        n1 = int(n1)
        #print(n1)
        #print(type(n1))
    #here we check if it it a float number.
    except ValueError:
        try:
            n1 = float(n1)
            #print(n1)
            #print(type(n1))
        except ValueError: #Not interget number, not a float number, then we to type again
            print('T\The provided value is not a number. Try again.')
            continue

    while True:
        operation = input('\nPlease enter what operation you would like to do, / is divide, * is multiply, + is plus and - is minus, % Modulus, // Floor Division: ')
        if operation in {'+', '-', '/', '*', '//', '%'}:
            break
        print(f'Operation not recognized: {operation}, try again')

    # take input for the second number from the user and check if the input is an integer or float.
    while True:
        n2 = input("\nIntroduce the Second number: ")
        #First we check if it is integner., if there is a ValueError we check if is it float
        try:
            n2 = int(n2)
            #print(n2)
            #print(type(n1)
            #If  it is integer we break this while and go to the next step
            break
        #here we check if it it a float number.
        except ValueError:
            try:
                n2 = float(n2)
                #print(n2)
                #print(type(n1))
                #If  it is a float number we break this while and go to the next step
                break
            #Not interget number, not a float number, then we to type again
            except ValueError:
                print('\nThe provided value is not a number. Try again.')
                continue

    #Here the math operation starts
    #Sum operation
    if operation in {'+'}:
    	print ("\nThe sum of", n1, "plus", n2, "is:",n1+n2)
    
    #Sum operation
    if operation in {'-'}:
    	print ("\nThe Subtraction of", n1, "minus", n2, "is:",n1-n2)
    
    #divide operation
    if operation in {'/'}:
    	print ("\nThe division of", n1, "divided by", n2, "is:",n1/n2)
    
    #multiply operation
    if operation in {'*'}:#multiply operation
    	print ("\nThe multiplication of", n1, "mulpiplty by", n2, "is:",n1*n2)
    
    #Floor Modulus operation
    if operation in {'%'}:#Floor Modulus operation
    	print ("\nThe Modulus of", n1, "and", n2, "is;",n1%n2)
    
    #Floor Division operation
    if operation in {'//'}:
    	print ("\nThe Floor Division of", n1, "and", n2, "is:",n1//n2)

    #Here we create the question to exit or continue
    while True:
        yes_no = ("Y","N","y","n")
        question = input("\nDo you wanna continue?: y/n: ")
        if question in {'y', 'Y', 'n', 'N',}:
            if question == "n" or question == "N":
                raise SystemExit
            elif question == "Y" or question == "y":
                break
        print(f'Not a valid answer: {question}, try again')
