from pygin import *
from game.scripts.game_settings import GameSettings

# ---------------
# Changed for IA:


def play():
    print("Initializing new game")
    Engine.start_game(GameSettings)
    print("Game finished")


if __name__ == '__main__':
    Engine.start_game(GameSettings)
# ---------------
