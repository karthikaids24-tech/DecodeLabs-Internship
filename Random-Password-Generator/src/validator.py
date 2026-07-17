"""
validator.py
----------------------
Validation functions.
"""

from constants import (
    MIN_PASSWORD_LENGTH,
    MAX_PASSWORD_LENGTH
)


class PasswordValidator:

    @staticmethod
    def validate_length(length: int):

        if not isinstance(length, int):
            raise TypeError(
                "Length must be integer."
            )

        if length < MIN_PASSWORD_LENGTH:

            raise ValueError(
                f"Minimum length is {MIN_PASSWORD_LENGTH}"
            )

        if length > MAX_PASSWORD_LENGTH:

            raise ValueError(
                f"Maximum length is {MAX_PASSWORD_LENGTH}"
            )

    @staticmethod
    def validate_options(
            upper,
            lower,
            digits,
            symbols
    ):

        if not any([
            upper,
            lower,
            digits,
            symbols
        ]):

            raise ValueError(
                "Select at least one character type."
            )