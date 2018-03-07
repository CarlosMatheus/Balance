from pygame.math import Vector2
from game_engine.time import Time
from game_engine.engine import Engine
from game_engine.normal_behavior import NormalBehavior
from game_engine.components.material import Material
from game_engine.color import Color
from elements.normal_behaviors.game_objects.circle import Circle
from random import uniform as randfloat

class StarScoreController(NormalBehavior):

    def start(self):
        self.fall_velocity = 250
        self.game_object_list = []
        self.radius = Engine.screen_width*0.03


    def update(self):
        for obstacle in self.game_object_list:
            if obstacle.transform.position.y > Engine.screen_height:
                self.game_object_list.remove(obstacle)
                obstacle.destroy(obstacle)
            else:
                self.fall(obstacle)

    def fall(self, obstacle):
        obstacle.transform.position = Vector2(obstacle.transform.position.x, obstacle.transform.position.y
                                        + self.fall_velocity * Time.delta_time())

    def generate_obstacle(self):
        random_pos = int(randfloat(self.radius, Engine.screen_width-self.radius))

        star = Circle(Vector2(random_pos, - 0.06 * Engine.screen_height), self.radius,
                      Material(Color.yellow))
        self.game_object_list.append(star)
