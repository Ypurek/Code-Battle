from examples import ExampleWarrior
from examples import ExampleRogue
from examples import ExampleMage
from examples import ExampleMonk
from game_engine import Game

players = [ExampleWarrior, ExampleRogue, ExampleMage, ExampleMonk]

game = Game(players)
winner = game.play()
print(f'\n\nfinal winner == {winner}')
