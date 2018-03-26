from pygame.math import Vector2
from game.game_objects.mesh_objects.star import Star
from pygame import mixer
from game_engine.time import Time
from game_engine.material import Material
from game_engine.game_object import GameObject
from game_engine.color import Color
from random import uniform as randfloat
from game.scripts.constants import Constants
from game.game_objects.mesh_objects.invencible_circle import InvencibleCircle
from game_engine.basic_objects.basic_circle import BasicCircle


class InvenciblePowerUpController(GameObject):

    def start(self):
        self.fall_velocity = 250
        self.radius = Constants.screen_width * 0.03
        self.game_object_list = []
        self.sound_collect = mixer.Sound('game/assets/soundtrack/powerup_collect.wav')
        self.time_of_last_invencibily = -1000
        self.invecible_time = 3.5
        self.current_color = "normal"
        self.animation_ticks_times = [0.4, 0.5, 0.6, 0.7, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00, 1.10]
        self.current_animation_tick_index = 0

    def awake(self):
        self.player_controller = GameObject.find_by_type("PlayerController")[0]

    def update(self):
        difference_time = Time.now() - self.time_of_last_invencibily
        if difference_time > self.invecible_time:
            for i in range(2):
                self.player_controller.game_object_list[i].is_invencible = False
            self.get_back_to_original_colors()
            self.current_animation_tick_index = 0
        else:
            value = min(difference_time / self.invecible_time, 1)  # Just to convert between 0 and 1
            diff = abs(value - self.animation_ticks_times[self.current_animation_tick_index])
            if(diff < 0.01):
                self.current_animation_tick_index += 1
                self.tick_colors()


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

    def get_power_up(self):
        self.sound_collect.play()
        for i in range(2):
            self.player_controller.game_object_list[i].is_invencible = True
        self.change_colors_to_green()
        self.time_of_last_invencibily = Time.now()

    def generate_obstacle(self):
        random_pos = int(randfloat(self.radius + Constants.circCenter_x - Constants.circRadius,
                                   Constants.screen_width -
                                   (self.radius + Constants.circCenter_x - Constants.circRadius)))

        circle = InvencibleCircle(Vector2(random_pos, -2 * self.radius), self.radius,
                                  Material(Color.green))

        self.game_object_list.append(circle)

    def tick_colors(self):
        if(self.current_color == "normal"):
            self.current_color = "green"
            self.change_colors_to_green()
        else:
            self.current_color = "normal"
            self.get_back_to_original_colors()

    def get_back_to_original_colors(self):
        self.player_controller.game_object_list[0].change_color(Color.orange)
        self.player_controller.game_object_list[1].change_color(Color.blue)

    def change_colors_to_green(self):
        for i in range(2):
            self.player_controller.game_object_list[i].change_color(Color.green)
