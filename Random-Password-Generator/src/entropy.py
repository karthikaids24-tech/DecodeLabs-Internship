"""
entropy.py
----------------------------
Password entropy calculations and crack-time estimation.
"""

import math
import string


class PasswordEntropy:
    """
    Calculates entropy and estimates crack time.
    """

    def __init__(self, password: str):
        self.password = password

    def character_pool(self) -> int:
        """
        Determine the possible character pool size.
        """

        pool = 0

        if any(c in string.ascii_lowercase for c in self.password):
            pool += 26

        if any(c in string.ascii_uppercase for c in self.password):
            pool += 26

        if any(c in string.digits for c in self.password):
            pool += 10

        if any(c in string.punctuation for c in self.password):
            pool += 32

        return max(pool, 1)

    def entropy(self) -> float:
        """
        Entropy in bits.
        """

        charset = self.character_pool()

        return len(self.password) * math.log2(charset)

    def combinations(self) -> int:
        """
        Total possible passwords.
        """

        return int(self.character_pool() ** len(self.password))

    def crack_time(self):
        """
        Approximate brute-force crack time.
        """

        guesses_per_second = 100_000_000_000

        seconds = self.combinations() / guesses_per_second

        units = [
            ("Years", 31536000),
            ("Days", 86400),
            ("Hours", 3600),
            ("Minutes", 60),
            ("Seconds", 1)
        ]

        for unit, value in units:

            if seconds >= value:
                return round(seconds / value, 2), unit

        return round(seconds, 2), "Seconds"

    def report(self):

        value, unit = self.crack_time()

        return {
            "entropy": round(self.entropy(), 2),
            "pool": self.character_pool(),
            "combinations": self.combinations(),
            "crack_time": f"{value} {unit}"
        }