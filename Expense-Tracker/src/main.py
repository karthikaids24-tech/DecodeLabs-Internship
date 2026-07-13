"""
main.py
--------
Main module of the Expense Tracker application.
This file connects all modules and provides
a menu-driven interface.
"""

# ==========================
# Import Required Modules
# ==========================

from expense import Expense

from storage import (
    load_expenses,
    add_expense,
    update_expense,
    delete_expense,
    search_expense,
    get_next_id
)

from reports import (
    show_all_expenses,
    category_summary,
    monthly_summary,
    expense_statistics
)

from charts import generate_all_charts

from budget import (
    set_budget,
    budget_status
)

from utils import (
    clear_screen,
    pause,
    display_menu,
    get_date,
    get_category,
    get_description,
    get_amount,
    get_expense_id,
    success,
    error
)


# ==========================
# Add Expense
# ==========================

def add_new_expense():

    print("\n========== ADD EXPENSE ==========\n")

    expense_id = get_next_id()

    date = get_date()

    category = get_category()

    description = get_description()

    amount = get_amount()

    expense = Expense(
        expense_id,
        date,
        category,
        description,
        amount
    )

    add_expense(expense)

    success("Expense added successfully.")

    pause()


# ==========================
# View Expenses
# ==========================

def view_expenses():

    print("\n========== ALL EXPENSES ==========\n")

    expenses = load_expenses()

    if not expenses:

        error("No expenses found.")

    else:

        for expense in expenses:
            print(expense)

    pause()
# ==========================
# Update Expense
# ==========================

def edit_expense():

    print("\n========== UPDATE EXPENSE ==========\n")

    # Get expense ID from user
    expense_id = get_expense_id()

    # Search for the expense
    expense = search_expense(expense_id)

    # Check whether expense exists
    if expense is None:

        error("Expense not found.")

        pause()

        return

    print("\nCurrent Expense Details\n")

    print(expense)

    print("\nEnter New Details\n")

    # Get updated information
    date = get_date()

    category = get_category()

    description = get_description()

    amount = get_amount()

    # Create updated Expense object
    updated = Expense(
        expense_id,
        date,
        category,
        description,
        amount
    )

    # Save updated expense
    update_expense(updated)

    success("Expense updated successfully.")

    pause()


# ==========================
# Delete Expense
# ==========================

def remove_expense():

    print("\n========== DELETE EXPENSE ==========\n")

    # Get expense ID
    expense_id = get_expense_id()

    # Search expense
    expense = search_expense(expense_id)

    if expense is None:

        error("Expense not found.")

        pause()

        return

    print("\nExpense Found\n")

    print(expense)

    # Ask confirmation
    choice = input("\nAre you sure you want to delete? (Y/N): ").strip().lower()

    if choice == "y":

        delete_expense(expense_id)

        success("Expense deleted successfully.")

    else:

        print("\nDeletion cancelled.")

    pause()


# ==========================
# Search Expense
# ==========================

def find_expense():

    print("\n========== SEARCH EXPENSE ==========\n")

    # Get expense ID
    expense_id = get_expense_id()

    # Search expense
    expense = search_expense(expense_id)

    if expense is None:

        error("Expense not found.")

    else:

        print("\nExpense Details\n")

        print(expense)

    pause()


# ==========================
# Category Summary
# ==========================

def show_category_summary():

    print("\n========== CATEGORY SUMMARY ==========\n")

    category_summary()

    pause()


# ==========================
# Monthly Summary
# ==========================

def show_monthly_summary():

    print("\n========== MONTHLY SUMMARY ==========\n")

    monthly_summary()

    pause()


# ==========================
# Expense Statistics
# ==========================

def show_statistics():

    print("\n========== EXPENSE STATISTICS ==========\n")

    expense_statistics()

    pause()
# ==========================
# Set Budget
# ==========================

def update_budget():

    print("\n========== SET MONTHLY BUDGET ==========\n")

    amount = get_amount()

    set_budget(amount)

    success("Monthly budget updated successfully.")

    pause()


# ==========================
# Budget Status
# ==========================

def show_budget_status():

    print("\n========== BUDGET STATUS ==========\n")

    budget_status()

    pause()


# ==========================
# Generate Charts
# ==========================

def create_charts():

    print("\n========== GENERATE CHARTS ==========\n")

    generate_all_charts()

    success("Charts generated successfully.")

    pause()


# ==========================
# Main Menu
# ==========================

def menu():

    while True:

        clear_screen()

        display_menu()

        choice = input("\nEnter your choice: ").strip()

        # --------------------------
        # Add Expense
        # --------------------------
        if choice == "1":

            clear_screen()

            add_new_expense()

        # --------------------------
        # View Expenses
        # --------------------------
        elif choice == "2":

            clear_screen()

            view_expenses()

        # --------------------------
        # Update Expense
        # --------------------------
        elif choice == "3":

            clear_screen()

            edit_expense()

        # --------------------------
        # Delete Expense
        # --------------------------
        elif choice == "4":

            clear_screen()

            remove_expense()

        # --------------------------
        # Search Expense
        # --------------------------
        elif choice == "5":

            clear_screen()

            find_expense()

        # --------------------------
        # Category Summary
        # --------------------------
        elif choice == "6":

            clear_screen()

            show_category_summary()

        # --------------------------
        # Monthly Summary
        # --------------------------
        elif choice == "7":

            clear_screen()

            show_monthly_summary()

        # --------------------------
        # Expense Statistics
        # --------------------------
        elif choice == "8":

            clear_screen()

            show_statistics()

        # --------------------------
        # Budget Status
        # --------------------------
        elif choice == "9":

            clear_screen()

            show_budget_status()

        # --------------------------
        # Set Budget
        # --------------------------
        elif choice == "10":

            clear_screen()

            update_budget()

        # --------------------------
        # Generate Charts
        # --------------------------
        elif choice == "11":

            clear_screen()

            create_charts()

        # --------------------------
        # Exit
        # --------------------------
        elif choice == "12":

            print("\nThank you for using Personal Expense Tracker.")

            print("Have a great day!")

            break

        # --------------------------
        # Invalid Choice
        # --------------------------
        else:

            error("Invalid choice. Please try again.")

            pause()


# ==========================
# Program Entry Point
# ==========================

def main():

    menu()


if __name__ == "__main__":

    main()