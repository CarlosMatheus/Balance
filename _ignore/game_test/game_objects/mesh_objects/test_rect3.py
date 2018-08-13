from game.game_objects.mesh_objects.rectangle import Rectangle
from _ignore.game_test.animations.rect_bounce3 import RectBounce3
from pygin import *


class TestRect3(Rectangle):

    def start(self):
        ()
        animation_list = [RectBounce3(self)]
        self.animator = Animator(self, animation_list)
        self.animator.play()

    def update(self):
        ()
        # self.transform.translate(Vector2(self.transform.position.x, self.transform.position.y + 15*Time.delta_time()))
