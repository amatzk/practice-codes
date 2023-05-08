import secrets
import string
from dataclasses import dataclass, replace
from enum import Enum, auto


class OptionKey(Enum):
    UPPERCASE = auto()
    LOWERCASE = auto()
    DIGITS = auto()
    SYMBOLS = auto()
    LENGTH = auto()


@dataclass(frozen=True)
class PasswordOptions:
    uppercase: bool
    lowercase: bool
    digits: bool
    symbols: bool
    length: int

    def update(self, key: OptionKey, value: bool | int):
        match key:
            case OptionKey.UPPERCASE if type(value) is bool:
                return replace(self, uppercase=value)
            case OptionKey.LOWERCASE if type(value) is bool:
                return replace(self, lowercase=value)
            case OptionKey.DIGITS if type(value) is bool:
                return replace(self, digits=value)
            case OptionKey.SYMBOLS if type(value) is bool:
                return replace(self, symbols=value)
            case OptionKey.LENGTH if type(value) is int:
                return replace(self, length=value)
            case _:
                raise ValueError(f"Invalid option: {key}, {value}")


class PasswordGenerator:
    def __init__(self, options: PasswordOptions = None):
        if options is None:
            options = PasswordOptions(
                uppercase=True, lowercase=True, digits=True, symbols=True, length=16
            )
        self.options = options

    def update_options(self, options: PasswordOptions):
        self.options = options

    def generate(self):
        characters = ""
        password = []

        character_sets = [
            (self.options.uppercase, string.ascii_uppercase),
            (self.options.lowercase, string.ascii_lowercase),
            (self.options.digits, string.digits),
            (self.options.symbols, string.punctuation),
        ]

        for enabled, character_set in character_sets:
            if enabled:
                characters += character_set
                password.append(secrets.choice(character_set))

        if not characters:
            raise ValueError("少なくとも1つの文字セットを有効にしてください")

        for _ in range(self.options.length - len(password)):
            password.append(secrets.choice(characters))

        secrets.SystemRandom().shuffle(password)

        return "".join(password)


if __name__ == "__main__":
    po = PasswordOptions(
        uppercase=True, lowercase=True, digits=True, symbols=True, length=16
    )
    pg = PasswordGenerator(po)
    pw = pg.generate()

    print(f"\n{pw}\n")

    po2 = PasswordOptions(
        uppercase=False, lowercase=False, digits=True, symbols=True, length=32
    )
    pg2 = PasswordGenerator(po2)
    pw2 = pg2.generate()

    print(f"\n{pw2}\n")

    po3 = po2.update(OptionKey.SYMBOLS, False)
    pg3 = PasswordGenerator(po3)
    pw3 = pg3.generate()

    print(f"\n{pw3}\n")

    pg4 = PasswordGenerator()
    pw4 = pg4.generate()

    print(f"\n{pw4}\n")
