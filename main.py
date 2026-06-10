file="expenses.txt" 
def main():
    welcome()
    expenses=load_expenses()
    while True:
        try:
            choice=int(input("Enter your choice: "))
            match choice:
                case 1:
                    add_expenses(expenses)
                case 2:
                    view_expenses(expenses)
                case 3:
                    total_expense(expenses)
                case 4:
                    remove_expenses(expenses)
                case 5:
                    print("Program ended.")
                    break
    
        except ValueError:
            print("Enter a valid choice.")

def welcome():
    print("Personal Expense Tracker")
    print("------------------------")
    print("Menu:")
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Remove Expense")
    print("5. Exit")
    print("------------------------")

def load_expenses():
    expenses=[]
    try:
        with open(file,"r") as f:
            for line in f:
                category,amount=line.strip().split(",")
                expenses.append({"Category":category,"Amount":float(amount)})
    except FileNotFoundError:
        print("File doesnt exist")
    except Exception as e:
        print(e)
    return expenses

def save_expenses(expenses):
    with open(file,"w") as f:
        for value in expenses:
            f.write(f"{value["Category"]},{value["Amount"]}\n")

def add_expenses(expenses):
    while True:
        try:
            category=input("Enter your category: ")
            amount=float(input("Enter your amount: "))
            expenses.append({"Category":category,"Amount":amount})
            save_expenses(expenses)
            print("Expense added successfully")
            break
        except ValueError:
            print("Invalid Amount")
        except Exception as e:
            print(e)

def view_expenses(expenses):
    if not expenses:
        print("No expenses to view.")  
        return

    print("Your Expenses:")
    i=1
    for e in expenses:
        print(f"{i}. {e["Category"]}={e["Amount"]}")
        i+=1

def total_expense(expenses):
    total=0
    for e in expenses:
        total+=e["Amount"]
    print(f"Your total Expenditure is {total}")


def remove_expenses(expenses):
    if not expenses:
        print("No expenses to remove.")
        return
    
    view_expenses(expenses)

    while True:
        category=input("Enter the category you want to remove: ").lower()
        flag=0
        for expense in expenses:
            if expense["Category"]==category:
                expenses.remove(expense)
                print(f"{category} removed successfully.")
                flag=1
                break
        if flag==0:
            print("Invalid Category")
        break
    
    save_expenses(expenses)
    view_expenses(expenses)


if __name__=="__main__":
    main()