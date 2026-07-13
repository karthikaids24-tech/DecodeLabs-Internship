"""
test_expense.py
---------------
Unit tests for the Expense class.
"""

# Import unittest framework
import unittest

# Import Expense class
from src.expense import Expense


class TestExpense(unittest.TestCase):

    # Test object creation
    def test_create_expense(self):

        expense = Expense(
            1,
            "2026-07-13",
            "Food",
            "Burger",
            250
        )

        self.assertEqual(expense.expense_id, 1)
        self.assertEqual(expense.date, "2026-07-13")
        self.assertEqual(expense.category, "Food")
        self.assertEqual(expense.description, "Burger")
        self.assertEqual(expense.amount, 250)


    # Test dictionary conversion
    def test_to_dict(self):

        expense = Expense(
            2,
            "2026-07-13",
            "Travel",
            "Metro",
            60
        )

        expected = {
            "ID": 2,
            "Date": "2026-07-13",
            "Category": "Travel",
            "Description": "Metro",
            "Amount": 60
        }

        self.assertEqual(expense.to_dict(), expected)


    # Test object creation from dictionary
    def test_from_dict(self):

        data = {
            "ID": "3",
            "Date": "2026-07-13",
            "Category": "Shopping",
            "Description": "Shoes",
            "Amount": "1200"
        }

        expense = Expense.from_dict(data)

        self.assertEqual(expense.expense_id, 3)
        self.assertEqual(expense.category, "Shopping")
        self.assertEqual(expense.description, "Shoes")
        self.assertEqual(expense.amount, 1200.0)


    # Test string representation
    def test_string_representation(self):

        expense = Expense(
            4,
            "2026-07-13",
            "Bills",
            "Electricity",
            1800
        )

        result = str(expense)

        self.assertIn("Bills", result)
        self.assertIn("Electricity", result)
        self.assertIn("1800.00", result)


# Run all test cases
if __name__ == "__main__":
    unittest.main()