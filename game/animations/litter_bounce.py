"""
You must put all includes from others libraries before the include of pygin
and put all include of other files after the include of pygin
"""
# Other Libraries includes:
import random
from pygame.math import Vector2
# pygin includes:
from pygin import *
# files includes:


class LitterBounce(Animation):

    def __init__(self, game_object):
        """
        :param game_object:
        """
        inter = "in_out_quint"
        gap = 10
        key_frames = list()
        key_frames.append(KeyFrame(0.0, position=Vector2(0, 0), interpolation=inter))
        key_frames.append(KeyFrame(0.5, position=Vector2(self.rand()*gap, self.rand()*gap), interpolation=inter))
        key_frames.append(KeyFrame(1, position=Vector2(self.rand()*gap, self.rand()*gap), interpolation=inter))
        key_frames.append(KeyFrame(1.5, position=Vector2(self.rand()*gap, self.rand()*gap), interpolation=inter))
        key_frames.append(KeyFrame(2, position=Vector2(-self.rand()*gap, self.rand()*gap), interpolation=inter))
        key_frames.append(KeyFrame(2.5, position=Vector2(-self.rand()*gap, self.rand()*gap), interpolation=inter))
        key_frames.append(KeyFrame(3, position=Vector2(0, 0), interpolation=inter))
        super().__init__(game_object, key_frames)

    def rand(self):
        return random.randint(-2, 8)
