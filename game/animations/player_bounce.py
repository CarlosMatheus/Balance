"""
You must put all includes from others libraries before the include of pygin
and put all include of other files after the include of pygin
"""
# Other Libraries includes:
from pygame.math import Vector2
# pygin includes:
from pygin import *
# files includes:


class PlayerBounce(Animation):

    def __init__(self, game_object):
        """
        :param game_object:
        """
        inter = "in_out_quint"
        gap = 0.5
        key_frames = list()
        key_frames.append(KeyFrame(0.0, position=Vector2(0, 0), interpolation=inter))
        key_frames.append(KeyFrame(0.25, position=Vector2(self.rand()*gap, self.rand()*gap), interpolation=inter))
        key_frames.append(KeyFrame(0.5, position=Vector2(0, 0), interpolation=inter))
        super().__init__(game_object, key_frames)

    def rand(self):
        return 3
