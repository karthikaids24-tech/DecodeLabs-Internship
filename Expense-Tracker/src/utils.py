"""
utils.py
---------
This module contains helper functions used throughout
the Expense Tracker application.
"""

# Import required modules
import os
from datetime import datetime


# List of available expense categories
CATEGORIES = [
    "Food",
    "Travel",
    "Shopping",
    "Medical",
    "Bills",
    "Education",
    "Entertainment",
    "Others"
]


# Clear the terminal screen
def clear_screen():

    # Windows
    if os.name == "nt":
        os.system("cls")

    # Linux / macOS
    else:
        os.system("clear")


# Pause the program until the user presses Enter
def pause():

    input("\nPress Enter to continue...")


# Display the main menu
def display_menu():

    print("\n" + "=" * 45)
    print("         PERSONAL EXPENSE TRACKER")
    print("=" * 45)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Search Expense")
    print("6. Category Summary")
    print("7. Monthly Summary")
    print("8. Expense Statistics")
    print("9. Budget Status")
    print("10. Set Budget")
    print("11. Generate Charts")
    print("12. Exit")
    print("=" * 45)


# Validate date format
def validate_date(date):

    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True

    except ValueError:
        return False


# Validate amount entered by the user
def validate_amount(amount):

    try:

        amount = float(amount)

        if amount <= 0:
            return False

        return True

    except ValueError:
        return False


# Display available categories
def show_categories():

    print("\nAvailable Categories\n")

    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category}")


# Get category from user
def get_category():

    while True:

        show_categories()

        choice = input("\nChoose Category Number: ")

        try:

            choice = int(choice)

            if 1 <= choice <= len(CATEGORIES):
                return CATEGORIES[choice - 1]

            else:
                print("\nInvalid category number.")

        except ValueError:
            print("\nPlease enter a valid number.")


# Get valid date from user
def get_date():

    while True:

        date = input("Enter Date (YYYY-MM-DD): ")

        if validate_date(date):
            return date

        print("Invalid date format.")


# Get valid amount from user
def get_amount():

    while True:

        amount = input("Enter Amount: ₹")

        if validate_amount(amount):
            return float(amount)

        print("Amount must be greater than 0.")


# Get description from user
def get_description():

    while True:

        description = input("Enter Description: ").strip()

        if description:
            return description

        print("Description cannot be empty.")


# Get expense ID from user
def get_expense_id():

    while True:

        expense_id = input("Enter Expense ID: ")

        try:
            return int(expense_id)

        except ValueError:
            print("Please enter a valid ID.")


# Display a success message
def success(message):

    print(f"\n✅ {message}")


# Display an error message
def error(message):

    print(f"\n❌ {message}")


# Display an information message
def info(message):

    print(f"\nℹ {message}")


# Display a decorative heading
def heading(title):

    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)