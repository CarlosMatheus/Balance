"""
You must put all includes from others libraries before the include of pygin
and put all include of other files after the include of pygin
"""
# Other Libraries includes:
from pygame.math import Vector2
from random import uniform as randfloat
from random import randint
# pygin includes:
from pygin import *
# files includes:
from game.game_objects.mesh_objects.obstacle_rectangle import Rectangle
from game.scripts.constants import Constants
from game.animations.obstacle_pulsing_animation import ObstaclePulsingAnimation


class RandomXFinalObstacleController(GameObject):

    def start(self):
        self.fall_velocity = 400
        self.translate_velocity = 00
        self.game_object_list = []
        self.size = 0.017 * Constants.screen_height

    def update(self):

        for obstacle in self.game_object_list:
            if obstacle.transform.position.y > Constants.screen_height:
                self.game_object_list.remove(obstacle)
                obstacle.destroy(obstacle)
                GameObject.destroy(obstacle)
            else:
                self.fall(obstacle)

    def fall(self, obstacle):
        new_x = obstacle.transform.position.x + self.translate_velocity \
                * Time.delta_time() * obstacle.vel

        if new_x > Constants.screen_width - self.size/2 \
                or new_x < -self.size/2:
            obstacle.vel *= -1
        obstacle.transform.position = Vector2(new_x, obstacle.transform.position.y
                                              + self.fall_velocity * Time.delta_time())

    def generate_obstacle(self):
        random_pos = int(randfloat(self.size / 2 + Constants.circCenter_x - Constants.circRadius,
                                   Constants.screen_width -
                                   (self.size / 2 + Constants.circCenter_x - Constants.circRadius)))

        rect = Rectangle(Vector2(random_pos, -self.size),
                         Vector2(self.size, self.size),
                         Material((255, 255, 255)))
        rect.animation = ObstaclePulsingAnimation(rect)
        rect.animator = Animator(rect, [rect.animation])
        rect.animator.play()

        direction = randint(0, 1)
        if direction == 0:
            direction = -1
        rect.vel = direction  # Checks if going left or right. Can be 1 for right or -1 for left
        self.game_object_list.append(rect)
