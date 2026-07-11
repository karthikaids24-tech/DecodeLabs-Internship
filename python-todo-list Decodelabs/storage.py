import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    """Load tasks from JSON file."""

    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            content = file.read().strip()

            if not content:
                return []

            return json.loads(content)

    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_tasks(tasks):
    import os

    path = os.path.abspath(FILE_NAME)

    print("Saving to:", path)
    print("Tasks:", tasks)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)

    print("File exists:", os.path.exists(path))
    print("File size:", os.path.getsize(path))