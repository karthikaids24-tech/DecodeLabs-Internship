import unittest
from task_manager import sort_tasks


class TestTaskManager(unittest.TestCase):

    def test_sort_tasks(self):

        tasks = [
            {
                "task": "Task 1",
                "priority": "Low",
                "completed": False,
                "created": "01-01-2026",
                "due": "05-01-2026"
            },
            {
                "task": "Task 2",
                "priority": "High",
                "completed": False,
                "created": "01-01-2026",
                "due": "03-01-2026"
            },
            {
                "task": "Task 3",
                "priority": "Medium",
                "completed": False,
                "created": "01-01-2026",
                "due": "04-01-2026"
            }
        ]

        sort_tasks(tasks)

        self.assertEqual(tasks[0]["priority"], "High")
        self.assertEqual(tasks[1]["priority"], "Medium")
        self.assertEqual(tasks[2]["priority"], "Low")


if __name__ == "__main__":
    unittest.main()