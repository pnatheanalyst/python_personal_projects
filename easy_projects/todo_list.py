# Create a list that allows receiving, adding, removing, and listing tasks.
# Create an empty list to allocate the tasks
tasks = []

# Create a menu to see the options available and choose one
while True:
    print("\n=== TO-DO LIST ===")
    print("1 - Add Tasks")
    print("2 - Enumerate Tasks")
    print("3 - Remove Tasks")
    print("4 - Leave")
    option = input("Choose an option: ")
    # If the user chooses '1', he will enter a task and the task will be added to the empty list
    if option == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        for task in tasks:
            print(task)
    # Else if the user chooses '2': if there is no tasks, the user will see a message to add tasks but if there's tasks, they will be enumerated
    elif option == '2':
        if tasks == []:
            print("There are no tasks. Add tasks first.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")
    # Else if the user chooses '2': if there is no tasks, the user will see a message to add tasks but if there's tasks, the user will be asked which of them they want to remove.
    elif option == '3':
        if tasks == []:
            print("There are no tasks. Add tasks first.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")
            removal = int(input("Which one would you like to remove? (Select the number of the task): "))
            index = removal - 1
            removed_task = tasks.pop(index)
            print("\nRemoved task!")
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")   
    # Else if the option is '4', there will be a polite message bidding farewells and the program will stop running        
    elif option == '4':
       print("Thank you for using our app!")
       break
    # If the user enters anything but 1, 2, 3 or 4, there will be a message indicating the user that there is an error
    else:
        print("Error. Try again.") 