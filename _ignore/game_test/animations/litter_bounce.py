from pygin import *
from pygame.math import Vector2


class LitterBounce(Animation):

    def __init__(self, game_object):
        """
        :param game_object:
        """
        inter = "in_out_quint"
        gap = 5
        key_frames = list()
        key_frames.append(KeyFrame(0.0, position=Vector2(0, 0), interpolation=inter))
        key_frames.append(KeyFrame(1, position=Vector2(0, gap), interpolation=inter))
        key_frames.append(KeyFrame(2, position=Vector2(-gap, 2*gap), interpolation=inter))
        key_frames.append(KeyFrame(3, position=Vector2(gap, gap), interpolation=inter))
        key_frames.append(KeyFrame(4, position=Vector2(0, 0), interpolation=inter))
        super().__init__(game_object, key_frames)
