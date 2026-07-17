from generator import PasswordGenerator
from strength import PasswordStrength
from history import HistoryManager
from exporter import ExportManager

password = PasswordGenerator().generate()

report = PasswordStrength(password).report()

history = HistoryManager()

history.add(
    password,
    report["strength"],
    report["entropy"],
    report["crack_time"]
)

print(history.statistics())

export = ExportManager()

records = history.load()

export.csv(records)
export.json(records)
export.txt(records)

print("History exported successfully.")