from pygin import *


class Disappear(Animation):

    def __init__(self, game_object, time):
        """
        :param game_object:
        """
        inter = "in_cubic"
        key_frames = list()
        key_frames.append(KeyFrame(0.0, alpha=255, interpolation=inter))
        key_frames.append(KeyFrame(time, alpha=0, interpolation=inter))
        super().__init__(game_object, key_frames)
