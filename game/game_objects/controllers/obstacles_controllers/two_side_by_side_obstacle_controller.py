"""
You must put all includes from others libraries before the include of pygin
and put all include of other files after the include of pygin
"""
# Other Libraries includes:
from pygame.math import Vector2
from random import randint as rand
# pygin includes:
from pygin import *
# files includes:
from game.game_objects.mesh_objects.obstacle_rectangle import Rectangle
from game.scripts.constants import Constants
from game.animations.obstacle_pulsing_animation import ObstaclePulsingAnimation


class TwoSideBySideSimpleObstacleController(GameObject):

    def start(self):
        self.fall_velocity = 300
        self.game_object_list = []

    def update(self):

        if len(self.game_object_list) > 0:

            for obstacle_pair in self.game_object_list:
                if obstacle_pair[0].transform.position.y > Constants.screen_height:
                    self.game_object_list.remove(obstacle_pair)
                    for obstacle in obstacle_pair:
                        obstacle.destroy(obstacle)
                        GameObject.destroy(obstacle)
                else:
                    self.fall(obstacle_pair)

    def fall(self, obstacle_pair):
        visible_condition = 0.1 * Constants.screen_height < obstacle_pair[1].transform.position.y < 0.45 * Constants.screen_height

        if visible_condition:
            obstacle_pair[1].transform.position = Vector2(obstacle_pair[1].transform.position.x, obstacle_pair[1].transform.position.y
                                                  + 5.0 * self.fall_velocity * Time.delta_time())

        else:
            obstacle_pair[1].transform.position = Vector2(obstacle_pair[1].transform.position.x, obstacle_pair[1].transform.position.y
                                        + self.fall_velocity * Time.delta_time())


        obstacle_pair[0].transform.position = Vector2(obstacle_pair[0].transform.position.x,
                                              obstacle_pair[0].transform.position.y
                                              + self.fall_velocity * Time.delta_time())

    def generate_obstacle(self):
        direction = rand(0, 1) < 0.5
        obstacle_width = 0.45 * Constants.screen_width
        obstacle_height = 0.06 * Constants.screen_height

        rect1 = Rectangle(Vector2(direction * 0.5 * Constants.screen_width + 12, - obstacle_height),
                          Vector2(obstacle_width, obstacle_height),
                          Material((255, 255, 255)))

        rect2_x = rect1.transform.position.x - 12

        if rect2_x == 0:
            rect2_x = 0.5 * Constants.screen_width + 12
        else:
            rect2_x = 0.0 + 12

        rect2 = Rectangle(Vector2(rect2_x, rect1.transform.position.y),
                          Vector2(obstacle_width, obstacle_height),
                          Material((255, 255, 255)))

        rect1.animation = ObstaclePulsingAnimation(rect1)
        rect1.animator = Animator(rect1, [rect1.animation])
        rect1.animator.play()

        rect2.animation = ObstaclePulsingAnimation(rect2)
        rect2.animator = Animator(rect2, [rect2.animation])
        rect2.animator.play()

        self.game_object_list.append([rect1, rect2])
