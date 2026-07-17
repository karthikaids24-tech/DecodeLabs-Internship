"""
settings_page.py
----------------------------------------
SecurePass Pro Settings Window

Author : Jai Krithik
"""

import customtkinter as ctk
from tkinter import BooleanVar
from tkinter import messagebox

from settings import Settings


class SettingsPage(ctk.CTkToplevel):

    def __init__(self, master=None):

        super().__init__(master)

        self.title("Settings")

        self.geometry("700x650")

        self.minsize(650, 600)

        self.settings = Settings()

        self.data = self.settings.load()

        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            self,
            text="Application Settings",
            font=("Segoe UI", 28, "bold")
        )

        self.title_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=25,
            pady=(20,15)
        )

        self.main_frame = ctk.CTkFrame(self)

        self.main_frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=25,
            pady=10
        )

        self.main_frame.grid_columnconfigure(1, weight=1)

        self.theme_var = ctk.StringVar(
            value=self.data.get(
                "theme",
                "Dark"
            )
        )

        self.length_var = ctk.IntVar(
            value=self.data.get(
                "password_length",
                16
            )
        )

        self.uppercase_var = BooleanVar(
            value=self.data.get(
                "uppercase",
                True
            )
        )

        self.lowercase_var = BooleanVar(
            value=self.data.get(
                "lowercase",
                True
            )
        )

        self.digits_var = BooleanVar(
            value=self.data.get(
                "digits",
                True
            )
        )

        self.symbols_var = BooleanVar(
            value=self.data.get(
                "symbols",
                True
            )
        )

        self.exclude_var = BooleanVar(
            value=self.data.get(
                "exclude_similar",
                False
            )
        )

        self.duplicate_var = BooleanVar(
            value=self.data.get(
                "no_duplicates",
                False
            )
        )

        self.auto_copy_var = BooleanVar(
            value=self.data.get(
                "auto_copy",
                True
            )
        )

        self.timeout_var = ctk.IntVar(
            value=self.data.get(
                "clipboard_timeout",
                20
            )
        )

        # ----------------------------
        # Theme
        # ----------------------------

        ctk.CTkLabel(
            self.main_frame,
            text="Application Theme",
            font=("Segoe UI",15,"bold")
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(20,10)
        )

        self.theme_menu = ctk.CTkOptionMenu(
            self.main_frame,
            values=[
                "Dark",
                "Light",
                "System"
            ],
            variable=self.theme_var
        )

        self.theme_menu.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=20
        )

        # ----------------------------
        # Default Password Length
        # ----------------------------

        ctk.CTkLabel(
            self.main_frame,
            text="Default Password Length",
            font=("Segoe UI",15,"bold")
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=20,
            pady=10
        )

        self.length_slider = ctk.CTkSlider(
            self.main_frame,
            from_=8,
            to=64,
            number_of_steps=56,
            variable=self.length_var,
            command=self.update_length
        )

        self.length_slider.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=20
        )

        self.length_label = ctk.CTkLabel(
            self.main_frame,
            text=str(self.length_var.get()),
            width=40
        )

        self.length_label.grid(
            row=1,
            column=2,
            padx=15
        )

        separator = ctk.CTkFrame(
            self.main_frame,
            height=2
        )

        separator.grid(
            row=2,
            column=0,
            columnspan=3,
            sticky="ew",
            padx=20,
            pady=20
        )

        ctk.CTkLabel(
            self.main_frame,
            text="Default Character Types",
            font=("Segoe UI",16,"bold")
        ).grid(
            row=3,
            column=0,
            columnspan=3,
            sticky="w",
            padx=20,
            pady=(0,15)
        )

        self.upper_switch = ctk.CTkSwitch(
            self.main_frame,
            text="Uppercase Letters",
            variable=self.uppercase_var
        )

        self.upper_switch.grid(
            row=4,
            column=0,
            sticky="w",
            padx=20,
            pady=6
        )

        self.lower_switch = ctk.CTkSwitch(
            self.main_frame,
            text="Lowercase Letters",
            variable=self.lowercase_var
        )

        self.lower_switch.grid(
            row=5,
            column=0,
            sticky="w",
            padx=20,
            pady=6
        )

        self.number_switch = ctk.CTkSwitch(
            self.main_frame,
            text="Numbers",
            variable=self.digits_var
        )

        self.number_switch.grid(
            row=6,
            column=0,
            sticky="w",
            padx=20,
            pady=6
        )

        self.symbol_switch = ctk.CTkSwitch(
            self.main_frame,
            text="Symbols",
            variable=self.symbols_var
        )

        self.symbol_switch.grid(
            row=7,
            column=0,
            sticky="w",
            padx=20,
            pady=6
        )

        self.exclude_switch = ctk.CTkSwitch(
            self.main_frame,
            text="Exclude Similar Characters",
            variable=self.exclude_var
        )

        self.exclude_switch.grid(
            row=4,
            column=1,
            sticky="w",
            padx=20,
            pady=6
        )

        self.duplicate_switch = ctk.CTkSwitch(
            self.main_frame,
            text="No Duplicate Characters",
            variable=self.duplicate_var
        )

        self.duplicate_switch.grid(
            row=5,
            column=1,
            sticky="w",
            padx=20,
            pady=6
        )
        separator2 = ctk.CTkFrame(
            self.main_frame,
            height=2
        )

        separator2.grid(
            row=8,
            column=0,
            columnspan=3,
            sticky="ew",
            padx=20,
            pady=20
        )

        ctk.CTkLabel(
            self.main_frame,
            text="Clipboard Settings",
            font=("Segoe UI",16,"bold")
        ).grid(
            row=9,
            column=0,
            columnspan=3,
            sticky="w",
            padx=20,
            pady=(0,15)
        )

        self.auto_copy_switch = ctk.CTkSwitch(
            self.main_frame,
            text="Automatically copy generated password",
            variable=self.auto_copy_var
        )

        self.auto_copy_switch.grid(
            row=10,
            column=0,
            columnspan=2,
            sticky="w",
            padx=20,
            pady=8
        )

        ctk.CTkLabel(
            self.main_frame,
            text="Clipboard Auto Clear (seconds)",
            font=("Segoe UI",15,"bold")
        ).grid(
            row=11,
            column=0,
            sticky="w",
            padx=20,
            pady=10
        )

        self.timeout_slider = ctk.CTkSlider(
            self.main_frame,
            from_=5,
            to=60,
            number_of_steps=55,
            variable=self.timeout_var,
            command=self.update_timeout
        )

        self.timeout_slider.grid(
            row=11,
            column=1,
            sticky="ew",
            padx=20
        )

        self.timeout_label = ctk.CTkLabel(
            self.main_frame,
            text=str(self.timeout_var.get()),
            width=40
        )

        self.timeout_label.grid(
            row=11,
            column=2,
            padx=15
        )

        separator3 = ctk.CTkFrame(
            self.main_frame,
            height=2
        )

        separator3.grid(
            row=12,
            column=0,
            columnspan=3,
            sticky="ew",
            padx=20,
            pady=20
        )

        self.button_frame = ctk.CTkFrame(
            self
        )

        self.button_frame.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=25,
            pady=(0,20)
        )

        self.button_frame.grid_columnconfigure(
            (0,1,2),
            weight=1
        )

        self.save_button = ctk.CTkButton(
            self.button_frame,
            text="Save Settings",
            height=42,
            command=self.save_settings
        )

        self.save_button.grid(
            row=0,
            column=0,
            padx=10,
            pady=15,
            sticky="ew"
        )

        self.reset_button = ctk.CTkButton(
            self.button_frame,
            text="Reset Defaults",
            height=42,
            fg_color="#F59E0B",
            hover_color="#D97706",
            command=self.reset_defaults
        )

        self.reset_button.grid(
            row=0,
            column=1,
            padx=10,
            pady=15,
            sticky="ew"
        )

        self.close_button = ctk.CTkButton(
            self.button_frame,
            text="Close",
            height=42,
            fg_color="#EF4444",
            hover_color="#DC2626",
            command=self.destroy
        )

        self.close_button.grid(
            row=0,
            column=2,
            padx=10,
            pady=15,
            sticky="ew"
        )

    def update_length(self, value):

        value = int(float(value))

        self.length_var.set(value)

        self.length_label.configure(
            text=str(value)
        )

    def update_timeout(self, value):

        value = int(float(value))

        self.timeout_var.set(value)

        self.timeout_label.configure(
            text=str(value)
        )

    def save_settings(self):

        data = {

            "theme": self.theme_var.get(),

            "password_length": self.length_var.get(),

            "uppercase": self.uppercase_var.get(),

            "lowercase": self.lowercase_var.get(),

            "digits": self.digits_var.get(),

            "symbols": self.symbols_var.get(),

            "exclude_similar": self.exclude_var.get(),

            "no_duplicates": self.duplicate_var.get(),

            "auto_copy": self.auto_copy_var.get(),

            "clipboard_timeout": self.timeout_var.get()

        }

        self.settings.save(data)

        if data["theme"] == "Dark":

            ctk.set_appearance_mode("dark")

        elif data["theme"] == "Light":

            ctk.set_appearance_mode("light")

        else:

            ctk.set_appearance_mode("system")

        messagebox.showinfo(
            "Settings",
            "Settings saved successfully."
        )

    def reset_defaults(self):

        answer = messagebox.askyesno(
            "Reset",
            "Restore default settings?"
        )

        if not answer:

            return

        defaults = Settings.DEFAULT

        self.settings.save(defaults)

        self.destroy()

        SettingsPage(self.master)
    def load_defaults(self):

        defaults = Settings.DEFAULT

        self.theme_var.set(
            defaults["theme"]
        )

        self.length_var.set(
            defaults["password_length"]
        )

        self.uppercase_var.set(
            defaults["uppercase"]
        )

        self.lowercase_var.set(
            defaults["lowercase"]
        )

        self.digits_var.set(
            defaults["digits"]
        )

        self.symbols_var.set(
            defaults["symbols"]
        )

        self.exclude_var.set(
            defaults["exclude_similar"]
        )

        self.duplicate_var.set(
            defaults["no_duplicates"]
        )

        self.auto_copy_var.set(
            defaults["auto_copy"]
        )

        self.timeout_var.set(
            defaults["clipboard_timeout"]
        )

        self.length_slider.set(
            defaults["password_length"]
        )

        self.timeout_slider.set(
            defaults["clipboard_timeout"]
        )

        self.length_label.configure(
            text=str(defaults["password_length"])
        )

        self.timeout_label.configure(
            text=str(defaults["clipboard_timeout"])
        )

    def apply_theme(self):

        theme = self.theme_var.get().lower()

        if theme not in [
            "dark",
            "light",
            "system"
        ]:

            theme = "dark"

        ctk.set_appearance_mode(theme)

    def on_close(self):

        self.destroy()

    def bind_shortcuts(self):

        self.bind(
            "<Control-s>",
            lambda event: self.save_settings()
        )

        self.bind(
            "<Escape>",
            lambda event: self.destroy()
        )

        self.bind(
            "<F5>",
            lambda event: self.load_defaults()
        )

    def initialize(self):

        self.length_slider.set(
            self.length_var.get()
        )

        self.timeout_slider.set(
            self.timeout_var.get()
        )

        self.length_label.configure(
            text=str(self.length_var.get())
        )

        self.timeout_label.configure(
            text=str(self.timeout_var.get())
        )

        self.apply_theme()

        self.bind_shortcuts()

        self.protocol(
            "WM_DELETE_WINDOW",
            self.on_close
        )


if __name__ == "__main__":

    ctk.set_appearance_mode("dark")

    ctk.set_default_color_theme("blue")

    root = ctk.CTk()

    root.withdraw()

    window = SettingsPage(root)

    window.initialize()

    root.mainloop()