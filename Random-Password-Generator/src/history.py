"""
history.py
----------------------------
Password History Manager
"""

from pathlib import Path
from datetime import datetime
import json

from constants import HISTORY_FILE, MAX_HISTORY


class HistoryManager:

    def __init__(self):

        Path("data").mkdir(exist_ok=True)

        self.file = Path(HISTORY_FILE)

        if not self.file.exists():

            with open(self.file, "w") as f:
                json.dump([], f)

    def load(self):

        with open(self.file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self, data):

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def add(self,
            password,
            strength,
            entropy,
            crack_time):

        history = self.load()

        history.insert(
            0,
            {
                "password": password,
                "strength": strength,
                "entropy": entropy,
                "crack_time": crack_time,
                "created": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            }
        )

        history = history[:MAX_HISTORY]

        self.save(history)

    def delete(self, index):

        history = self.load()

        if 0 <= index < len(history):

            history.pop(index)

            self.save(history)

    def clear(self):

        self.save([])

    def search(self, keyword):

        keyword = keyword.lower()

        return [

            item

            for item in self.load()

            if keyword in item["password"].lower()

        ]

    def statistics(self):

        history = self.load()

        if not history:

            return {
                "count": 0,
                "average_entropy": 0
            }

        entropy = sum(
            item["entropy"]
            for item in history
        )

        return {
            "count": len(history),
            "average_entropy":
            round(entropy / len(history), 2)
        }