from pygin import *
from pygame.math import Vector2


class RectBounce2(Animation):

    def __init__(self, game_object):
        """
        :param game_object:
        """
        inter = "in_cubic"
        gap = 200
        key_frames = list()
        key_frames.append(KeyFrame(0.0, Vector2(0, 0), interpolation=inter))
        key_frames.append(KeyFrame(2, Vector2(0, -gap), interpolation=inter))
        key_frames.append(KeyFrame(4, Vector2(0, 0), interpolation=inter))
        key_frames.append(KeyFrame(6, Vector2(0, gap), interpolation=inter))
        key_frames.append(KeyFrame(8, Vector2(0, 0), interpolation=inter))
        super().__init__(game_object, key_frames)
