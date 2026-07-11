import os
from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)


def clear_screen():
    """Clear terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def title(text):
    print(Fore.CYAN + Style.BRIGHT + text)


def success(text):
    print(Fore.GREEN + text)


def error(text):
    print(Fore.RED + text)


def warning(text):
    print(Fore.YELLOW + text)


def info(text):
    print(Fore.BLUE + text)


def line():
    print(Fore.MAGENTA + "=" * 60)