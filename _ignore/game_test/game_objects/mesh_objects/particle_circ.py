from pygin import *


class ParticleCirc(BasicCircle):

    def __init__(self, position):
        self.creator_obj = None
        super().__init__(position=position, radius=1)

    def start(self):
        pass

    def update(self):
        pass

    def set_creator_object(self, obj):
        self.creator_obj = obj
