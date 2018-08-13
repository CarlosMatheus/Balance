from _ignore.game_test.scenes.test_scene import TestScene


class ScenesControllerScript:

    @classmethod
    def get_scenes(cls):
        """
        :return: the scene list with the references to the scenes classes
        """
        return [TestScene]
