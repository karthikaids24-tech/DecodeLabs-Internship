from generator import PasswordGenerator

generator = PasswordGenerator(
    length=20,
    uppercase=True,
    lowercase=True,
    digits=True,
    symbols=True,
    exclude_similar=True,
    no_duplicates=True
)

password = generator.generate()

print(password)