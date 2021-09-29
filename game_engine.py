from itertools import combinations
from player import Player
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Game:
    players = list()
    winners = dict()
    bonus = 2
    p1, p2 = 0, 0
    w1, w2 = 0, 0
    power = 100

    def __init__(self, players: list):
        self.players = players
        self.winners = dict()

    def play(self):
        tier = 1
        while len(self.players) > 1:
            list_players = ''
            for p in self.players:
                list_players += f'{p.name}, '
            logging.info('!' * 10 + f" tier {tier}: {list_players[:-2]}")
            self.play_tier()
            self.players = self.tier_results()
            self.winners = dict()
            tier += 1
        if len(self.players) == 0:
            return 'no one win'
        else:
            return self.players[0].name

    def play_tier(self):
        pair = 1
        for player1_class, player2_class in combinations(self.players, 2):
            player1 = player1_class()
            player2 = player2_class()
            logging.info("=" * 5 + f' pair {pair:2}: {player1.name} vs {player2.name} ' + "=" * 5)
            rounds = 1
            while player1.power > 0 and player2.power > 0 and rounds < 20:
                results = self.play_round(player1, player2)
                logging.debug(f'round {rounds:2}: {results}')
                rounds += 1
            self.control_reset()
            self.count_bonus(player1, player2)
            logging.info(f'score: {player1.name}: {player1.win_counter}, {player2.name}: {player2.win_counter}')
            self.find_combination_winner(player1, player2)
            pair += 1

    def tier_results(self):
        if len(self.winners) < len(self.players):
            results = list()
            for winner in self.winners:
                results.append(winner)
                logging.info(f'{winner.name} goes to next level')
            return results
        else:
            min_wins = 1000
            the_most_weak = None
            for winner in self.winners:
                if self.winners[winner] < min_wins:
                    min_wins = self.winners[winner]
                    the_most_weak = winner
            logging.info(f'{the_most_weak.name} is the most weak player and won\'t go to next level')
            del self.winners[the_most_weak]
            return list(self.winners.keys())

    def count_bonus(self, player1: Player, player2: Player):
        if player1.power == 0 and player2.power > 0:
            player2.win_counter += self.bonus
            logging.debug(f'{player2.name} gets bonus')
        elif player2.power == 0 and player1.power > 0:
            player1.win_counter += self.bonus
            logging.debug(f'{player1.name} gets bonus')

    def play_round(self, player1: Player, player2: Player):
        p1 = player1.play()
        p2 = player2.play()
        self.round_control(player1, p1, player2, p2)
        stats = f"{player1.name}: {p1}/{player1.power} - {player2.name}: {p2}/{player2.power}"
        if p1 == p2:
            player1.result(False)
            player2.result(False)
            return f'draw. {stats}'
        elif p1 > p2:
            player1.result(True)
            player2.result(False)
            return f'{player1.name} wins!. {stats}'
        else:
            player1.result(False)
            player2.result(True)
            return f'{player2.name} wins!. {stats}'

    def round_control(self, player1: Player, p1: int, player2: Player, p2: int):
        self.p1 += p1
        self.p2 += p2
        if self.p1 + player1.power != self.power:
            raise CheaterException(player1.__class__)
        if self.p2 + player2.power != self.power:
            raise CheaterException(player1.__class__)

    def control_reset(self):
        self.p1 = 0
        self.p2 = 0

    def find_combination_winner(self, player1: Player, player2: Player):
        winner = None
        if player1.win_counter > player2.win_counter:
            winner = player1
        elif player1.win_counter < player2.win_counter:
            winner = player2
        else:
            return  # no winner
        if self.winners.get(winner.__class__) is None:
            self.winners[winner.__class__] = winner.win_counter
        else:
            self.winners[winner.__class__] += winner.win_counter


class CheaterException(Exception):
    def __init__(self, player_class):
        self.player_class = player_class
