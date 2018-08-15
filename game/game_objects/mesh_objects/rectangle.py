"""
You must put all includes from others libraries before the include of pygin
and put all include of other files after the include of pygin
"""
# Other Libraries includes:

# pygin includes:
from pygin import *
# files includes:


class Rectangle(BasicRectangle):

    def __init__(self, position, dimension, material, layer=0):
        super(Rectangle, self).__init__(position, dimension, material, layer=layer)
        self.dimension = dimension
        self.polygon_collider = PolygonCollider(self)
