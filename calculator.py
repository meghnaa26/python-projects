# Calculator
# Built by Meghna
# A calculator that performs +, -, *, /, %, //, ** operations
# Features: division by zero handling, invalid input handling, repeat optioncalculate_again="yes"
while calculate_again == "yes":
    valid = True
    n1 = float(input("Enter the first number: "))
    o = input("Enter the operation want to perform(+,-,*,/,%,**,//): ")
    n2 = float(input("Enter the second number: "))
    result = 0
    if o == "+":
        result = n1 + n2
    elif o == "-":
        result = n1 - n2
    elif o == "*":
        result = n1 * n2
    elif o == "/":
        if n2 == 0:
            print("Not valid")
        else:
            result = n1 / n2
    elif o == "%":
        if n2 == 0:
            print("Not valid")
        else:
            result = n1 % n2
    elif o == "//":
        if n2 == 0:
            print("Not valid")
        else:
            result = n1 // n2
    elif o == "**":
        result = n1 ** n2
    else:
        print("Enter a valid operation")
        valid = False
    if valid == True:
        print("The result is",result)
    calculate_again=input("Do you want to perform more operations: ")
