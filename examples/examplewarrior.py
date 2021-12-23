from player import Player


class ExampleWarrior(Player):
    name = 'warrior'

    def play(self) -> int:
        value = 10
        return self.reduce(value)
