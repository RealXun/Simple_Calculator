# Simple Calculator
Create a simple calculator without defining functions
<p align="center">
    <img src="https://github.com/RealXun/Simple_Calculator/blob/main/Resources/cover.png" width="500">

## Create a simple calculator without defining functions - part 1
Create a simple calculator that accepts a first number, an operation, and a second number.

## Here is an example output, where a user has typed 4, **, and 5* into the input boxes:

Simple calculator!
First number? 4
operation? *
Second number? 5
product of 4 * 5 equals 20

> The program must accept a symbol, such as the asterisk (*) symbol, to perform a multiplication and produce a product. Be sure to implement logic for these results:

Sum (+)
Subtraction (-)
Multiplication (*)
Quotient (/)
Exponent (//)
Module (%)

> If the user does not type a numeric value, display this message:
> Please input a number.

> If the user types an operation that is not recognized, display this message:
> Operation not recognized.

Whether you're struggling and need to take a look at the solution or finish the exercise successfully, continue on to see a solution to this challenge.
```
PSEUDOCODE
We declare two input values

to (input)
b (input)
Declare the type of operation to perform

operation (input)
We create a variable with a list of operators

operators = ["+", "-", "*", "/", "//", "%" ]
We declare the evaluation condition IF the operator is not found in the list of Operators `` print (Operation not recognized)


ELSE

IF the operation is "+"
ELSE RESULT a+b

IF THE operation is "-"
ELSE RESULT a-b


... like this for the rest of the operators

print(result)
```
