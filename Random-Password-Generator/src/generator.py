"""
generator.py
---------------------
Secure password generator.
"""

import secrets
import string

from validator import PasswordValidator


class PasswordGenerator:

    def __init__(
            self,
            length=16,
            uppercase=True,
            lowercase=True,
            digits=True,
            symbols=True,
            exclude_similar=False,
            no_duplicates=False
    ):

        PasswordValidator.validate_length(
            length
        )

        PasswordValidator.validate_options(
            uppercase,
            lowercase,
            digits,
            symbols
        )

        self.length = length

        self.uppercase = uppercase
        self.lowercase = lowercase
        self.digits = digits
        self.symbols = symbols

        self.exclude_similar = exclude_similar

        self.no_duplicates = no_duplicates

    def build_pool(self):

        pool = ""

        if self.uppercase:
            pool += string.ascii_uppercase

        if self.lowercase:
            pool += string.ascii_lowercase

        if self.digits:
            pool += string.digits

        if self.symbols:
            pool += "!@#$%^&*()-_=+[]{}<>?"

        if self.exclude_similar:

            similar = "O0oIl1"

            pool = "".join(
                c
                for c in pool
                if c not in similar
            )

        return pool

    def generate(self):

        pool = self.build_pool()

        password = []

        if self.uppercase:
            password.append(
                secrets.choice(
                    string.ascii_uppercase
                )
            )

        if self.lowercase:
            password.append(
                secrets.choice(
                    string.ascii_lowercase
                )
            )

        if self.digits:
            password.append(
                secrets.choice(
                    string.digits
                )
            )

        if self.symbols:
            password.append(
                secrets.choice(
                    "!@#$%^&*()-_=+[]{}<>?"
                )
            )

        while len(password) < self.length:

            char = secrets.choice(pool)

            if (
                self.no_duplicates
                and char in password
            ):
                continue

            password.append(char)

        secrets.SystemRandom().shuffle(password)

        return "".join(password)