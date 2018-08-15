"""
You must put all includes from others libraries before the include of pygin
and put all include of other files after the include of pygin
"""
# Other Libraries includes:

# pygin includes:
from pygin import *
# files includes:
from game.scripts.scenes_controller_script import ScenesControllerScript
from game.scripts.constants import Constants


class GameSettings:

    game_name = "Balance"
    screen_width = Constants.screen_width
    screen_height = Constants.screen_height
    scenes_list = ScenesControllerScript.get_scenes()
