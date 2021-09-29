from player import Player
import random


class Example3(Player):
    name = 'mage'

    def play(self) -> int:
        value = random.randint(0, 20)
        return self.reduce(value)
