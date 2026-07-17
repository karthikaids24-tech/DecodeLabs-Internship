"""
SecurePass Pro

home.py
------------------------------------
Main Application Window

Author : Jai Krithik
"""

import customtkinter as ctk
from tkinter import BooleanVar
from tkinter import messagebox

from generator import PasswordGenerator
from strength import PasswordStrength
from history import HistoryManager
from clipboard import ClipboardManager
from exporter import ExportManager
from settings import Settings
from ui.widgets import *

APP_WIDTH = 1200
APP_HEIGHT = 760


class Home(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("SecurePass Pro")

        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")

        self.minsize(1100, 700)

        ctk.set_appearance_mode("Dark")

        ctk.set_default_color_theme("blue")

        self.settings = Settings()

        self.history = HistoryManager()

        self.exporter = ExportManager()

        self.generated_password = ""

        self.password_length = ctk.IntVar(value=16)

        self.uppercase = BooleanVar(value=True)

        self.lowercase = BooleanVar(value=True)

        self.digits = BooleanVar(value=True)

        self.symbols = BooleanVar(value=True)

        self.exclude_similar = BooleanVar(value=False)

        self.no_duplicates = BooleanVar(value=False)

        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)

        self.sidebar = Card(self)

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns",
            padx=15,
            pady=15
        )

        self.sidebar.configure(width=220)

        self.main_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.main_frame.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(0,15),
            pady=15
        )

        self.main_frame.grid_columnconfigure(
            0,
            weight=1
        )

        self.main_frame.grid_rowconfigure(
            1,
            weight=1
        )

        TitleLabel(
            self.sidebar,
            "SecurePass"
        ).pack(
            pady=(30,10)
        )

        SubtitleLabel(
            self.sidebar,
            "Navigation"
        ).pack(
            pady=(5,20)
        )

        self.generate_button = PrimaryButton(
            self.sidebar,
            "Generate Password",
            self.generate_password
        )

        self.generate_button.pack(
            fill="x",
            padx=20,
            pady=8
        )

        self.history_button = SecondaryButton(
            self.sidebar,
            "History",
            self.open_history
        )

        self.history_button.pack(
            fill="x",
            padx=20,
            pady=8
        )

        self.export_button = SecondaryButton(
            self.sidebar,
            "Export",
            self.export_history
        )

        self.export_button.pack(
            fill="x",
            padx=20,
            pady=8
        )

        self.settings_button = SecondaryButton(
            self.sidebar,
            "Settings",
            self.open_settings
        )

        self.settings_button.pack(
            fill="x",
            padx=20,
            pady=8
        )

        self.exit_button = SecondaryButton(
            self.sidebar,
            "Exit",
            self.destroy
        )

        self.exit_button.pack(
            side="bottom",
            fill="x",
            padx=20,
            pady=25
        )

        TitleLabel(
            self.main_frame,
            "Secure Password Generator"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(10,20)
        )

        self.options_card = Card(self.main_frame)

        self.options_card.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20,
            pady=(0,15)
        )

        self.options_card.grid_columnconfigure(
            1,
            weight=1
        )

        SubtitleLabel(
            self.options_card,
            "Password Configuration"
        ).grid(
            row=0,
            column=0,
            columnspan=3,
            sticky="w",
            padx=20,
            pady=(20,15)
        )

        ctk.CTkLabel(
            self.options_card,
            text="Password Length",
            font=("Segoe UI",14)
        ).grid(
            row=1,
            column=0,
            padx=20,
            pady=10,
            sticky="w"
        )

        self.length_slider = ctk.CTkSlider(
            self.options_card,
            from_=8,
            to=64,
            number_of_steps=56,
            variable=self.password_length,
            command=self.update_slider
        )

        self.length_slider.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=15
        )

        self.length_value = ctk.CTkLabel(
            self.options_card,
            text="16",
            width=40
        )

        self.length_value.grid(
            row=1,
            column=2,
            padx=15
        )

        Divider(self.options_card).grid(
            row=2,
            column=0,
            columnspan=3,
            sticky="ew",
            padx=20,
            pady=15
        )

        self.upper_switch = Toggle(
            self.options_card,
            "Uppercase Letters",
            self.uppercase
        )

        self.upper_switch.grid(
            row=3,
            column=0,
            sticky="w",
            padx=20,
            pady=8
        )

        self.lower_switch = Toggle(
            self.options_card,
            "Lowercase Letters",
            self.lowercase
        )

        self.lower_switch.grid(
            row=4,
            column=0,
            sticky="w",
            padx=20,
            pady=8
        )

        self.number_switch = Toggle(
            self.options_card,
            "Numbers",
            self.digits
        )

        self.number_switch.grid(
            row=5,
            column=0,
            sticky="w",
            padx=20,
            pady=8
        )

        self.symbol_switch = Toggle(
            self.options_card,
            "Symbols",
            self.symbols
        )

        self.symbol_switch.grid(
            row=6,
            column=0,
            sticky="w",
            padx=20,
            pady=8
        )

        self.exclude_switch = Toggle(
            self.options_card,
            "Exclude Similar Characters",
            self.exclude_similar
        )

        self.exclude_switch.grid(
            row=3,
            column=1,
            sticky="w",
            padx=20,
            pady=8
        )

        self.duplicate_switch = Toggle(
            self.options_card,
            "No Duplicate Characters",
            self.no_duplicates
        )

        self.duplicate_switch.grid(
            row=4,
            column=1,
            sticky="w",
            padx=20,
            pady=8
        )
        Divider(self.options_card).grid(
            row=7,
            column=0,
            columnspan=3,
            sticky="ew",
            padx=20,
            pady=15
        )

        self.generate_btn = PrimaryButton(
            self.options_card,
            "Generate Secure Password",
            self.generate_password
        )

        self.generate_btn.grid(
            row=8,
            column=0,
            columnspan=3,
            sticky="ew",
            padx=20,
            pady=(10,20)
        )

        # ==================================================
        # Password Display Card
        # ==================================================

        self.password_card = Card(self.main_frame)

        self.password_card.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=20,
            pady=(0,15)
        )

        self.password_card.grid_columnconfigure(
            0,
            weight=1
        )

        SubtitleLabel(
            self.password_card,
            "Generated Password"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(20,10)
        )

        self.password_box = PasswordBox(
            self.password_card
        )

        self.password_box.grid(
            row=1,
            column=0,
            columnspan=4,
            sticky="ew",
            padx=20,
            pady=(0,20)
        )

        self.copy_btn = SecondaryButton(
            self.password_card,
            "Copy",
            self.copy_password
        )

        self.copy_btn.grid(
            row=2,
            column=0,
            padx=20,
            pady=(0,20),
            sticky="ew"
        )

        self.save_btn = SecondaryButton(
            self.password_card,
            "Save",
            self.save_password
        )

        self.save_btn.grid(
            row=2,
            column=1,
            padx=10,
            pady=(0,20),
            sticky="ew"
        )

        self.history_btn = SecondaryButton(
            self.password_card,
            "History",
            self.open_history
        )

        self.history_btn.grid(
            row=2,
            column=2,
            padx=10,
            pady=(0,20),
            sticky="ew"
        )

        self.export_btn = SecondaryButton(
            self.password_card,
            "Export",
            self.export_history
        )

        self.export_btn.grid(
            row=2,
            column=3,
            padx=20,
            pady=(0,20),
            sticky="ew"
        )

        # ==================================================
        # Statistics Area
        # ==================================================

        self.stats_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent"
        )

        self.stats_frame.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=20,
            pady=(0,15)
        )

        self.stats_frame.grid_columnconfigure(
            (0,1,2),
            weight=1
        )

        self.strength_card = Card(
            self.stats_frame
        )

        self.strength_card.grid(
            row=0,
            column=0,
            padx=(0,10),
            sticky="nsew"
        )

        SubtitleLabel(
            self.strength_card,
            "Password Strength"
        ).pack(
            anchor="w",
            padx=20,
            pady=(20,10)
        )

        self.strength_meter = StrengthMeter(
            self.strength_card
        )

        self.strength_meter.pack(
            fill="x",
            padx=20,
            pady=(0,20)
        )

        self.entropy_card = InfoTile(
            self.stats_frame,
            "Entropy"
        )

        self.entropy_card.grid(
            row=0,
            column=1,
            padx=10,
            sticky="nsew"
        )

        self.crack_card = InfoTile(
            self.stats_frame,
            "Crack Time"
        )

        self.crack_card.grid(
            row=0,
            column=2,
            padx=(10,0),
            sticky="nsew"
        )

        # ==================================================
        # Status Bar
        # ==================================================

        self.status_bar = StatusBar(self)

        self.status_bar.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="ew"
        )

        self.status_bar.set(
            "Ready"
        )

        self.length_slider.set(16)
    def update_slider(self, value):

        value = int(float(value))

        self.password_length.set(value)

        self.length_value.configure(text=str(value))

    def generate_password(self):

        try:

            generator = PasswordGenerator(
                length=self.password_length.get(),
                uppercase=self.uppercase.get(),
                lowercase=self.lowercase.get(),
                digits=self.digits.get(),
                symbols=self.symbols.get(),
                exclude_similar=self.exclude_similar.get(),
                no_duplicates=self.no_duplicates.get()
            )

            self.generated_password = generator.generate()

            self.password_box.set(self.generated_password)

            report = PasswordStrength(
                self.generated_password
            ).report()

            self.strength_meter.update_strength(
                report["progress"],
                report["strength"],
                report["color"]
            )

            self.entropy_card.set(
                f"{report['entropy']} bits"
            )

            self.crack_card.set(
                report["crack_time"]
            )

            self.status_bar.set(
                "Password generated successfully"
            )

            if self.settings.load().get(
                "auto_copy",
                True
            ):

                ClipboardManager.copy(
                    self.generated_password
                )

                timeout = self.settings.load().get(
                    "clipboard_timeout",
                    20
                )

                ClipboardManager.auto_clear(timeout)

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

            self.status_bar.set("Error")

    def copy_password(self):

        if not self.generated_password:

            messagebox.showwarning(
                "Warning",
                "Generate a password first."
            )

            return

        ClipboardManager.copy(self.generated_password)

        timeout = self.settings.load().get(
            "clipboard_timeout",
            20
        )

        ClipboardManager.auto_clear(timeout)

        self.status_bar.set(
            f"Copied to clipboard (clears in {timeout}s)"
        )

    def save_password(self):

        if not self.generated_password:

            messagebox.showwarning(
                "Warning",
                "Generate a password first."
            )

            return

        report = PasswordStrength(
            self.generated_password
        ).report()

        self.history.add(
            self.generated_password,
            report["strength"],
            report["entropy"],
            report["crack_time"]
        )

        self.status_bar.set(
            "Password saved to history"
        )

        messagebox.showinfo(
            "Saved",
            "Password saved to history."
        )

    def export_history(self):

        records = self.history.load()

        if not records:

            messagebox.showwarning(
                "Warning",
                "History is empty."
            )

            return

        self.exporter.csv(records)

        self.exporter.json(records)

        self.exporter.txt(records)

        self.status_bar.set(
            "History exported successfully"
        )

        messagebox.showinfo(
            "Export Complete",
            "Exported to exports/ folder."
        )

    def open_history(self):

        records = self.history.load()

        if not records:

            messagebox.showinfo(
                "History",
                "No saved passwords."
            )

            return

        history_window = ctk.CTkToplevel(self)

        history_window.title("Password History")

        history_window.geometry("850x520")

        history_window.grid_columnconfigure(0, weight=1)

        history_window.grid_rowconfigure(1, weight=1)

        TitleLabel(
            history_window,
            "Password History"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(15,10)
        )

        frame = ctk.CTkScrollableFrame(history_window)

        frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(0,15)
        )

        for item in records:

            row = ctk.CTkFrame(frame)

            row.pack(fill="x", pady=5)

            ctk.CTkLabel(
                row,
                text=item["created"],
                width=150,
                anchor="w"
            ).pack(side="left", padx=10, pady=10)

            ctk.CTkLabel(
                row,
                text=item["password"],
                font=("Consolas", 14, "bold"),
                anchor="w"
            ).pack(side="left", padx=10, pady=10)

            ctk.CTkLabel(
                row,
                text=item["strength"],
                width=100,
                anchor="w"
            ).pack(side="left", padx=10, pady=10)

    def open_settings(self):

        settings_window = ctk.CTkToplevel(self)

        settings_window.title("Settings")

        settings_window.geometry("420x420")

        settings_window.grid_columnconfigure(0, weight=1)

        TitleLabel(
            settings_window,
            "Settings"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(15,10)
        )

        settings = self.settings.load()

        theme_var = ctk.StringVar(
            value=settings.get("theme", "Dark")
        )

        auto_copy_var = BooleanVar(
            value=settings.get("auto_copy", True)
        )

        timeout_var = ctk.IntVar(
            value=settings.get("clipboard_timeout", 20)
        )

        form = ctk.CTkFrame(settings_window)

        form.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20,
            pady=10
        )

        form.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(
            form,
            text="Theme"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=10,
            pady=10
        )

        theme_menu = ctk.CTkOptionMenu(
            form,
            values=["Dark", "Light"],
            variable=theme_var
        )

        theme_menu.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=10,
            pady=10
        )

        auto_copy_switch = ctk.CTkSwitch(
            form,
            text="Auto Copy Password",
            variable=auto_copy_var
        )

        auto_copy_switch.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="w",
            padx=10,
            pady=10
        )

        ctk.CTkLabel(
            form,
            text="Clipboard Timeout (sec)"
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=10,
            pady=10
        )

        timeout_slider = ctk.CTkSlider(
            form,
            from_=5,
            to=60,
            number_of_steps=55,
            variable=timeout_var
        )

        timeout_slider.grid(
            row=2,
            column=1,
            sticky="ew",
            padx=10,
            pady=10
        )

        def save_settings():

            new_settings = settings.copy()

            new_settings["theme"] = theme_var.get()

            new_settings["auto_copy"] = auto_copy_var.get()

            new_settings["clipboard_timeout"] = timeout_var.get()

            self.settings.save(new_settings)

            ctk.set_appearance_mode(theme_var.get())

            self.status_bar.set("Settings saved")

            messagebox.showinfo(
                "Saved",
                "Settings updated successfully."
            )

        save_btn = PrimaryButton(
            settings_window,
            "Save Settings",
            save_settings
        )

        save_btn.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=20,
            pady=(10,20)
        )
    def refresh_statistics(self):

        stats = self.history.statistics()

        self.status_bar.set(
            f"Saved Passwords : {stats['count']} | "
            f"Average Entropy : {stats['average_entropy']} bits"
        )

    def clear_history(self):

        answer = messagebox.askyesno(
            "Confirm",
            "Delete all saved passwords?"
        )

        if not answer:
            return

        self.history.clear()

        self.refresh_statistics()

        self.status_bar.set(
            "History cleared"
        )

        messagebox.showinfo(
            "Success",
            "Password history cleared."
        )

    def load_settings(self):

        settings = self.settings.load()

        self.password_length.set(
            settings.get(
                "password_length",
                16
            )
        )

        self.uppercase.set(
            settings.get(
                "uppercase",
                True
            )
        )

        self.lowercase.set(
            settings.get(
                "lowercase",
                True
            )
        )

        self.digits.set(
            settings.get(
                "digits",
                True
            )
        )

        self.symbols.set(
            settings.get(
                "symbols",
                True
            )
        )

        self.exclude_similar.set(
            settings.get(
                "exclude_similar",
                False
            )
        )

        self.no_duplicates.set(
            settings.get(
                "no_duplicates",
                False
            )
        )

        self.length_slider.set(
            self.password_length.get()
        )

        self.length_value.configure(
            text=str(
                self.password_length.get()
            )
        )

    def reset_options(self):

        self.password_length.set(16)

        self.uppercase.set(True)

        self.lowercase.set(True)

        self.digits.set(True)

        self.symbols.set(True)

        self.exclude_similar.set(False)

        self.no_duplicates.set(False)

        self.length_slider.set(16)

        self.length_value.configure(
            text="16"
        )

        self.password_box.set("")

        self.generated_password = ""

        self.entropy_card.set("--")

        self.crack_card.set("--")

        self.strength_meter.update_strength(
            0,
            "No Password",
            "#6B7280"
        )

        self.status_bar.set(
            "Options reset"
        )

    def about(self):

        messagebox.showinfo(
            "About",
            "SecurePass Pro\n\n"
            "Version : 1.0\n\n"
            "Developed using Python and CustomTkinter\n\n"
            "Author : Jai Krithik"
        )

    def run(self):

        self.load_settings()

        self.refresh_statistics()

        self.mainloop()


if __name__ == "__main__":

    app = Home()

    app.run()