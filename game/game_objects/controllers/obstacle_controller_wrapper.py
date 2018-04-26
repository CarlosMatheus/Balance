from game_engine.time import Time
from random import randint as rand
from pygame.math import Vector2

#Controllers
from game.game_objects.controllers.obstacles_controllers.simple_obstacle_controller import SimpleObstacleController
from game.game_objects.controllers.obstacles_controllers.middle_rect_obstacle_controller import MiddleRectObstacleController
from game.game_objects.controllers.obstacles_controllers.random_x_final_obstacle_controller import RandomXFinalObstacleController
from game.game_objects.controllers.obstacles_controllers.rect_translate_x_obstacle_cotroller import RectTranslateXObstacleController
from game.game_objects.controllers.obstacles_controllers.two_in_one_simple_obstacle_controller import TwoInOneSimpleObstacleController
from game.game_objects.controllers.obstacles_controllers.two_side_by_side_obstacle_controller import TwoSideBySideSimpleObstacleController
from game.game_objects.controllers.obstacles_controllers.spinning_middle_rect_obstacle_controller import SpinningMiddleRectObstacleController
from game.game_objects.controllers.obstacles_controllers.half_moon_spinning_rect_obstacle_controller import HalfMoonSpinningRectObstacleController
from game.game_objects.controllers.obstacles_controllers.invisible_middle_obstacle_controller import InvisibleMiddleObstacleController
from game.game_objects.controllers.obstacles_controllers.invisible_simple_obstacle_controller import InvisibleSimpleObstacleController
from game_engine.game_object import GameObject
from game_engine.basic_objects.text import Text
from game_engine.color import Color
from game.animations.text_up_fade_out_animation import TextUpFadeOutAnimation
from game_engine.components.animator import Animator
from game_engine.material import Material
from game.scripts.constants import Constants



class ObstacleControllerWrapper(GameObject):

    def start(self):
        self.obstacle_generators = [
            SimpleObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0)
        ]
        self.rect_x_controller = RandomXFinalObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0)
        self.obstacle_geneation_delta = 1500
        self.last_generation_time = 1000 * Time.now()
        self.game_object_list = []
        self.last_increases_dificculty_time = Time.now()
        self.game_difficuty = 1
        self.time_to_increase_difficult = 6.2
        self.generation_obstacle_difficult = 1
        self.max_difficult = 10
        self.should_delete_difficulty_text = False
        self.diff_text_gen_time = 0.0
        for obstacle_generator in self.obstacle_generators:
            obstacle_generator.start()

    def update(self):

        if Time.time_scale < 0.5:
            #Adjust timers to new delta
            self.last_generation_time += 1000 * Time.delta_time(True)
            self.last_increases_dificculty_time += Time.delta_time(True)

        self.increase_difficult()
        self.delete_difficulty_text()

        if (1000 * Time.now() - self.last_generation_time) * Time.time_scale > self.obstacle_geneation_delta * \
                self.generation_obstacle_difficult:
            self.generate_random_obstacle()

        for obstacle_generator in self.obstacle_generators:
            game_objs = obstacle_generator.game_object_list
            self.game_object_list.extend(game_objs)

    def increase_difficult(self):
        if Time.now() - self.last_increases_dificculty_time > self.time_to_increase_difficult \
                and self.game_difficuty < self.max_difficult:

            self.game_difficuty += 1
            self.last_increases_dificculty_time = Time.now()
            self.time_to_increase_difficult *= 1.03
            self.generation_obstacle_difficult = (1 - (self.game_difficuty - 1) * 0.2 / self.max_difficult)
            self.generate_difficulty_text()

            if self.game_difficuty == 2:
                obstacle = MiddleRectObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0)
                obstacle.start()
                self.obstacle_generators.append(obstacle)

            if self.game_difficuty == 3:
                obstacle = TwoInOneSimpleObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0)
                obstacle.start()
                self.obstacle_generators.append(obstacle)

            if self.game_difficuty == 4:
                obstacle = TwoSideBySideSimpleObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0)
                obstacle.start()
                self.obstacle_generators.append(obstacle)

            if self.game_difficuty == 5:
                obstacle = HalfMoonSpinningRectObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0)
                obstacle.start()
                self.obstacle_generators.append(obstacle)

            if self.game_difficuty == 6:
                obstacle = InvisibleMiddleObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0)
                obstacle.start()
                self.obstacle_generators.append(obstacle)
                self.delete_object_with_specific_type(MiddleRectObstacleController)

            if self.game_difficuty == 7:
                obstacle = InvisibleSimpleObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0)
                obstacle.start()
                self.obstacle_generators.append(obstacle)

            if self.game_difficuty == 8 and len(self.obstacle_generators) > 3:
                obstacle = RectTranslateXObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0)
                obstacle.start()
                self.obstacle_generators.append(obstacle)
                self.delete_object_with_specific_type(SimpleObstacleController)
                self.delete_object_with_specific_type(TwoInOneSimpleObstacleController)

            if self.game_difficuty == 9:
                obstacle = SpinningMiddleRectObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0)
                obstacle.start()
                self.obstacle_generators.append(obstacle)

            if self.game_difficuty == 10:
                self.delete_object_with_specific_type(TwoSideBySideSimpleObstacleController)
                self.delete_object_with_specific_type(InvisibleSimpleObstacleController)
                self.delete_object_with_specific_type(HalfMoonSpinningRectObstacleController)

    def generate_difficulty_text(self):
        title_x = 0.35 * Constants.screen_width
        title_y = 0.3 * Constants.screen_height
        title_size = 50
        text = "HARDER!"

        if self.game_difficuty == self.max_difficult:
            text = "MAX DIFFICULTY!"
            title_size = 28
            title_x = 0.20 * Constants.screen_width

        font_path = "game/assets/fonts/neuropolxrg.ttf"
        diff_text = Text(Vector2(title_x - title_size, title_y), text, Material(Color.red, alpha=255), title_size,
                         font_path)
        diff_text.transform.position.x -= diff_text.text_mesh.size
        diff_text.animation = TextUpFadeOutAnimation(diff_text)
        diff_text.animator = Animator(diff_text, [diff_text.animation])
        diff_text.animator.play()
        self.diff_text = diff_text
        self.diff_text_gen_time = Time.now()
        self.should_delete_difficulty_text = True

    def delete_difficulty_text(self):
        if Time.now() - self.diff_text_gen_time > 1.0 and self.should_delete_difficulty_text:
            self.should_delete_difficulty_text = False
            self.diff_text.destroy_me()

    def generate_random_obstacle(self):
        self.last_generation_time = 1000 * Time.now()

        number_of_obstacles = int(min(self.game_difficuty, len(self.obstacle_generators)))
        random_ind = rand(0, number_of_obstacles-1)
        random_obstacle_generator = self.obstacle_generators[random_ind]
        if type(random_obstacle_generator) == RectTranslateXObstacleController:
            self.last_generation_time -= 300

        if self.game_difficuty == self.max_difficult:
            self.rect_x_controller.generate_obstacle()
        random_obstacle_generator.generate_obstacle()

    def delete_object_with_specific_type(self, obstacle_type):
        for i in range(len(self.obstacle_generators)):
            if type(self.obstacle_generators[i]) == obstacle_type:
                self.obstacle_generators.pop(i)
                break
