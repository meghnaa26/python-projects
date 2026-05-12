import json
def save_data():
    global salary, expenses
    data = {
        "salary":salary,
        "expenses":expenses
    }
    with open("expenses.json","w") as file:
        json.dump(data,file)

def load_data():
    global salary, expenses
    try:
        with open("expenses.json","r") as file:
            data = json.load(file)
            salary = data["salary"]
            expenses = data["expenses"]
    except:
        pass
    
choice=""

salary = 0
def add_salary():
    global salary
    salary = float(input("Enter your monthly salary: "))
    print("Salary of ₹", salary,"added successfully!")
    save_data()

category = ['Food','Transport','Medical','Bills/Loan/EMI','Entertainment','Savings','Other']
expenses =[]

def add_expenses():
    global expenses 
    
    print("Select category: ")
    for i in range(len(category)):
        print(i+1, "-", category[i])
        
    choice=int(input("Enter category number: "))
    selected=category[choice-1]
    amount = float(input("Enter amount₹: "))
    description = input("Enter description: ")
    
    expense = {
        "category":selected,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    print("Expenses added successfully!")
    save_data()
    
def view_expenses():
    if len(expenses)==0:
        print("No expenses added yet!")
    else:
        print("=== YOUR EXPENSES ===")
        for i in range(len(expenses)):
            print(i+1, expenses[i]["category"],"₹", expenses[i]["amount"],
      "-", expenses[i]["description"])
      
def view_summary():
    total = 0
    for expense in expenses:
        total += expense["amount"]
    remaining = salary - total
    print("=== SUMMARY ===")
    print("Monthly salary: ",salary)
    print("Total spent: ",total)
    print("Money remaining: ",remaining)
    
    print("--- Spent Per Category ---")
    for cat in category:
        cat_total =0
        for expense in expenses:
            if expense["category"]==cat:
                cat_total += expense["amount"]
        print(cat,"₹", cat_total)

def health_scale():
    if salary ==0:
        print("Please add salary first!")
        return
    total = 0
    for expense in expenses:
        total += expense["amount"]
        
    remaining = salary - total
    percentage = (remaining/salary)*100
        
    filled = int(percentage/10)
    empty = 10 - filled
    bar = "▮" *empty+ "▦"*  filled
        
    print("=== SPENDING HEALTH ===")
    print(f"[{bar}] {percentage: .1f}% remaining")
        
    if percentage >= 80:
        print("Excellent! You're saving well!")
    elif percentage >= 60:
        print(" Good! Keep it up!")
    elif percentage >= 40:
        print("Be Careful! Watch your spending!")
    elif percentage >= 20:
        print("Warning! You're overspending!")
    else:
        print("Danger! Critical spending level!")
        
load_data()

while choice !="6":
    print("=== EXPENSE MANAGER ===")
    print("1.Add salary")
    print("2.Add expenses")
    print("3.View expenses")
    print("4.View summary")
    print("5.Spending Health scale")
    print("6.Exit")
    
    choice=input("Enter your choice: ")
    
    if choice == '1':
        add_salary()
    elif choice == '2':
        add_expenses()
    elif choice == '3':
        view_expenses()
    elif choice == '4':
        view_summary()
    elif choice == '5':
        health_scale()
    elif choice == '6':
        print("Thank you for using our website.")
    else:
        print("Please enter a valid choice")
