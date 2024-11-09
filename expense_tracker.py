import json
import os
from datetime import datetime

# Define the file name to store expenses
FILENAME = "expenses.json"

# Load existing expenses from the file (if available)
def load_expenses():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

# Save expenses to the file
def save_expenses(expenses):
    with open(FILENAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    try:
        # Validate date format
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    description = input("Enter a description: ")
    category = input("Enter the category (e.g., Food, Transport, Utilities): ")
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    
    expense = {
        "date": date,
        "description": description,
        "category": category,
        "amount": amount
    }
    
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

# View all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- Expense List ---")
    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. Date: {expense['date']}, Description: {expense['description']}, "
              f"Category: {expense['category']}, Amount: ${expense['amount']:.2f}")

# Delete an expense
def delete_expense():
    view_expenses()
    if not expenses:
        return

    try:
        index = int(input("Enter the number of the expense to delete: ")) - 1
        if 0 <= index < len(expenses):
            removed_expense = expenses.pop(index)
            save_expenses(expenses)
            print(f"Deleted expense: {removed_expense}")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main function to run the expense tracker
def main():
    print("Welcome to the Expense Tracker!")
    global expenses
    expenses = load_expenses()
    
    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

# Run the expense tracker
if __name__ == "__main__":
    main()
