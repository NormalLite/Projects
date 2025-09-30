import pandas as pd
import os

file_name = "expenses.csv"

if os.path.exists(file_name):
    expenses = pd.read_csv(file_name)
else:
    columns = ["Date", "Category", "Description", "Amount"]
    expenses = pd.DataFrame(columns=columns)

def save_expenses():
    expenses.to_csv(file_name, index=False)

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Transport, etc.): ")
    description = input("Enter description: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return
    global expenses
    expenses = pd.concat([expenses, pd.DataFrame([[date, category, description, amount]], columns=expenses.columns)], ignore_index=True)
    save_expenses()
    print("Expense added and saved successfully!\n")

def view_expenses():
    if expenses.empty:
        print("No expenses recorded yet.\n")
    else:
        print("\nAll Expenses:")
        print(expenses.to_string(index=False))
        print()

def summary_by_category():
    if expenses.empty:
        print("No expenses recorded yet.\n")
    else:
        summary = expenses.groupby("Category")["Amount"].sum()
        print("\nExpense Summary by Category:")
        print(summary)
        print()

def main():
    while True:
        print("Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Summary by Category")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary_by_category()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

