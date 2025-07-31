from datetime import date

EXPENSE_TRACKER = "expenses.txt"

def add_expense():
    today = date.today()
    amount = float(input('Enter the amount: '))
    category = input('Enter a category: ')
    note = input('Enter a note: ')
    
    with open(EXPENSE_TRACKER, "a") as file:
        file.write(f"{today},{amount},{category},{note}\n")
    
    print(f"✅ Expense of {amount} added.")


def view_expenses():
    with open(EXPENSE_TRACKER, "r") as file:
        for line in file.readlines():
            today,amount,category,note = line.strip().split(",")
            print(f"Date: {today}, Amount: {amount}, Category: {category}, Note: {note}")


def delete_expense():
    with open(EXPENSE_TRACKER, "r") as file:
        lines = file.readlines()
        for i,line in enumerate(lines,start=1):
            print(f"{i}. {line.strip()}")
        try:
            choice=int(input("Enter the number of the expense you want to delete: "))
            if 1 <= choice  <= len(lines):
                delete_exprense = lines.pop(choice-1)
                with open(EXPENSE_TRACKER, "w") as file:
                    file.writelines(lines)
                print(f"✅ Expense of {delete_exprense} deleted.")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def filter_expenses():
    filter_type = input("Enter the filter type (category or date): ")

    with open(EXPENSE_TRACKER,"r") as file:
        lines = file.readlines()

        if filter_type == "category":
            categories = input("Enter the category: ")
            for line in lines:
                today,amount,category,note = line.strip().split(",")
                if category == categories:
                    print(f"Date: {today}, Amount: {amount}, Category: {category}, Note: {note}")

        elif filter_type == "date":
            date_input = input("Enter the date (YYYY-MM-DD): ")
            for line in lines:
                today,amount,category,note = line.strip().split(",")
                if today == date_input:
                    print(f"Date: {today}, Amount: {amount}, Category: {category}, Note: {note}")

        else:
            print("Invalid filter type. Please try again.")

def main():
    while True:
        print("\n Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Filter Expenses")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            filter_expenses()
        elif choice == "5":
            print(" Exiting Expense Tracker. Goodbye!")
            break
        else:
            print(" Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
