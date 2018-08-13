from game.game_objects.mesh_objects.rectangle import Rectangle
from _ignore.game_test.animations.rect_bounce import RectBounce
from pygin import *


class TestRect2(Rectangle):

    def start(self):
        animation_list = [RectBounce(self)]
        self.animator = Animator(self, animation_list)
        self.animator.play()

    def update(self):
        # print(self.polygon_mesh.geometric_center)
        # print(self.polygon_mesh.get_unscaled_points())
        # print(self.polygon_mesh.get_points())
        ()
        # self.transform.translate(Vector2(self.transform.position.x, self.transform.position.y + 15*Time.delta_time()))
