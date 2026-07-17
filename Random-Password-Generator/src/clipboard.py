"""
clipboard.py
--------------------------
Clipboard Manager
"""

import threading
import time

import pyperclip


class ClipboardManager:

    @staticmethod
    def copy(password):

        pyperclip.copy(password)

    @staticmethod
    def clear():

        pyperclip.copy("")

    @staticmethod
    def auto_clear(seconds=20):

        def task():

            time.sleep(seconds)

            pyperclip.copy("")

        threading.Thread(
            target=task,
            daemon=True
        ).start()