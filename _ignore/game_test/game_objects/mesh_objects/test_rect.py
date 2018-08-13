from game.game_objects.mesh_objects.rectangle import Rectangle
from pygin import *
from _ignore.game_test.animations.rect_bounce import RectBounce
from pygame.math import Vector2


class TestRect(Rectangle):

    def start(self):
        # animation_list = [RectBounce(self)]
        # self.animator = Animator(self, animation_list)
        # self.animator.play()
        self.physics = Physics(self, gravity=10.0, velocity=Vector2(75, -75), angular_velocity=3, angular_acceleration=1)

    def update(self):
        ()
        # self.transform.translate(Vector2(self.transform.position.x, self.transform.position.y + 15*Time.delta_time()))
