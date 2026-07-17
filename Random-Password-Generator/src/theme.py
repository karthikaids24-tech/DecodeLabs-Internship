"""
theme.py
---------------------------------------
Theme Manager

Author : Jai Krithik
"""

import customtkinter as ctk

from settings import Settings


class ThemeManager:

    def __init__(self):

        self.settings = Settings()

        self.theme = self.settings.load().get(
            "theme",
            "Dark"
        )

        self.color_theme = "blue"

    def apply_theme(self):

        theme = self.theme.lower()

        if theme not in [
            "dark",
            "light",
            "system"
        ]:

            theme = "dark"

        ctk.set_appearance_mode(theme)

        ctk.set_default_color_theme(
            self.color_theme
        )

    def set_theme(
            self,
            theme
    ):

        self.theme = theme

        data = self.settings.load()

        data["theme"] = theme

        self.settings.save(data)

        self.apply_theme()

    def get_theme(self):

        return self.theme

    def toggle_theme(self):

        if self.theme.lower() == "dark":

            self.set_theme("Light")

        else:

            self.set_theme("Dark")

    def set_color_theme(
            self,
            color
    ):

        self.color_theme = color

        ctk.set_default_color_theme(
            color
        )

    def get_color_theme(self):

        return self.color_theme

    def reload(self):

        self.theme = self.settings.load().get(
            "theme",
            "Dark"
        )

        self.apply_theme()


theme = ThemeManager()