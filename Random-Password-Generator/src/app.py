"""
app.py
---------------------------------------
SecurePass Pro

Application Controller

Author : Jai Krithik
"""

import traceback
import customtkinter as ctk
from tkinter import messagebox

from theme import theme
from ui.home import Home


class SecurePassApp:

    def __init__(self):

        self.window = None

    def initialize(self):

        try:

            theme.apply_theme()

            self.window = Home()

            self.window.protocol(
                "WM_DELETE_WINDOW",
                self.on_close
            )

            return True

        except Exception as error:

            traceback.print_exc()

            messagebox.showerror(
                "Startup Error",
                str(error)
            )

            return False

    def run(self):

        success = self.initialize()

        if success:

            self.window.mainloop()

    def restart(self):

        if self.window is not None:

            self.window.destroy()

        self.initialize()

        self.window.mainloop()

    def on_close(self):

        answer = messagebox.askyesno(

            "Exit",

            "Do you really want to exit SecurePass Pro?"

        )

        if answer:

            self.window.destroy()

    def get_window(self):

        return self.window

    def is_running(self):

        return self.window is not None


def launch():

    app = SecurePassApp()

    app.run()


if __name__ == "__main__":

    launch()