"""
You must put all includes from others libraries before the include of pygin
and put all include of other files after the include of pygin
"""
# Other Libraries includes:
from pygame.math import Vector2
# pygin includes:
from pygin import *
# files includes:


class TextUpFadeOutAnimation(Animation):

    def __init__(self, game_obj):
        key_frame_list = list()
        key_frame_list.append(
            KeyFrame(0.00, position=game_obj.transform.position, alpha = 255, interpolation="in_out_quint"))
        key_frame_list.append(
            KeyFrame(0.8, position=Vector2(game_obj.transform.position.x, 0.95 * game_obj.transform.position.y), alpha=0))
        super().__init__(game_obj, key_frame_list, should_loop=False)
