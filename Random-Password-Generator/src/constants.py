"""
constants.py
--------------------
Global constants used throughout the application.
"""

APP_NAME = "SecurePass Pro"

VERSION = "1.0.0"

AUTHOR = "Jai Krithik"

# Password Limits
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 128
DEFAULT_PASSWORD_LENGTH = 16

# History
MAX_HISTORY = 500

# Character Sets
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

LOWERCASE = "abcdefghijklmnopqrstuvwxyz"

DIGITS = "0123456789"

SYMBOLS = "!@#$%^&*()_-+=[]{}|;:,.<>?/"

# Similar Characters
SIMILAR = "O0oIl1"

# Data Paths
SETTINGS_FILE = "data/settings.json"

HISTORY_FILE = "data/history.json"

LOG_FILE = "data/app.log"

EXPORT_FOLDER = "exports"

# Theme
DEFAULT_THEME = "dark"

AUTO_CLEAR_CLIPBOARD = 20