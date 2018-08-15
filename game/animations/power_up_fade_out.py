"""
You must put all includes from others libraries before the include of pygin
and put all include of other files after the include of pygin
"""
# Other Libraries includes:

# pygin includes:
from pygin import *
# files includes:



class PowerUpFadeOut(Animation):

    def __init__(self, game_obj):
        key_frame_list = list()
        key_frame_list.append(KeyFrame(0.00, alpha=255, interpolation="in_cubic"))
        key_frame_list.append(KeyFrame(0.30, alpha=0))
        super().__init__(game_obj, key_frame_list, should_loop=False)
