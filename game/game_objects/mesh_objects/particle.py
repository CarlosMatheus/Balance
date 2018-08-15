"""
You must put all includes from others libraries before the include of pygin
and put all include of other files after the include of pygin
"""
# Other Libraries includes:

# pygin includes:
from pygin import *
# files includes:
from game.animations.particle_fade_animation import ParticleFadeAnimation


class Particle(BasicParticleCirc):

    def __init__(self, position):
        self.change = True
        super().__init__(position)

    def start(self):
        self.animation = ParticleFadeAnimation(self, self.creator_obj.particle_system.duration)
        self.animator = Animator(self, [self.animation])
        self.animator.play()

    def update(self):
        if self.change:
            self.change = False
            self.material = Material(self.creator_obj.material.color)
        if Time.now() - self.creation_time > self.destroy_time:
            self.destroy_me()
