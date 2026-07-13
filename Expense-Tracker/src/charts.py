"""
charts.py
----------
This module creates different charts for expense analysis.
The charts are automatically saved in the 'charts' folder.
"""

# Import required libraries
import os
import matplotlib.pyplot as plt

# Import the DataFrame generator
from reports import get_dataframe

# Folder where charts will be saved
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CHART_FOLDER = os.path.join(BASE_DIR, "charts")


# Create charts folder if it doesn't exist
def create_chart_folder():
    os.makedirs(CHART_FOLDER, exist_ok=True)


# Create a pie chart showing expense distribution by category
def category_pie_chart():

    # Load expense data
    df = get_dataframe()

    if df.empty:
        print("\nNo expense data available.")
        return

    # Create chart folder
    create_chart_folder()

    # Group expenses by category
    category_data = df.groupby("Category")["Amount"].sum()

    # Create pie chart
    plt.figure(figsize=(8, 8))

    plt.pie(
        category_data,
        labels=category_data.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Expense Distribution by Category")

    # Save chart
    plt.savefig(f"{CHART_FOLDER}/category_pie_chart.png")

    plt.show()

    print("\nPie chart saved successfully.")


# Create a bar chart for category-wise expenses
def category_bar_chart():

    df = get_dataframe()

    if df.empty:
        print("\nNo expense data available.")
        return

    create_chart_folder()

    category_data = df.groupby("Category")["Amount"].sum()

    plt.figure(figsize=(10, 6))

    plt.bar(
        category_data.index,
        category_data.values
    )

    plt.title("Category-wise Expenses")

    plt.xlabel("Category")

    plt.ylabel("Amount (₹)")

    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.savefig(f"{CHART_FOLDER}/category_bar_chart.png")

    plt.show()

    print("\nBar chart saved successfully.")


# Create a monthly expense trend line chart
def monthly_line_chart():

    df = get_dataframe()

    if df.empty:
        print("\nNo expense data available.")
        return

    create_chart_folder()

    # Extract Year-Month
    df["Month"] = df["Date"].dt.to_period("M").astype(str)

    monthly_data = df.groupby("Month")["Amount"].sum()

    plt.figure(figsize=(10, 6))

    plt.plot(
        monthly_data.index,
        monthly_data.values,
        marker="o"
    )

    plt.title("Monthly Expense Trend")

    plt.xlabel("Month")

    plt.ylabel("Amount (₹)")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(f"{CHART_FOLDER}/monthly_line_chart.png")

    plt.show()

    print("\nMonthly trend chart saved successfully.")


# Create a monthly expense comparison bar chart
def monthly_bar_chart():

    df = get_dataframe()

    if df.empty:
        print("\nNo expense data available.")
        return

    create_chart_folder()

    df["Month"] = df["Date"].dt.to_period("M").astype(str)

    monthly_data = df.groupby("Month")["Amount"].sum()

    plt.figure(figsize=(10, 6))

    plt.bar(
        monthly_data.index,
        monthly_data.values
    )

    plt.title("Monthly Expense Comparison")

    plt.xlabel("Month")

    plt.ylabel("Amount (₹)")

    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.savefig(f"{CHART_FOLDER}/monthly_bar_chart.png")

    plt.show()

    print("\nMonthly bar chart saved successfully.")


# Generate all charts together
def generate_all_charts():

    category_pie_chart()

    category_bar_chart()

    monthly_line_chart()

    monthly_bar_chart()

    print("\nAll charts generated successfully.")