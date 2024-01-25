import string
import random

from pydantic import BaseModel


class Configuration(BaseModel):
    length: int
    use_special_characters: bool = False
    use_numbers: bool = False
    use_capital_letters: bool = False


class PasswordGenerator:
    _strategy_map: dict

    def __init__(self, configuration: Configuration):
        self._strategy_map = {
            'length': LengthStrategy(configuration.length),
            'use_special_characters': None,
            'use_numbers': None,
            'use_capital_letters': None,
        }

    def generate(self):
        new_password = ""
        for k, strategy in self._strategy_map.items():
            if strategy:
                new_password = strategy(new_password)
        return new_password


class LengthStrategy:
    def __init__(self, length):
        self.length = length

    def __call__(self, password):
        chars = list(string.ascii_lowercase)
        return random.shuffle(chars)[:self.length]
