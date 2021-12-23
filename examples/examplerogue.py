from player import Player


class ExampleRogue(Player):
    name = 'rogue'

    def play(self) -> int:
        if self.last_game_win is None:
            self.last_value = 10
            return self.reduce(self.last_value)
        if not self.last_game_win:
            self.last_value *= 2
            return self.reduce(self.last_value)
        else:
            self.last_value = 10
            return self.reduce(self.last_value)
