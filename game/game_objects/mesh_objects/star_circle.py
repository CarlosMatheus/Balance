"""
You must put all includes from others libraries before the include of pygin
and put all include of other files after the include of pygin
"""
# Other Libraries includes:

# pygin includes:
from pygin import *
# files includes:


class StarCircle(BasicCircle):

    def __init__(self, position, radius, material):
        super(StarCircle, self).__init__(position, radius, material, layer = -1)
        self.circle_collider = CircleCollider(self)

    def start(self):
        pass

    def update(self):
        pass
