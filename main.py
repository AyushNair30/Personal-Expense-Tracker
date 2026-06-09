file="expenses.txt" 
def main():
    welcome()

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
                expenses.append({"Category":category,"Amount":amount})
    except FileNotFoundError:
        print("File doesnt exist")
    except Exception as e:
        print(e)

def save_expenses(expenses):
    with open(file,"a") as f:
        for value in expenses:
            f.write(f"{value["Category"]},{value["Amount"]}")

def add_expenses(expenses):
    try:
        category=input("Enter your category: ")
        amount=float(input("Enter your amount"))
        expenses.append({"Category":category,"Amount":amount})
        save_expenses(expenses)
    except ValueError:
        print("Invalid Amount")
    except Exception as e:
        print(e)

def view_expense(expenses):
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












if __name__=="__main__":
    main()