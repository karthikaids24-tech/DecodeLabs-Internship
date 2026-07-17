from generator import PasswordGenerator
from strength import PasswordStrength

generator = PasswordGenerator(
    length=18,
    uppercase=True,
    lowercase=True,
    digits=True,
    symbols=True
)

password = generator.generate()

analysis = PasswordStrength(password).report()

print("-" * 60)
print("Generated Password :", analysis["password"])
print("Score              :", analysis["score"])
print("Strength           :", analysis["strength"])
print("Entropy            :", analysis["entropy"], "bits")
print("Character Pool     :", analysis["pool"])
print("Estimated Crack    :", analysis["crack_time"])
print("-" * 60)