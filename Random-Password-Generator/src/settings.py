"""
settings.py
----------------------------
Application Settings
"""

import json
from pathlib import Path

from constants import SETTINGS_FILE


class Settings:

    DEFAULT = {

        "theme": "Dark",

        "password_length": 16,

        "uppercase": True,

        "lowercase": True,

        "digits": True,

        "symbols": True,

        "exclude_similar": False,

        "no_duplicates": False,

        "auto_copy": True,

        "clipboard_timeout": 20

    }

    def __init__(self):

        Path("data").mkdir(exist_ok=True)

        self.file = Path(SETTINGS_FILE)

        if not self.file.exists():

            self.save(self.DEFAULT)

    def load(self):

        with open(
                self.file,
                "r",
                encoding="utf-8") as f:

            return json.load(f)

    def save(self, settings):

        with open(
                self.file,
                "w",
                encoding="utf-8") as f:

            json.dump(
                settings,
                f,
                indent=4
            )