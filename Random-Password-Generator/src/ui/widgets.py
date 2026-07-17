"""
widgets.py
-------------------------------------
Reusable CustomTkinter Widgets

Author : Jai Krithik
"""

import customtkinter as ctk


# --------------------------------------------------------
# Colors
# --------------------------------------------------------

PRIMARY = "#3B82F6"
SUCCESS = "#22C55E"
WARNING = "#F59E0B"
DANGER = "#EF4444"

CARD_COLOR = "#1E293B"

TEXT_COLOR = "white"

FONT = ("Segoe UI", 14)
TITLE_FONT = ("Segoe UI", 28, "bold")
SUBTITLE_FONT = ("Segoe UI", 18, "bold")


# --------------------------------------------------------
# Title Label
# --------------------------------------------------------

class TitleLabel(ctk.CTkLabel):

    def __init__(self, parent, text):

        super().__init__(

            parent,

            text=text,

            font=TITLE_FONT

        )


# --------------------------------------------------------
# Subtitle
# --------------------------------------------------------

class SubtitleLabel(ctk.CTkLabel):

    def __init__(self, parent, text):

        super().__init__(

            parent,

            text=text,

            font=SUBTITLE_FONT

        )


# --------------------------------------------------------
# Card Widget
# --------------------------------------------------------

class Card(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(

            parent,

            fg_color=CARD_COLOR,

            corner_radius=15,

            border_width=1,

            border_color="#2D3748"

        )

        self.pack_propagate(False)


# --------------------------------------------------------
# Primary Button
# --------------------------------------------------------

class PrimaryButton(ctk.CTkButton):

    def __init__(self, parent, text, command):

        super().__init__(

            parent,

            text=text,

            command=command,

            height=42,

            corner_radius=10,

            fg_color=PRIMARY,

            hover_color="#2563EB",

            font=("Segoe UI", 14, "bold")

        )


# --------------------------------------------------------
# Secondary Button
# --------------------------------------------------------

class SecondaryButton(ctk.CTkButton):

    def __init__(self, parent, text, command):

        super().__init__(

            parent,

            text=text,

            command=command,

            height=38,

            corner_radius=10,

            fg_color="#334155",

            hover_color="#475569"

        )


# --------------------------------------------------------
# Password Display
# --------------------------------------------------------

class PasswordBox(ctk.CTkTextbox):

    def __init__(self, parent):

        super().__init__(

            parent,

            height=60,

            corner_radius=10,

            font=("Consolas", 18, "bold")

        )

        self.configure(state="disabled")

    def set(self, password):

        self.configure(state="normal")

        self.delete("1.0", "end")

        self.insert("end", password)

        self.configure(state="disabled")


# --------------------------------------------------------
# Strength Meter
# --------------------------------------------------------

class StrengthMeter(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.label = ctk.CTkLabel(

            self,

            text="Strength"

        )

        self.label.pack(anchor="w")

        self.progress = ctk.CTkProgressBar(

            self,

            width=260,

            height=14

        )

        self.progress.pack(

            pady=5,

            fill="x"

        )

        self.progress.set(0)

        self.status = ctk.CTkLabel(

            self,

            text="No Password"

        )

        self.status.pack(anchor="w")

    def update_strength(

        self,

        value,

        text,

        color

    ):

        self.progress.set(value)

        self.progress.configure(

            progress_color=color

        )

        self.status.configure(

            text=text

        )


# --------------------------------------------------------
# Information Tile
# --------------------------------------------------------

class InfoTile(Card):

    def __init__(

        self,

        parent,

        title,

        value=""

    ):

        super().__init__(parent)

        self.configure(

            width=180,

            height=80

        )

        self.title = ctk.CTkLabel(

            self,

            text=title,

            font=("Segoe UI", 13)

        )

        self.title.pack(

            pady=(10, 2)

        )

        self.value = ctk.CTkLabel(

            self,

            text=value,

            font=("Segoe UI", 18, "bold")

        )

        self.value.pack()

    def set(self, text):

        self.value.configure(text=text)


# --------------------------------------------------------
# Toggle Switch
# --------------------------------------------------------

class Toggle(ctk.CTkSwitch):

    def __init__(

        self,

        parent,

        text,

        variable

    ):

        super().__init__(

            parent,

            text=text,

            variable=variable

        )


# --------------------------------------------------------
# Section Divider
# --------------------------------------------------------

class Divider(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(

            parent,

            height=2,

            fg_color="#374151"

        )


# --------------------------------------------------------
# Status Bar
# --------------------------------------------------------

class StatusBar(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(

            parent,

            height=28

        )

        self.label = ctk.CTkLabel(

            self,

            text="Ready",

            anchor="w"

        )

        self.label.pack(

            fill="both",

            padx=10

        )

    def set(self, message):

        self.label.configure(text=message)