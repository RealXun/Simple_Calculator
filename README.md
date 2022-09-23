# Simple Calculator
Create a simple calculator.
<p align="center">
    <img src="https://github.com/RealXun/Simple_Calculator/blob/main/Resources/cover.png" width="500">

## Simple calculator V2
With defining functions:
- def first_number() --> To input the first number.
- def second_number() --> To input the second number.
- def what_operation() --> To input the math operation we want to do.
- def exit_continue() --> To exit or to continue with another operation.
- def multiplication() --> Multiplication operation.
- def addition() --> Sum operation.
- def subtraction() --> Subtraction operation.
- def divide() --> Division operation.
- def modulus_operation() --> Modulus operation.
- def division_operation() --> Floor Division operation.

## Simple calculator V1 
Without defining functions.

With this flow:
- Insert first number.
- Insert an operation.
- Insert second number.

Must accept a symbol, such as the asterisk (*) symbol, to perform the operation and produce a product:
- Sum (+)
- Subtraction (-)
- Multiplication (*)
- Quotient (/)
- Exponent (//)
- Module (%)

### IMPORTANT 
> If the user does not type a numeric value, display an error message like:
> Please input a number.

> If the user types an operation that is not recognized, display an error message like:
> Operation not recognized.

## Here is an example output, where a user has typed 4, **, and 5* into the input boxes:
```
Simple calculator!
First number? 4
operation? *
Second number? 5
product of 4 * 5 equals 20
```

### Pseudocode
```
PSEUDOCODE
We declare two input values, number1 and number2.

number1 (input)

Declare the type of operation to perform

operation (input)
We create a variable with a list of operators

operators = ["+", "-", "*", "/", "//", "%" ]
We declare the evaluation condition IF the operator is not found in the list of Operators `` print (Operation not recognized)

number2 (input)

ELSE

IF the operation is "+"
ELSE RESULT a+b

IF THE operation is "-"
ELSE RESULT a-b

... like this for the rest of the operators

print(result)
```
