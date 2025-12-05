import csv
import os

FILE_NAME = "expenses.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Description"])

def add_expense():
    try:
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([amount, description])

        print("Expense added successfully!\n")
    except ValueError:
        print("Invalid amount! Please enter a number.\n")

def view_expenses():
    print("\n----- All Expenses -----")
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()

def total_spending():
    total = 0
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            total += float(row[0])

    print(f"\nTotal Spending: ₹{total}\n")

def main():
    while True:
        print("----- Expense Tracker -----")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_spending()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option!\n")

if __name__ == "__main__":
    main()
