from pygin import *
from _ignore.game_test.game_objects.controllers.test_scene_controller import TestSceneController


class TestScene(Scene):

    def __init__(self):
        """
        Create the list of mesh_objects and call the superclass constructor passing the list
        """
        self.init_game_objects_controllers_reference_list = [TestSceneController]
        super(TestScene, self).__init__(self.init_game_objects_controllers_reference_list)
