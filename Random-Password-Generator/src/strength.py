"""
strength.py
-----------------------------------
Password quality analyzer.
"""

import re

from entropy import PasswordEntropy


class PasswordStrength:

    def __init__(self, password: str):

        self.password = password

    def score(self):

        score = 0

        if len(self.password) >= 8:
            score += 15

        if len(self.password) >= 12:
            score += 10

        if len(self.password) >= 16:
            score += 15

        if re.search(r"[A-Z]", self.password):
            score += 15

        if re.search(r"[a-z]", self.password):
            score += 15

        if re.search(r"\d", self.password):
            score += 15

        if re.search(r"[!@#$%^&*()_\-+=\[\]{}|;:,.<>?/]", self.password):
            score += 15

        entropy = PasswordEntropy(self.password).entropy()

        if entropy >= 60:
            score += 10

        return min(score, 100)

    def level(self):

        score = self.score()

        if score < 30:
            return "Very Weak"

        elif score < 50:
            return "Weak"

        elif score < 70:
            return "Medium"

        elif score < 90:
            return "Strong"

        return "Very Strong"

    def color(self):

        mapping = {
            "Very Weak": "#D32F2F",
            "Weak": "#F57C00",
            "Medium": "#FBC02D",
            "Strong": "#388E3C",
            "Very Strong": "#2E7D32"
        }

        return mapping[self.level()]

    def progress(self):

        return self.score() / 100

    def report(self):

        entropy = PasswordEntropy(self.password)

        return {
            "password": self.password,
            "score": self.score(),
            "strength": self.level(),
            "color": self.color(),
            "progress": self.progress(),
            "entropy": entropy.report()["entropy"],
            "pool": entropy.report()["pool"],
            "crack_time": entropy.report()["crack_time"]
        }