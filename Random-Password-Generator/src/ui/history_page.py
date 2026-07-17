"""
history_page.py
--------------------------------------------
Professional Password History Window

Author : Jai Krithik
"""

import customtkinter as ctk
from tkinter import messagebox

from history import HistoryManager
from exporter import ExportManager
from clipboard import ClipboardManager


class HistoryPage(ctk.CTkToplevel):

    def __init__(self, master=None):

        super().__init__(master)

        self.title("Password History")

        self.geometry("1050x650")

        self.minsize(900, 550)

        self.history = HistoryManager()

        self.exporter = ExportManager()

        self.records = self.history.load()

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(2, weight=1)

        title = ctk.CTkLabel(
            self,
            text="Password History",
            font=("Segoe UI", 28, "bold")
        )

        title.grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(20,10)
        )

        self.toolbar = ctk.CTkFrame(self)

        self.toolbar.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20,
            pady=(0,15)
        )

        self.toolbar.grid_columnconfigure(1, weight=1)

        self.search_entry = ctk.CTkEntry(
            self.toolbar,
            placeholder_text="Search Password..."
        )

        self.search_entry.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="ew"
        )

        self.search_button = ctk.CTkButton(
            self.toolbar,
            text="Search",
            command=self.search_history
        )

        self.search_button.grid(
            row=0,
            column=1,
            padx=5
        )

        self.refresh_button = ctk.CTkButton(
            self.toolbar,
            text="Refresh",
            command=self.load_history
        )

        self.refresh_button.grid(
            row=0,
            column=2,
            padx=5
        )

        self.export_button = ctk.CTkButton(
            self.toolbar,
            text="Export",
            command=self.export_history
        )

        self.export_button.grid(
            row=0,
            column=3,
            padx=5
        )

        self.clear_button = ctk.CTkButton(
            self.toolbar,
            text="Clear All",
            fg_color="red",
            hover_color="#B91C1C",
            command=self.clear_history
        )

        self.clear_button.grid(
            row=0,
            column=4,
            padx=5
        )

        self.scroll = ctk.CTkScrollableFrame(self)

        self.scroll.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(0,20)
        )

        self.load_history()
    def load_history(self):

        self.records = self.history.load()

        for widget in self.scroll.winfo_children():
            widget.destroy()

        if not self.records:

            empty = ctk.CTkLabel(
                self.scroll,
                text="No Password History Found",
                font=("Segoe UI",18,"bold")
            )

            empty.pack(
                pady=40
            )

            return

        header = ctk.CTkFrame(self.scroll)

        header.pack(
            fill="x",
            padx=5,
            pady=(0,8)
        )

        headers = [
            ("Date",180),
            ("Password",320),
            ("Strength",120),
            ("Entropy",100),
            ("Crack Time",170),
            ("Actions",120)
        ]

        for text,width in headers:

            lbl = ctk.CTkLabel(
                header,
                text=text,
                width=width,
                font=("Segoe UI",14,"bold"),
                anchor="w"
            )

            lbl.pack(
                side="left",
                padx=5,
                pady=8
            )

        for index,item in enumerate(self.records):

            self.create_row(
                index,
                item
            )

    def create_row(
            self,
            index,
            item
    ):

        row = ctk.CTkFrame(
            self.scroll,
            corner_radius=10
        )

        row.pack(
            fill="x",
            padx=5,
            pady=4
        )

        ctk.CTkLabel(
            row,
            text=item["created"],
            width=180,
            anchor="w"
        ).pack(
            side="left",
            padx=5,
            pady=10
        )

        password_box = ctk.CTkEntry(
            row,
            width=320
        )

        password_box.insert(
            0,
            item["password"]
        )

        password_box.configure(
            state="readonly"
        )

        password_box.pack(
            side="left",
            padx=5
        )

        color = "#22C55E"

        if item["strength"] == "Weak":
            color = "#F59E0B"

        elif item["strength"] == "Very Weak":
            color = "#EF4444"

        elif item["strength"] == "Medium":
            color = "#3B82F6"

        strength = ctk.CTkLabel(
            row,
            text=item["strength"],
            width=120,
            fg_color=color,
            corner_radius=8
        )

        strength.pack(
            side="left",
            padx=5
        )

        entropy = ctk.CTkLabel(
            row,
            text=f"{item['entropy']} bits",
            width=100
        )

        entropy.pack(
            side="left",
            padx=5
        )

        crack = ctk.CTkLabel(
            row,
            text=item["crack_time"],
            width=170
        )

        crack.pack(
            side="left",
            padx=5
        )

        copy_btn = ctk.CTkButton(
            row,
            text="Copy",
            width=55,
            command=lambda p=item["password"]:
            self.copy_password(p)
        )

        copy_btn.pack(
            side="left",
            padx=2
        )

        delete_btn = ctk.CTkButton(
            row,
            text="Delete",
            width=60,
            fg_color="red",
            hover_color="#B91C1C",
            command=lambda i=index:
            self.delete_password(i)
        )

        delete_btn.pack(
            side="left",
            padx=2
        )

    def copy_password(
            self,
            password
    ):

        ClipboardManager.copy(password)

        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard."
        )

    def delete_password(
            self,
            index
    ):

        answer = messagebox.askyesno(
            "Delete",
            "Delete this password?"
        )

        if not answer:
            return

        self.history.delete(index)

        self.load_history()
    def search_history(self):

        keyword = self.search_entry.get().strip()

        if keyword == "":

            self.load_history()

            return

        self.records = self.history.search(keyword)

        for widget in self.scroll.winfo_children():
            widget.destroy()

        if not self.records:

            ctk.CTkLabel(
                self.scroll,
                text="No matching passwords found.",
                font=("Segoe UI",16,"bold")
            ).pack(
                pady=40
            )

            return

        for index, item in enumerate(self.records):

            self.create_row(index, item)

    def export_history(self):

        records = self.history.load()

        if not records:

            messagebox.showwarning(
                "Export",
                "No history available."
            )

            return

        try:

            self.exporter.csv(records)

            self.exporter.json(records)

            self.exporter.txt(records)

            messagebox.showinfo(
                "Export Successful",
                "History exported successfully.\n\n"
                "Files saved in exports/ folder."
            )

        except Exception as e:

            messagebox.showerror(
                "Export Error",
                str(e)
            )

    def clear_history(self):

        answer = messagebox.askyesno(
            "Clear History",
            "Delete all saved passwords?"
        )

        if not answer:
            return

        self.history.clear()

        self.load_history()

        messagebox.showinfo(
            "Success",
            "History cleared successfully."
        )

    def get_statistics(self):

        records = self.history.load()

        total = len(records)

        if total == 0:

            return {

                "count":0,

                "average_entropy":0

            }

        entropy = sum(
            item["entropy"]
            for item in records
        )

        average = round(
            entropy / total,
            2
        )

        return {

            "count":total,

            "average_entropy":average

        }

    def create_footer(self):

        stats = self.get_statistics()

        footer = ctk.CTkFrame(self)

        footer.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=20,
            pady=(0,15)
        )

        total_label = ctk.CTkLabel(

            footer,

            text=f"Total Passwords : {stats['count']}",

            font=("Segoe UI",14,"bold")

        )

        total_label.pack(
            side="left",
            padx=15,
            pady=10
        )

        entropy_label = ctk.CTkLabel(

            footer,

            text=f"Average Entropy : {stats['average_entropy']} bits",

            font=("Segoe UI",14)

        )

        entropy_label.pack(
            side="right",
            padx=15
        )

    def refresh(self):

        self.load_history()

        try:

            self.footer.destroy()

        except:

            pass

        self.footer = ctk.CTkFrame(self)

        self.footer.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=20,
            pady=(0,15)
        )

        stats = self.get_statistics()

        ctk.CTkLabel(

            self.footer,

            text=f"Total Passwords : {stats['count']}",

            font=("Segoe UI",14,"bold")

        ).pack(
            side="left",
            padx=15,
            pady=10
        )

        ctk.CTkLabel(

            self.footer,

            text=f"Average Entropy : {stats['average_entropy']} bits",

            font=("Segoe UI",14)

        ).pack(
            side="right",
            padx=15
        )


if __name__ == "__main__":

    app = ctk.CTk()

    app.withdraw()

    HistoryPage(app)

    app.mainloop()