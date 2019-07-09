from pygin import *
from pygame.math import Vector2
from game.game_objects.mesh_objects.player_circle import PlayerCircle
from game.scripts.constants import Constants
import math

class PlayerController(GameObject):

    # def __init__(self):
    #     # ---------------
    #     # Changed for IA:
    #     # super(GameObject, self).__init__()
    #     # self.angle = 0.0
    #     # ---------------

    def start(self):
        # ---------------
        # Changed for IA:
        self.AI_playing = False
        self.AI_playing_act = 2
        self.in_initial_animation = False
        # ---------------
        self.angle = 0.0
        self.angularSpeed = 5.0
        self.game_object_list = [
            PlayerCircle(Vector2(Constants.circCenter_x + Constants.circRadius, Constants.screen_height+15), 15, Material(Color.blue, alpha=240)),
            PlayerCircle(Vector2(Constants.circCenter_x - Constants.circRadius, Constants.screen_height+15), 15, Material(Color.orange, alpha=240))
        ]
        self.should_play = True
        self.initial_time = Time.now()

    def set_IA_as_player(self, act):
        self.AI_playing = True
        self.AI_playing_act = act

    def update(self):
        # ---------------
        # Changed for IA:
        self.initial_animation()
        if not self.in_initial_animation:
            dist_1_ini = abs(self.game_object_list[0].check_distance_circle_to_rect())
            dist_2_ini = abs(self.game_object_list[1].check_distance_circle_to_rect())
            if not self.AI_playing:
                if Input.is_pressing_left:
                    self.turn_left()
                if Input.is_pressing_right:
                    self.turn_right()
            else:
                if self.AI_playing_act == 0:
                    self.turn_right()
                elif self.AI_playing_act == 1:
                    self.turn_left()
                # else:
                    # print('nothing')
            dist_1_final = abs(self.game_object_list[0].check_distance_circle_to_rect())
            dist_2_final = abs(self.game_object_list[1].check_distance_circle_to_rect())
            r1 = self.reward_based_on_move_away(dist_1_ini, dist_1_final)
            r2 = self.reward_based_on_move_away(dist_2_ini, dist_2_final)
            reward = r1 + r2
            score_controller = GameObject.find_by_type("ScoreController")[0]
            score_controller.score += reward
            print(reward)
        # ---------------

    def reward_based_on_move_away(self, dist_initial, dist_final):
        r = self.f(dist_final)
        if dist_final > dist_initial:
            return -r
        else:
            return r

    def f(self, x):
        if x > 80:
            return 0
        if 70 < x < 80:
            return -0.5
        if 60 < x < 70:
            return -1
        if 50 < x < 60:
            return -2
        if 40 < x < 50:
            return -3
        if 30 < x < 40:
            return -4
        if 20 < x < 30:
            return -5
        if 10 < x < 20:
            return -6
        if 5 < x < 10:
            return -7
        if x < 5:
            return -10
        return 0

    def initial_animation(self):
        if self.in_initial_animation:
            if self.should_play:
                self.should_play = False
                self.game_object_list[0].animator.play()
                self.game_object_list[1].animator.play()
        if Time.now() - self.initial_time > 1.0:
            self.in_initial_animation = False

    def turn_right(self):
        self.angle = (self.angle + self.angularSpeed * Time.delta_time()) % (2 * math.pi)
        self.update_circles()

    def turn_left(self):
        self.angle = (self.angle - self.angularSpeed * Time.delta_time()) % (2 * math.pi)
        self.update_circles()

    def update_circles(self):
        self.game_object_list[0].transform.\
            translate(Vector2(Constants.circCenter_x + Constants.circRadius * math.cos(self.angle),
                              Constants.circCenter_y + Constants.circRadius * math.sin(self.angle)))

        self.game_object_list[1].transform.\
            translate(Vector2(Constants.circCenter_x + Constants.circRadius * math.cos(self.angle + math.pi),
                              Constants.circCenter_y + Constants.circRadius * math.sin(self.angle + math.pi)))
