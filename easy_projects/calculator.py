# Build a basic calculator with Python

# Doing a menu with the four operations
while True:
    print("\n=== CALCULATOR ===")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Leave")
    print()
    # Ask the user to insert the option according to the menu above
    option = input("Choose an operation: ")
    # If the choice is not on the menu, it needs to show a message indicating that there's an error and goes back to the loop
    if option not in ['1', '2', '3', '4', '5']:
        print("Error. Try Again.")
        continue
    # Else if the option is '1', it will ask for the first and second number and finally show the result (Addition)
    elif option == '1':
        num_one = float(input("Type the first number: "))
        num_two = float(input("Type the second number: "))
        addition = num_one + num_two
        print(f"The addition of {round(num_one)} and {round(num_two)} is: {round(addition)}.")
    # Else if the option is '2', it will ask for the first and second number and finally show the result (Subtraction)
    elif option == '2':
        num_one = float(input("Type the first number: "))
        num_two = float(input("Type the second number: "))
        subtraction = num_one - num_two
        print(f"The subtraction of {round(num_one)} and {round(num_two)} is: {round(subtraction)}.")
    # Else if the option is '3', it will ask for the first and second number and finally show the result (Multiplication)
    elif option == '3':
        num_one = float(input("Type the first number: "))
        num_two = float(input("Type the second number: "))
        multiplication = num_one * num_two
        print(f"The multiplication of {round(num_one)} and {round(num_two)} is: {round(multiplication)}.")
    # Else if the option is '4', it will ask for the first and second number and finally show the result (Division)
    elif option == '4':
        num_one = float(input("Type the first number: "))
        num_two = float(input("Type the second number: "))
        division = num_one / num_two
        print(f"The division of {num_one} and {num_two} is: {round(division, 2)}.")
    # # Else if the option is '5', the program stops and exits
    elif option == '5':
        print("Thank You!")
        break