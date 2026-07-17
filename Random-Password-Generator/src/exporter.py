"""
exporter.py
------------------------
Export Password History
"""

import csv
import json
from pathlib import Path


class ExportManager:

    def __init__(self):

        Path("exports").mkdir(exist_ok=True)

    def csv(self,
            history,
            filename="exports/passwords.csv"):

        if not history:
            return

        with open(
                filename,
                "w",
                newline="",
                encoding="utf-8") as f:

            writer = csv.DictWriter(
                f,
                fieldnames=history[0].keys()
            )

            writer.writeheader()

            writer.writerows(history)

    def json(self,
             history,
             filename="exports/passwords.json"):

        with open(
                filename,
                "w",
                encoding="utf-8") as f:

            json.dump(
                history,
                f,
                indent=4
            )

    def txt(self,
            history,
            filename="exports/passwords.txt"):

        with open(
                filename,
                "w",
                encoding="utf-8") as f:

            for item in history:

                f.write(
                    f"{item['created']} | "
                    f"{item['password']} | "
                    f"{item['strength']}\n"
                )