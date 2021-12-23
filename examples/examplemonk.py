from player import Player
import random


class ExampleMonk(Player):
    name = 'monk'

    def play(self) -> int:
        value = random.randint(10, 15)
        return self.reduce(value)
