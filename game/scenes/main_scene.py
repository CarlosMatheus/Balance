"""
You must put all includes from others libraries before the include of pygin
and put all include of other files after the include of pygin
"""
# Other Libraries includes:
from pygame.math import Vector2
import math
# pygin includes:
from pygin import *
# files includes:
from game.game_objects.controllers.main_scene_controller import MainSceneController


class MainScene(Scene):

    def __init__(self):
        """
        Create the list of mesh_objects and call the superclass constructor passing the list
        """
        self.init_game_objects_controllers_reference_list = [MainSceneController]
        super(MainScene, self).__init__(self.init_game_objects_controllers_reference_list)
