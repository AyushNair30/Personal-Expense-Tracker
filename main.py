def main():
    file="expenses.txt" 
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












if __name__=="__main__":
    main()