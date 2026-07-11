from task_manager import (
    add_task,
    view_tasks,
    update_task,
    complete_task,
    delete_task,
    search_task,
    statistics,
    sort_tasks,
    overdue_tasks,
    export_to_csv
)

from storage import load_tasks, save_tasks

from utils import (
    title,
    success,
    error,
    clear_screen,
    line
)


def banner():
    clear_screen()

    line()
    title("        TO-DO LIST APPLICATION")
    title("        DecodeLabs Python Project")
    line()


def menu():

    print("""
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
""")


def main():

    tasks = load_tasks()

    while True:

        banner()

        menu()

        choice = input("Enter your choice (1-11): ").strip()

        if choice == "1":

            add_task(tasks)
            save_tasks(tasks)

        elif choice == "2":

            view_tasks(tasks)

        elif choice == "3":

            update_task(tasks)
            save_tasks(tasks)

        elif choice == "4":

            complete_task(tasks)
            save_tasks(tasks)

        elif choice == "5":

            delete_task(tasks)
            save_tasks(tasks)

        elif choice == "6":

            search_task(tasks)

        elif choice == "7":

            statistics(tasks)

        elif choice == "8":

            sort_tasks(tasks)
            save_tasks(tasks)

        elif choice == "9":

            overdue_tasks(tasks)

        elif choice == "10":

            export_to_csv(tasks)

        elif choice == "11":

            save_tasks(tasks)

            success("\nThank you for using the To-Do List Application.")

            break

        else:

            error("\nInvalid Choice.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()