from pygin import *
from game.game_objects.mesh_objects.screen_fader import ScreenFader
from game.game_objects.controllers.player_controller import PlayerController
from game.game_objects.controllers.score_controller import ScoreController
from game.game_objects.controllers.background_particles_controller import BackgroundParticlesController
from game.game_objects.controllers.obstacle_controller_wrapper import ObstacleControllerWrapper
from game.game_objects.controllers.items_controller_wrapper import ItemsControllerWrapper
from game.game_objects.controllers.pause_controller import PauseController


class MainSceneController(GameObject):

    def start(self):
        """
        setup initial scene variables
        """
        self.setup_initializer()
        self.setup_fader()
        self.fade_out_duration = 1.2

        # ---------------
        # Changed for IA:
        # self.max_rectangles = 0
        # ---------------

    def setup_initializer(self):
        self.initial_time = Time.now()
        self.should_initialize = True

    def setup_fader(self):
        """
        Start fade in and set variables to fade out
        """
        ScreenFader(fade="in")
        self.should_change_scene = False
        self.should_fade_out = False
        self.change_scene_timer = 0.0

    def update(self):
        """
        call the initialize scene
        """
        if Input.press_space_down:
            Time.time_scale = (Time.time_scale + 1) % 2
            if Time.time_scale == 0.0:
                self.pause_controller = PauseController()
            else:
                self.pause_controller.destroy_all_text()
                self.pause_controller.destroy_me()

        self.initialize_scene()
        self.change_scene()

        # ---------------
        # Changed for IA:
        rectangles = GameObject.find_by_type("Rectangle")
        state = [self.player_controller.angle]
        for rect in rectangles:
            if rect.polygon_mesh is not None:
                # Get center:
                print(rect.transform.position)

                # Get h, l
                point_list = rect.polygon_collider.get_point_list()
                print([(point.x, point.y) for point in point_list])
                print(rect.dimen)
                print(rect.transform.rotation)

                # Get ang

                if rect.physics is not None:
                    print("" + str(rect.physics.get_inst_velocity()))

        # self.max_rectangles = max(len(rectangles), self.max_rectangles)
        # print(self.max_rectangles)
        # ---------------

    def update_ai(self):
        """
        Will update and pass the information to AI
        :return:
        """

    def initialize_scene(self):
        """
        When is the correct time, initialize scene
        This will happen just once
        """
        if Time.now() - self.initial_time > 0.45 and self.should_initialize:
            self.should_initialize = False
            # Changed for IA:
            # self.background_particle_controller = BackgroundParticlesController()
            self.player_controller = PlayerController()
            self.obstacle_controller_wrapper = ObstacleControllerWrapper()
            self.items_controller = ItemsControllerWrapper()
            self.score_controller = ScoreController()

    def change_scene(self):
        """
        Will fade screen out and the change it
        """
        if self.should_fade_out:
            ScreenFader(fade="out", fade_duration=self.fade_out_duration)
            self.should_fade_out = False
            self.should_change_scene = True
            self.change_scene_timer = Time.now()
            Time.time_scale = 0
        if self.should_change_scene and Time.now() - self.change_scene_timer > self.fade_out_duration+0.2:
            Time.time_scale = 1.0
            # Changed for IA:
            # Scene.change_scene(2)
            # Engine.end_game()

    def game_over(self):
        """
        Is called just once to enable change scene
        """
        if not self.should_change_scene:
            self.should_fade_out = True
