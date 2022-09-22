while True:
    # take input from the user and check if the input is an integer.
    n1 = input("Introduce the First number: ")
    try:
        n1 = int(n1)
        print(n1)
        print(type(n1))
    except ValueError:
        try:
            n1 = float(n1)
            print(n1)
            print(type(n1))
        except ValueError:
            print('The provided value is not a number. Try again.')
            continue
    while True:
        operation = input('Please enter what operation you would like to do, / is divide, * is multiply, + is plus and - is minus: ')
        if operation in {'+', '-', '/', '*', '//', '%'}:
            break
        print(f'Not a valid answer: {operation}, try again')
    while True:
        n2 = input("Introduce the Second number: ")
        try:
            n2 = int(n2)
            print(n2)
            print(type(n1))
            break
        except ValueError:
            try:
                n2 = float(n2)
                print(n2)
                print(type(n1))
                break
            except ValueError:
                print('The provided value is not a number. Try again.')
                continue
    if operation in {'+'}:
    	print ("The sum of", n1, "plus", n2, "is;",n1+n2)
    if operation in {'-'}:
    	print ("The sum of", n1, "plus", n2, "is;",n1-n2)
    if operation in {'/'}:
    	print ("The sum of", n1, "plus", n2, "is;",n1+n2)
    if operation in {'*'}:
    	print ("The sum of", n1, "plus", n2, "is;",n1-n2)
    if operation in {'//'}:
    	print ("The sum of", n1, "plus", n2, "is;",n1//n2)
    while True:
        yes_no = ("Y","N","y","n")
        question = input("Do you wanna conitnuio?: y/n: ")
        if question in {'y', 'Y', 'n', 'N',}:
            if question == "n" or question == "N":
                raise SystemExit
            elif question == "Y" or question == "y":
                break
        print(f'Not a valid answer: {question}, try again')
