"""
reports.py
----------
This module generates reports and summaries from expense data.
"""

# Import pandas for data analysis
import pandas as pd

# Import the function to load expenses
from storage import load_expenses


# Convert expense objects into a Pandas DataFrame
def get_dataframe():

    # Load all expenses
    expenses = load_expenses()

    # If no expenses are available
    if not expenses:
        return pd.DataFrame()

    # Convert each Expense object into a dictionary
    data = [expense.to_dict() for expense in expenses]

    # Create DataFrame
    df = pd.DataFrame(data)

    # Convert Amount column into numeric values
    df["Amount"] = pd.to_numeric(df["Amount"])

    # Convert Date column into datetime format
    df["Date"] = pd.to_datetime(df["Date"])

    return df


# Display all expenses
def show_all_expenses():

    df = get_dataframe()

    if df.empty:
        print("\nNo expenses found.")
        return

    print("\n========== ALL EXPENSES ==========\n")
    print(df.to_string(index=False))


# Calculate total expense
def total_expense():

    df = get_dataframe()

    if df.empty:
        return 0

    return df["Amount"].sum()


# Display category-wise summary
def category_summary():

    df = get_dataframe()

    if df.empty:
        print("\nNo expenses available.")
        return

    summary = df.groupby("Category")["Amount"].sum()

    print("\n====== CATEGORY SUMMARY ======\n")
    print(summary)


# Display monthly summary
def monthly_summary():

    df = get_dataframe()

    if df.empty:
        print("\nNo expenses available.")
        return

    # Extract Year-Month
    df["Month"] = df["Date"].dt.to_period("M")

    summary = df.groupby("Month")["Amount"].sum()

    print("\n====== MONTHLY SUMMARY ======\n")
    print(summary)


# Search expenses by category
def search_category(category):

    df = get_dataframe()

    if df.empty:
        print("\nNo expenses available.")
        return

    result = df[df["Category"].str.lower() == category.lower()]

    if result.empty:
        print("\nNo matching category found.")
    else:
        print(result.to_string(index=False))


# Calculate average expense
def average_expense():

    df = get_dataframe()

    if df.empty:
        return 0

    return df["Amount"].mean()


# Find highest expense
def highest_expense():

    df = get_dataframe()

    if df.empty:
        return None

    return df.loc[df["Amount"].idxmax()]


# Find lowest expense
def lowest_expense():

    df = get_dataframe()

    if df.empty:
        return None

    return df.loc[df["Amount"].idxmin()]


# Display complete statistics
def expense_statistics():

    df = get_dataframe()

    if df.empty:
        print("\nNo expenses available.")
        return

    print("\n========== EXPENSE STATISTICS ==========\n")

    print(f"Total Expense      : ₹{total_expense():.2f}")
    print(f"Average Expense    : ₹{average_expense():.2f}")

    highest = highest_expense()
    lowest = lowest_expense()

    print("\nHighest Expense")
    print(highest)

    print("\nLowest Expense")
    print(lowest)

    print("\nCategory-wise Summary")
    print(df.groupby("Category")["Amount"].sum())

    print("\nMonthly Summary")
    monthly = df.groupby(df["Date"].dt.to_period("M"))["Amount"].sum()
    print(monthly)