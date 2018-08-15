"""
You must put all includes from others libraries before the include of pygin
and put all include of other files after the include of pygin
"""
# Other Libraries includes:

# pygin includes:
from pygin import *
# files includes:
from game.game_objects.controllers.retry_controller import RetryController


class RetryScene(Scene):

    def __init__(self):
        """
        Create the list of mesh_objects and call the superclass constructor passing the list
        """
        self.init_game_objects_controllers_reference_list = [RetryController]
        super(RetryScene, self).__init__(self.init_game_objects_controllers_reference_list)
