from abc import ABC, abstractmethod


class Player(ABC):
    name = "default"
    power = 100
    win_counter = 0
    loose_counter = 0
    last_game_win = None

    @abstractmethod
    def play(self) -> int:
        '''
        this method should reduce power by 0 <= value <= 100 and return it
        :return: integer value between 0 and 100
        '''
        ...

    def result(self, win: bool):
        self.last_game_win = win
        if win:
            self.win_counter += 1
        else:
            self.loose_counter += 1

    def reduce(self, value: int):
        if type(value) != int or value < 0:
            return 0
        if self.power >= value:
            self.power -= value
        else:
            value = self.power
            self.power = 0
        return value

    def __repr__(self):
        return f"player - {self.name}. class - {self.__class__.__name__}"
