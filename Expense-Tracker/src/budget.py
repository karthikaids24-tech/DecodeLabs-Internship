"""
budget.py
----------
This module manages the monthly budget for the Expense Tracker.
"""

# Import required modules
import json
import os

# Import the function to calculate total expenses
from reports import total_expense

# Path to the budget file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")

BUDGET_FILE = os.path.join(DATA_DIR, "budget.json")


# Create the budget file if it does not exist
def initialize_budget():

    # Create the data folder if needed
    os.makedirs(os.path.dirname(BUDGET_FILE), exist_ok=True)

    # Create budget file with default value
    if not os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, "w") as file:
            json.dump({"budget": 0}, file)


# Set a new monthly budget
def set_budget(amount):

    initialize_budget()

    with open(BUDGET_FILE, "w") as file:
        json.dump({"budget": amount}, file)

    print(f"\nMonthly budget set to ₹{amount:.2f}")


# Get the current budget
def get_budget():

    initialize_budget()

    with open(BUDGET_FILE, "r") as file:
        data = json.load(file)

    return data["budget"]


# Display the current budget
def view_budget():

    budget = get_budget()

    print(f"\nCurrent Monthly Budget : ₹{budget:.2f}")


# Calculate the remaining budget
def remaining_budget():

    budget = get_budget()

    spent = total_expense()

    return budget - spent


# Calculate the percentage of budget used
def budget_percentage():

    budget = get_budget()

    if budget == 0:
        return 0

    spent = total_expense()

    return (spent / budget) * 100


# Display complete budget status
def budget_status():

    budget = get_budget()

    spent = total_expense()

    remaining = remaining_budget()

    percentage = budget_percentage()

    print("\n========== BUDGET STATUS ==========")

    print(f"Monthly Budget : ₹{budget:.2f}")

    print(f"Total Spent    : ₹{spent:.2f}")

    print(f"Remaining      : ₹{remaining:.2f}")

    print(f"Budget Used    : {percentage:.2f}%")

    # Display budget warnings
    if budget == 0:
        print("\nNo budget has been set.")

    elif spent > budget:
        print("\nBudget Exceeded!")

        print(f"You have exceeded your budget by ₹{spent - budget:.2f}")

    elif percentage >= 80:
        print("\nWarning!")

        print("You have used more than 80% of your monthly budget.")

    else:
        print("\nGreat! Your spending is within the budget.")


# Reset the budget to zero
def reset_budget():

    set_budget(0)

    print("\nBudget has been reset successfully.")