from pygin import *
from _ignore.game_test.animations.circle_bounce import CircleBounce
from _ignore.game_test.animations.litter_bounce import LitterBounce
from _ignore.game_test.game_objects.mesh_objects.particle_circ import ParticleCirc
from game.game_objects.mesh_objects.particle import Particle
from pygame.math import Vector2


class Circle(BasicCircle):

    def start(self):
        self.material.alpha=200
        animation_list = [LitterBounce(self)]
        self.animator = Animator(self, animation_list)
        self.animator.play()
        self.particle_system = ParticleSystem(self, ParticleCirc, quant=5, period=0.05, vel_min=15, vel_max=120, spawn_prob="parab")
        # self.particle_system = ParticleSystem(self, PlayerParticle, quant=1, period=0.15, vel_min=30, vel_max=60, duration=0.8, gravity=98)
        self.particle_system.set_line_gen(self.fin_point_method, self.ini_point_method)
        # self.particle_system.set_circ_gen(self.transform.position, self.circle_mesh.get_radius(), mode="directional",
        #                                   direct_met=self.direct_met, ini_angle_met=self.ini_angle_met,
        #                                   fin_angle_met=self.fin_angle_met)
        # self.particle_system.set_circ_gen(self.transform.position, self.circle_mesh.get_radius(), mode="radial",
        #                                   direct_met=self.direct_met, ini_angle_met=self.ini_angle_met,
        #                                   fin_angle_met=self.fin_angle_met)
        # self.particle_system.play()

    def fin_point_method(self):
        return self.transform.position + Vector2(self.circle_mesh.get_radius()-5, 0)

    def ini_point_method(self):
        return self.transform.position - Vector2(self.circle_mesh.get_radius(), 0)

    def ini_angle_met(self):
        return 150

    def fin_angle_met(self):
        return 390

    def direct_met(self):
        return Vector2(0, -1)

    # def update(self):
    #     ()
    #     # self.transform.translate(Vector2(self.transform.position.x, self.transform.position.y + 15*Time.delta_time()))
