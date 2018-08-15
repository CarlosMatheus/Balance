"""
You must put all includes from others libraries before the include of pygin
and put all include of other files after the include of pygin
"""
# Other Libraries includes:

# pygin includes:
from pygin import *
# files includes:


class ParticleFadeAnimation(Animation):

    def __init__(self, game_obj, duration):
        key_frame_list = list()
        key_frame_list.append(KeyFrame(0.0, alpha=255, interpolation="in_cubic"))
        key_frame_list.append(KeyFrame(duration, alpha=0))
        super().__init__(game_obj, key_frame_list, should_loop=False, unscaled=True)
