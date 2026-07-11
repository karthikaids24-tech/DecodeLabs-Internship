# 📝 Python To-Do List Application

A professional Command-Line To-Do List application built using **Python** as part of my **DecodeLabs Python Developer Internship**.

This application helps users efficiently manage daily tasks with features like task creation, updates, searching, statistics, CSV export, and JSON data storage.

---

## 🚀 Features

- ✅ Add New Tasks
- 📋 View All Tasks
- ✏️ Update Existing Tasks
- ✔️ Mark Tasks as Completed
- 🗑 Delete Tasks
- 🔍 Search Tasks
- 📊 Task Statistics
- ⭐ Priority Levels (High / Medium / Low)
- 📅 Created Date
- ⏰ Due Date
- 🚨 View Overdue Tasks
- 📂 Sort Tasks by Priority
- 💾 Automatic JSON Data Storage
- 📄 Export Tasks to CSV
- 🎨 Colored Terminal Interface (Colorama)
- ✅ Input Validation

---

## 📁 Project Structure

```
python-todo-list/
│
├── main.py
├── task_manager.py
├── storage.py
├── utils.py
├── tasks.json
├── tasks.csv
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── tests/
│   ├── __init__.py
│   └── test_task_manager.py
│
└── screenshots/
```

---

## 🛠 Technologies Used

- Python 3.x
- JSON
- CSV
- Colorama

---

## 📦 Installation

### Clone the repository

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python main.py
```

or

```bash
py main.py
```

---

## 📌 Menu

```
1. Add Task
2. View Tasks
3. Update Task
4. Complete Task
5. Delete Task
6. Search Task
7. Statistics
8. Sort Tasks by Priority
9. View Overdue Tasks
10. Export Tasks to CSV
11. Exit
```

---

## 📊 CSV Export

The application can export all tasks into a CSV file.

Generated file:

```
tasks.csv
```

Example:

| Task | Priority | Status | Created Date | Due Date |
|------|----------|--------|--------------|----------|
| Complete Assignment | High | Pending | 09-07-2026 | 15-07-2026 |

---

## 💾 Data Storage

All tasks are stored locally inside:

```
tasks.json
```

Example:

```json
[
    {
        "task": "Complete Python Project",
        "priority": "High",
        "completed": false,
        "created": "09-07-2026",
        "due": "15-07-2026"
    }
]
```

---

## 📷 Screenshots

Add screenshots of your application inside the **screenshots** folder.

Example:

```
screenshots/
│
├── home.png
├── add_task.png
├── statistics.png
└── export_csv.png
```

---

## 🎯 Learning Outcomes

This project helped me understand:

- Python Functions
- Modular Programming
- File Handling
- JSON Operations
- CSV Operations
- Exception Handling
- Input Validation
- CLI Application Development
- Git & GitHub

---

## 🚀 Future Improvements

- GUI using Tkinter
- SQLite Database Support
- Login System
- Task Categories
- Task Reminders
- Dark Mode UI
- Export to PDF
- Email Notifications
- Cloud Sync

---

## 👨‍💻 Author

**Jai Krithik R**

B.Tech Artificial Intelligence & Data Science

DecodeLabs Python Developer Intern

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It motivates me to build more open-source projects.
