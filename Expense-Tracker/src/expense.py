"""
expense.py
----------
This module defines the Expense class used to represent
a single expense record in the Expense Tracker application.
"""

# Import dataclass to automatically create constructor and other methods
from dataclasses import dataclass


# Create a dataclass for storing expense information
@dataclass
class Expense:
    # Unique ID for each expense
    expense_id: int

    # Date of the expense (YYYY-MM-DD)
    date: str

    # Expense category (Food, Travel, Shopping, etc.)
    category: str

    # Short description of the expense
    description: str

    # Expense amount
    amount: float

    # Convert the Expense object into a dictionary
    # This is useful when saving data to a CSV file
    def to_dict(self):
        return {
            "ID": self.expense_id,
            "Date": self.date,
            "Category": self.category,
            "Description": self.description,
            "Amount": self.amount
        }

    # Create an Expense object from a dictionary
    # This is useful when loading data from a CSV file
    @classmethod
    def from_dict(cls, data):
        return cls(
            expense_id=int(data["ID"]),
            date=data["Date"],
            category=data["Category"],
            description=data["Description"],
            amount=float(data["Amount"])
        )

    # Return a formatted string when printing an Expense object
    def __str__(self):
        return (
            f"[{self.expense_id}] "
            f"{self.date} | "
            f"{self.category:<15} | "
            f"{self.description:<25} | "
            f"₹{self.amount:.2f}"
        )