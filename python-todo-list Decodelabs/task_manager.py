from datetime import datetime
from utils import success, error, warning, info, title, line
import csv

# ===========================================
# VIEW TASKS
# ===========================================

def view_tasks(tasks):

    if not tasks:
        warning("\nNo tasks found.")
        return

    line()
    title("                YOUR TASKS")
    line()

    for i, task in enumerate(tasks, start=1):

        status = "Completed ✅" if task["completed"] else "Pending ⏳"

        print(f"""
Task ID      : {i}
Task         : {task['task']}
Priority     : {task['priority']}
Status       : {status}
Created Date : {task['created']}
Due Date     : {task['due']}
------------------------------------------------------------
""")


# ===========================================
# ADD TASK
# ===========================================

def add_task(tasks):

    line()
    title("ADD NEW TASK")
    line()

    while True:

        task_name = input("Task Name : ").strip()

        if task_name:
            break

        error("Task cannot be empty.")

    while True:

        priority = input(
            "Priority (High/Medium/Low): "
        ).capitalize().strip()

        if priority in ["High", "Medium", "Low"]:
            break

        error("Choose High, Medium or Low.")

    while True:

        due = input("Due Date (DD-MM-YYYY): ").strip()

        if due:
            break

        error("Due date cannot be empty.")

    created = datetime.now().strftime("%d-%m-%Y")

    tasks.append({

        "task": task_name,
        "priority": priority,
        "completed": False,
        "created": created,
        "due": due

    })

    success("\n✓ Task Added Successfully.")


# ===========================================
# COMPLETE TASK
# ===========================================

def complete_task(tasks):

    if not tasks:
        warning("No tasks available.")
        return

    view_tasks(tasks)

    try:

        number = int(input("\nEnter Task Number : "))

        if 1 <= number <= len(tasks):

            tasks[number - 1]["completed"] = True

            success("Task Completed Successfully.")

        else:

            error("Invalid Task Number.")

    except ValueError:

        error("Enter numbers only.")


# ===========================================
# DELETE TASK
# ===========================================

def delete_task(tasks):

    if not tasks:
        warning("No tasks available.")
        return

    view_tasks(tasks)

    try:

        number = int(input("\nEnter Task Number : "))

        if number < 1 or number > len(tasks):

            error("Invalid Task Number.")
            return

        confirm = input(
            "\nAre you sure? (y/n): "
        ).lower()

        if confirm == "y":

            deleted = tasks.pop(number - 1)

            success(
                f"'{deleted['task']}' deleted successfully."
            )

        else:

            warning("Delete Cancelled.")

    except ValueError:

        error("Enter numbers only.")
# ===========================================
# UPDATE TASK
# ===========================================

def update_task(tasks):

    if not tasks:
        warning("No tasks available.")
        return

    view_tasks(tasks)

    try:
        number = int(input("\nEnter Task Number to Update: "))

        if number < 1 or number > len(tasks):
            error("Invalid Task Number.")
            return

        task = tasks[number - 1]

        print("\nPress Enter to keep the current value.\n")

        new_task = input(f"Task ({task['task']}): ").strip()

        if new_task:
            task["task"] = new_task

        while True:

            new_priority = input(
                f"Priority ({task['priority']}) [High/Medium/Low]: "
            ).capitalize().strip()

            if new_priority == "":
                break

            if new_priority in ["High", "Medium", "Low"]:
                task["priority"] = new_priority
                break

            error("Invalid Priority.")

        new_due = input(
            f"Due Date ({task['due']}): "
        ).strip()

        if new_due:
            task["due"] = new_due

        success("\nTask Updated Successfully.")

    except ValueError:
        error("Enter a valid number.")


# ===========================================
# SEARCH TASK
# ===========================================

def search_task(tasks):

    if not tasks:
        warning("No tasks available.")
        return

    keyword = input("\nEnter keyword to search: ").lower().strip()

    found = False

    line()
    title("SEARCH RESULTS")
    line()

    for i, task in enumerate(tasks, start=1):

        if keyword in task["task"].lower():

            found = True

            status = "Completed ✅" if task["completed"] else "Pending ⏳"

            print(f"""
Task ID      : {i}
Task         : {task['task']}
Priority     : {task['priority']}
Status       : {status}
Created Date : {task['created']}
Due Date     : {task['due']}
------------------------------------------------------------
""")

    if not found:
        warning("No matching task found.")


# ===========================================
# STATISTICS
# ===========================================

def statistics(tasks):

    total = len(tasks)

    completed = sum(task["completed"] for task in tasks)

    pending = total - completed

    percentage = (completed / total * 100) if total else 0

    high = sum(task["priority"] == "High" for task in tasks)
    medium = sum(task["priority"] == "Medium" for task in tasks)
    low = sum(task["priority"] == "Low" for task in tasks)

    line()
    title("TASK STATISTICS")
    line()

    print(f"""
Total Tasks        : {total}

Completed Tasks    : {completed}

Pending Tasks      : {pending}

Completion Rate    : {percentage:.2f}%

High Priority      : {high}

Medium Priority    : {medium}

Low Priority       : {low}
""")

    input("\nPress Enter to continue...")


# ===========================================
# SORT TASKS BY PRIORITY
# ===========================================

def sort_tasks(tasks):

    priority_order = {
        "High": 1,
        "Medium": 2,
        "Low": 3
    }

    tasks.sort(
        key=lambda task: priority_order.get(task["priority"], 4)
    )

    success("Tasks sorted by priority.")


# ===========================================
# SHOW OVERDUE TASKS
# ===========================================

def overdue_tasks(tasks):

    today = datetime.now().date()

    line()
    title("OVERDUE TASKS")
    line()

    found = False

    for task in tasks:

        if task["completed"]:
            continue

        try:

            due = datetime.strptime(
                task["due"],
                "%d-%m-%Y"
            ).date()

            if due < today:

                found = True

                print(f"""
Task : {task['task']}
Due  : {task['due']}
Priority : {task['priority']}
----------------------------------------
""")

        except ValueError:
            continue

    if not found:
        success("No overdue tasks found.")
    
# ===========================================
# EXPORT TASKS TO CSV
# ===========================================

import csv


def export_to_csv(tasks):

    if not tasks:
        warning("No tasks available to export.")
        return

    filename = "tasks.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        # Header
        writer.writerow([
            "Task",
            "Priority",
            "Status",
            "Created Date",
            "Due Date"
        ])

        # Data
        for task in tasks:

            status = "Completed" if task["completed"] else "Pending"

            writer.writerow([
                task["task"],
                task["priority"],
                status,
                task["created"],
                task["due"]
            ])

    success(f"\nTasks exported successfully to '{filename}'.")