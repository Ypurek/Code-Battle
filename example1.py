from player import Player


class Example1(Player):
    name = 'warrior'

    def play(self) -> int:
        value = 10
        return self.reduce(value)
