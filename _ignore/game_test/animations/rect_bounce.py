from pygin import *
from pygame.math import Vector2


class RectBounce(Animation):

    def __init__(self, game_object):
        """
        :param game_object:
        """
        inter = "in_out_quint"
        gap = 5
        key_frames = list()
        key_frames.append(KeyFrame(0.0, scale=Vector2(0, 0), interpolation=inter))
        key_frames.append(KeyFrame(1, scale=Vector2(0, gap), interpolation=inter))
        key_frames.append(KeyFrame(2, scale=Vector2(0, 0), interpolation=inter))
        key_frames.append(KeyFrame(3, scale=Vector2(gap, 0), interpolation=inter))
        key_frames.append(KeyFrame(4, scale=Vector2(0, 0), interpolation=inter))
        super().__init__(game_object, key_frames)
