from example1 import Example1
from example2 import Example2
from example3 import Example3
from example4 import Example4
from game_engine import Game

players = [Example1, Example2, Example3, Example4]

game = Game(players)
winner = game.play()
print(f'\n\nfinal winner == {winner}')
