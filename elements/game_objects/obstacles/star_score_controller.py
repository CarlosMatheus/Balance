from pygame.math import Vector2
from game_engine.time import Time
from game_engine.engine import Engine
from game_engine.game_object import GameObject
from elements.game_objects.material import Material
from elements.game_objects.game_objects.star_circle import StarCircle
from game_engine.game_object import GameObject
from game_engine.color import Color
from elements.game_objects.game_objects.player_circle import PlayerCircle
from random import uniform as randfloat
from game_engine.components.constants import Constants

class StarScoreController(GameObject):

    def start(self):
        self.fall_velocity = 250
        self.game_object_list = []
        self.radius = Constants.screen_width*0.03

    def update(self):
        for obstacle in self.game_object_list:
            if obstacle.transform.position.y > Constants.screen_height:
                self.game_object_list.remove(obstacle)
                obstacle.destroy(obstacle)
                GameObject.destroy(obstacle)
            else:
                self.fall(obstacle)

    def fall(self, obstacle):
        obstacle.transform.position = Vector2(obstacle.transform.position.x, obstacle.transform.position.y
                                              + self.fall_velocity * Time.delta_time())

    def generate_obstacle(self):
        random_pos = int(randfloat(self.radius/2+Constants.circCenter_x-Constants.circRadius,
                                   Constants.screen_width-
                                   (self.radius/2+Constants.circCenter_x-Constants.circRadius)))

        star = StarCircle(Vector2(random_pos, - 0.06 * Constants.screen_height),
                          self.radius, Material(Color.yellow))
        self.game_object_list.append(star)
