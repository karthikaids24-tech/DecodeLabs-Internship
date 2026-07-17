"""
utils.py
--------------------
Common utility functions.
"""

from pathlib import Path
from datetime import datetime
import json


def ensure_directory(path: str) -> None:
    """
    Create directory if it does not exist.
    """

    Path(path).mkdir(
        parents=True,
        exist_ok=True
    )


def current_time() -> str:
    """
    Returns formatted timestamp.
    """

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def save_json(data, filename):

    Path(filename).parent.mkdir(
        exist_ok=True
    )

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


def load_json(filename):

    file = Path(filename)

    if not file.exists():
        return {}

    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)