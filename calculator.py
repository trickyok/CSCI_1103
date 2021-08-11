# calculator.py
# Gage Farmer
# 7/17/2021


def main():
    
    # If True, user will be asked if they want to make another
    # calculation, and the program restarts.
    repeat = True

    # Gets desired operation from user
    operation = input("Please select one option: add/subtract/multiply/divide: ")

    # Confirms chosen operation
    print("You chose " + operation + ".")

    # Gets numbers from user
    a = input("What is the first number? ")
    b = input("What is the second number? ")

    # Incorrect variable type handler
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print("One of the numbers you have entered are invalid, please try again.")
        rpt = input("Would you like to make another calculation? (Y/N): ")
        if rpt.lower() == "y":
            print()
            main()
        else:
            quit()

    # Long and annoying set of 'if' statements for the operations because I
    # can't be bothered to make a switch case type thing
    # They all just calculate the result then print the final formatted statement
    if operation == "add":
        result = a + b
        print(str(a) + " + " + str(b) + " = " + str(result))
    elif operation == "subtract":
        result = a - b
        print(str(a) + " - " + str(b) + " = " + str(result))
    elif operation == "multiply":
        result = a * b
        print(str(a) + " * " + str(b) + " = " + str(result))
    elif operation == "divide":
        result = a / b
        print(str(a) + " / " + str(b) + " = " + str(result))

    # Invalid operation handler
    else:
        print("The option you chose (" + operation + ") is not valid, please try again.")
        rpt = input("Would you like to make another calculation? (Y/N): ")
        if rpt.lower() == "y":
            print()
            main()
        else:
            quit()

    if repeat:
        rpt = input("Would you like to make another calculation? (Y/N): ")
        if rpt.lower() == "y":
            print()
            main()


main()
