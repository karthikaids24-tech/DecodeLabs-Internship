# 💰 Personal Expense Tracker

A modular **Python-based Personal Expense Tracker** that helps users manage their daily expenses efficiently. This application allows users to add, view, update, delete, and search expenses while providing detailed reports, budget tracking, and graphical visualizations.

The project is built using **Python**, **Pandas**, and **Matplotlib**, following a modular architecture and Object-Oriented Programming (OOP) principles.

---

## 📌 Features

- ➕ Add new expenses
- 📋 View all expenses
- ✏️ Update existing expenses
- ❌ Delete expenses
- 🔍 Search expenses by Expense ID
- 📂 Category-wise expense summary
- 📅 Monthly expense summary
- 📊 Expense statistics
- 💰 Set monthly budget
- ⚠️ Budget usage and warning system
- 📈 Generate expense charts
- 💾 Store data in CSV format
- 🧪 Unit testing
- 🏗️ Modular project structure

---

## 📂 Project Structure

```
Expense-Tracker/
│
├── data/
│   ├── expenses.csv
│   └── budget.json
│
├── charts/
│   ├── category_bar_chart.png
│   ├── category_pie_chart.png
│   ├── monthly_bar_chart.png
│   └── monthly_line_chart.png
│
├── src/
│   ├── expense.py
│   ├── storage.py
│   ├── reports.py
│   ├── charts.py
│   ├── budget.py
│   ├── utils.py
│   └── main.py
│
├── tests/
│   └── test_expense.py
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## 🛠️ Technologies Used

- Python 3
- Pandas
- Matplotlib
- CSV
- JSON
- unittest

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/expense-tracker.git
```

### 2. Navigate to the Project Directory

```bash
cd expense-tracker
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Navigate to the `src` folder:

```bash
cd src
```

Run the application:

```bash
python main.py
```

---

## 🧪 Running Tests

From the project root:

```bash
python -m unittest tests/test_expense.py
```

---

## 🖥️ Main Menu

```
=========================================
        PERSONAL EXPENSE TRACKER
=========================================

1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Search Expense
6. Category Summary
7. Monthly Summary
8. Expense Statistics
9. Budget Status
10. Set Budget
11. Generate Charts
12. Exit
```

---

## 📊 Generated Reports

The application provides:

- Total Expense
- Category-wise Summary
- Monthly Summary
- Expense Statistics
- Budget Status

---

## 📈 Charts Generated

The following charts are automatically generated:

- 🥧 Category-wise Pie Chart
- 📊 Category-wise Bar Chart
- 📈 Monthly Expense Trend
- 📉 Monthly Expense Comparison

Generated charts are stored inside the **charts/** folder.

---

## 💰 Budget Tracking

Users can:

- Set a monthly budget
- View current budget
- Check remaining balance
- Monitor budget usage percentage
- Receive warning when spending exceeds 80%
- Receive alert when budget is exceeded

---

## 💾 Data Storage

Expenses are stored inside:

```
data/expenses.csv
```

Budget information is stored inside:

```
data/budget.json
```

---

## 🧠 Python Concepts Used

- Object-Oriented Programming (OOP)
- Modular Programming
- Functions
- File Handling
- CSV Handling
- JSON Handling
- Exception Handling
- Dataclasses
- Pandas Data Analysis
- Matplotlib Visualization

---

## 🚀 Future Enhancements

- User Authentication
- SQLite Database Integration
- PDF Report Export
- Excel Export
- Interactive Dashboard
- Tkinter GUI
- Flask Web Version
- Cloud Backup
- Email Reports
- Multi-user Support

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Jai Krithik R**

**B.Tech – Artificial Intelligence & Data Science**

### Connect with Me

- LinkedIn: www.linkedin.com/in/jai-krithik-r-lucky

---

## ⭐ Show Your Support

If you found this project useful:

- ⭐ Star this repository
- 🍴 Fork it
- 🛠️ Contribute improvements
- 💬 Share your feedback

---

### Happy Coding! 🚀