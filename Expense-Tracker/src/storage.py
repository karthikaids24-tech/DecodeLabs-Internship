"""
storage.py
----------
This module handles all CSV file operations such as:
1. Creating the CSV file
2. Loading expenses
3. Saving expenses
4. Updating expenses
5. Deleting expenses
"""

# Import required modules
import csv
import os

# Import the Expense class
from expense import Expense

# Path of the CSV file

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")

FILE_PATH = os.path.join(DATA_DIR, "expenses.csv")


# Create the CSV file if it does not already exist
def initialize_file():
    if not os.path.exists(FILE_PATH):

        # Create the data folder if it doesn't exist
        os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)

        # Create CSV file with column headers
        with open(FILE_PATH, mode="w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "ID",
                "Date",
                "Category",
                "Description",
                "Amount"
            ])


# Load all expenses from the CSV file
def load_expenses():

    # Make sure the file exists
    initialize_file()

    expenses = []

    # Read all records from CSV
    with open(FILE_PATH, mode="r", newline="") as file:

        reader = csv.DictReader(file)

        # Convert each row into an Expense object
        for row in reader:
            expenses.append(Expense.from_dict(row))

    return expenses


# Save all expenses to the CSV file
def save_expenses(expenses):

    # Open CSV file in write mode
    with open(FILE_PATH, mode="w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "ID",
                "Date",
                "Category",
                "Description",
                "Amount"
            ]
        )

        # Write column headers
        writer.writeheader()

        # Write each expense
        for expense in expenses:
            writer.writerow(expense.to_dict())


# Generate the next available Expense ID
def get_next_id():

    expenses = load_expenses()

    # If no expenses exist, start from 1
    if not expenses:
        return 1

    # Return one more than the largest existing ID
    return max(exp.expense_id for exp in expenses) + 1


# Add a new expense
def add_expense(expense):

    expenses = load_expenses()

    expenses.append(expense)

    save_expenses(expenses)


# Delete an expense using its ID
def delete_expense(expense_id):

    expenses = load_expenses()

    updated_expenses = [
        expense
        for expense in expenses
        if expense.expense_id != expense_id
    ]

    save_expenses(updated_expenses)


# Update an existing expense
def update_expense(updated_expense):

    expenses = load_expenses()

    for index, expense in enumerate(expenses):

        if expense.expense_id == updated_expense.expense_id:
            expenses[index] = updated_expense
            break

    save_expenses(expenses)


# Search for an expense by ID
def search_expense(expense_id):

    expenses = load_expenses()

    for expense in expenses:

        if expense.expense_id == expense_id:
            return expense

    return None