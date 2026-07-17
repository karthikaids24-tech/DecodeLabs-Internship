"""
main.py
----------------------------------------
SecurePass Pro

Application Entry Point

Author : Jai Krithik
"""

import sys
import traceback
from tkinter import messagebox

import customtkinter as ctk

from app import launch


APP_NAME = "SecurePass Pro"
VERSION = "1.0.0"


def configure_application():
    """
    Configure CustomTkinter before
    launching the application.
    """

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")


def show_error(error):

    traceback.print_exc()

    messagebox.showerror(
        "Application Error",
        f"An unexpected error occurred.\n\n{error}"
    )


def print_banner():

    print("=" * 60)
    print(f"{APP_NAME}  v{VERSION}")
    print("=" * 60)
    print("Professional Random Password Generator")
    print("=" * 60)


def main():

    print_banner()

    try:

        configure_application()

        launch()

    except KeyboardInterrupt:

        print("\nApplication terminated by user.")

    except Exception as error:

        show_error(error)

        sys.exit(1)


if __name__ == "__main__":

    main()