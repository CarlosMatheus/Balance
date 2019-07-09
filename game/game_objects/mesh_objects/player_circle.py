from pygin import *
from pygame.math import Vector2
from game.game_objects.mesh_objects.star import Star
from game.animations.circle_player_initial_animation import CirclePlayerInitialAnimation
from game.game_objects.mesh_objects.particle import Particle
from game.game_objects.mesh_objects.get_power_up_effect import GetPowerUpEffect
from game.game_objects.mesh_objects.die_effect import DieEffect
from pygame import mixer
import math


class PlayerCircle(BasicCircle):

    def __init__(self, position, radius, material):
        super(PlayerCircle, self).__init__(position, radius, material, layer=-2)
        self.circle_collider = CircleCollider(self)
        self.is_invencible = False
        self.is_not_dying = True
        # ------------
        # Changed for IA:
        self.min_dist = 1000
        # ------------

    def start(self):
        self.physics = Physics(self)
        self.star_score_controller = GameObject.find_by_type("StarScoreController")[0]
        self.main_scene_controller = GameObject.find_by_type("MainSceneController")[0]
        self.invencible_power_up_controller = GameObject.find_by_type("InvenciblePowerUpController")[0]
        self.animation = CirclePlayerInitialAnimation(self)
        self.animator = Animator(self, [self.animation])
        self.death_sound = mixer.Sound('game/assets/soundtrack/ball_death_01.ogg')
        self.particle_system = ParticleSystem(self, Particle, quant=5, period=0.07,
                                              vel_min=30, vel_max=200, duration=0.5,
                                              inherit_vel=True, inherit_vel_mult=-0.7)
        self.particle_system.set_circ_gen(self.transform.position, self.circle_mesh.get_radius(), mode="directional",
                                          direct_met=self.direct_met, ini_angle_met=self.ini_angle_met,
                                          fin_angle_met=self.fin_angle_met)
        # Changed for IA:
        # self.particle_system.play()


    def ini_angle_met(self):
        return 0 + Vector2(1, 0).angle_to(self.physics.inst_velocity)

    def fin_angle_met(self):
        return 180 + Vector2(1, 0).angle_to(self.physics.inst_velocity)

    def direct_met(self):
        return Vector2(0, 1)

    def check_distance_circle_to_rect(self):
        rectangles = GameObject.find_by_type("Rectangle")
        min_dist = 1000
        for rect in rectangles:
            points = rect.polygon_mesh.get_points()
            point_a = points[0]
            point_b = points[1]
            point_c = points[2]
            point_d = points[3]
            dists = [
                self.get_min_dist_from_line(point_a, point_b),
                self.get_min_dist_from_line(point_b, point_c),
                self.get_min_dist_from_line(point_c, point_d),
                self.get_min_dist_from_line(point_d, point_a),
            ]

            min_dist_to_rect = 1000
            for dist in dists:
                if abs(dist) < abs(min_dist_to_rect):
                    min_dist_to_rect = dist

            if abs(min_dist_to_rect) < abs(min_dist):
                min_dist = min_dist_to_rect
            self.update_score_based_on_dists(min_dist_to_rect)
        self.min_dist = min_dist

    def get_min_dist_from_line(self, point_a, point_b):
        point_c = point_b - point_a
        min_dist = 1000
        for i in range(11):
            point_d = point_c * (i/10) + point_a
            center_dist = self.transform.position.distance_to(point_d)
            cur_dist = center_dist - self.radius
            if self.transform.position.y > point_d.y:
                cur_dist *= -1
            if abs(cur_dist) < abs(min_dist):
                min_dist = cur_dist
        return min_dist

    def update_score_based_on_dists(self, min_dist):
        # print(min_dist)
        penalty = self.f(abs(min_dist))
        # print(penalty)
        if penalty < 0:
            score_controller = GameObject.find_by_type("ScoreController")[0]
            score_controller.score += penalty
            # print(penalty)
            # print("MIN_dist: " + str(min_dist))

    def f(self, x):
        if x > 0:
            return 2 * math.log(x / 150)
        else:
            return -25


    def update(self):
        self.check_collision()
        self.check_distance_circle_to_rect()

    def check_collision(self):
        (collided, game_obj) = self.circle_collider.on_collision()
        if collided:
            if issubclass(type(game_obj), BasicRectangle) and not self.is_invencible and game_obj.collidable:
                self.main_scene_controller.game_over()
                self.die()
            elif issubclass(type(game_obj), Star):
                GetPowerUpEffect(position=game_obj.transform.position, material=game_obj.material)
                game_obj.die()
                self.star_score_controller.get_star()
            elif issubclass(type(game_obj), BasicCircle):
                GetPowerUpEffect(position=game_obj.transform.position, material=game_obj.material)
                game_obj.die()
                self.invencible_power_up_controller.get_power_up()

    def die(self):
        # -----------------
        # Changed for IA:
        score_controller = GameObject.find_by_type("ScoreController")[0]
        die_penalty = 500

        score_controller.score -= die_penalty * Time.delta_time()

        # if self.is_not_dying:
        #     self.death_sound.play()
        #     self.is_not_dying = False
        #     self.particle_system.stop()
        #     inst_vel = self.physics.inst_velocity
        #     r = self.circle_mesh.get_radius()
        #     for i in range(7):
        #         DieEffect(self.transform.position, self.material, 1 + r*i/6, inst_vel=inst_vel)
        #     self.material.alpha = 0
        # -----------------
