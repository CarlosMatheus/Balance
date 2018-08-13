from game.game_objects.mesh_objects.rectangle import Rectangle
from pygame.math import Vector2
from pygin import *


class Player(Rectangle):

    def start(self):
        self.v = 100
        self.physics = Physics(self, gravity=5.0)
        self.physics.angular_acceleration = 1
        self.physics.velocity = Vector2(30,-80)

    def update(self):
        if Input.is_pressing_left:
            self.transform.translate(Vector2(self.transform.position.x - self.v*Time.delta_time(), self.transform.position.y))
        if Input.is_pressing_right:
            self.transform.translate(Vector2(self.transform.position.x + self.v * Time.delta_time(), self.transform.position.y ))
