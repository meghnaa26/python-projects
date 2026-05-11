tasks=["learn python","learn java","learn html"]
choice=""
while choice != "4":
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Quit")
    choice = input("Enter your choice: ")
    
    if choice=="1":
        task = input("Enter the task: ")
        tasks.append(task)
    elif choice=="2":
        for task in tasks:
            print(task)
    elif choice=="3":
        task= input("Which task to remove: ")
        if task in tasks:
            tasks.remove(task)
        else:
            print("The task is not found in the list")
    elif choice == "4":
        print("GOODBYE!")
    else:
        print("Please enter a valid choice")
