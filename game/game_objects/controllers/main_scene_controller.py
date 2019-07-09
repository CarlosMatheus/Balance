from pygin import *
from game.game_objects.mesh_objects.screen_fader import ScreenFader
from game.game_objects.controllers.player_controller import PlayerController
from game.game_objects.controllers.score_controller import ScoreController
from game.game_objects.controllers.background_particles_controller import BackgroundParticlesController
from game.game_objects.controllers.obstacle_controller_wrapper import ObstacleControllerWrapper
from game.game_objects.controllers.items_controller_wrapper import ItemsControllerWrapper
from game.game_objects.controllers.pause_controller import PauseController
import numpy as np
from trainer import Trainer
import math


class MainSceneController(GameObject):

    def start(self):
        """
        setup initial scene variables
        """
        self.setup_initializer()
        self.setup_fader()
        self.current_score = 0.0

        # ---------------
        # Changed for IA:

        sys.setrecursionlimit(20000)

        self.fade_out_duration = 0
        Time.time_scale = 1.0

        self.trigger_died = False
        self.max_rectangles = 3
        self.agent = Trainer.get_agent()
        self.state_size = 1 + self.max_rectangles * len([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        self.initial_state = [0.0] + [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] * self.max_rectangles
        self.state = np.reshape(self.initial_state, [1, self.state_size])
        self.cumulative_reward = Trainer.get_cumulative_reward()
        self.died = False
        self.player_controller = None
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

        # if self.player_controller and hasattr(self.player_controller, 'angle') and not self.trigger_died:
        #     print(((self.player_controller.angle / math.pi) * 180) % 180)

        # ---------------
        # Changed for IA:
        self.ai()
        # ---------------

    def ai(self):
        """
        manage the ia
        :return:
        """
        agent = Trainer.get_agent()
        state_size = self.state_size
        state = self.state
        cumulative_reward = Trainer.get_cumulative_reward()

        # If the game really started (passed the initial animation)
        if self.player_controller and hasattr(self.player_controller, 'angle') and not self.trigger_died:

            # Get this frame action
            action = agent.act(state)

            # Get the state and reward of this frame
            next_state, reward, died = self.update_ai()

            # Reshape the state to pass on Keras:
            next_state = np.reshape(next_state, [1, state_size])

            # Make AI play actual action
            self.player_controller.set_IA_as_player(action)

            # Appending this experience to the experience replay buffer
            agent.append_experience(state, action, reward, next_state, died)
            # print(reward)

            # Update state for next frame
            self.state = next_state

            # Make cumulative reward
            cumulative_reward = agent.gamma * cumulative_reward + reward
            Trainer.set_cumulative_reward(cumulative_reward)
            # print(cumulative_reward)

            # Adjust score
            self.current_score = self.score_controller.score

            if died:
                self.trigger_died = True
                episodes = Trainer.get_episodes()
                NUM_EPISODES = Trainer.get_num_episodes()
                time = Time.now() - self.initial_time
                print("episode: {}/{}, time: {}, score: {:.6}, epsilon: {:.3}"
                      .format(episodes, NUM_EPISODES, time, cumulative_reward, agent.epsilon))

            batch_size = Trainer.get_batch_size()
            if len(agent.replay_buffer) > 2 * batch_size:
                loss = agent.replay(batch_size)


    def update_ai(self):
        """
        Will update and pass the information to AI
        :return:
        """
        max_rectangles = self.max_rectangles
        # If Player already can control:
        rectangles = GameObject.find_by_type("Rectangle")
        state = [(((self.player_controller.angle / math.pi) * 180) % 180)]
        rectangle_states = []
        empty_rectangle_state = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        for rect in rectangles:
            if rect.polygon_mesh is not None:
                # Get center:
                center = rect.transform.position

                # Get height, width
                point_list = rect.polygon_collider.get_point_list()
                point_a = point_list[0]
                point_b = point_list[1]
                point_d = point_list[-1]

                width = point_a.distance_to(point_d)
                height = point_a.distance_to(point_b)

                # Get ang
                angle = point_a.angle_to(point_d)

                if rect.physics is None: rect.physics = Physics(rect)

                linear_vel = rect.physics.get_inst_velocity()

                rectangle_state = [center[0], center[1], height, width, angle, linear_vel.x, linear_vel.y]
                rectangle_states.append(rectangle_state)

        del_list = []
        for idx in range(len(rectangle_states)): # del rect that are before 200
            if rectangle_states[idx][1] < 200:
                del_list.append(idx)

        for idx in del_list:
            if idx < len(rectangle_states):
                del rectangle_states[idx]

        del_list = []
        for idx in range(len(rectangle_states)):  # del rect that are after 640
            if rectangle_states[idx][1] > 640:
                del_list.append(idx)

        for idx in del_list:
            if idx < len(rectangle_states):
                del rectangle_states[idx]

        while len(rectangle_states) > max_rectangles:
            min_idx = 0
            min_val = 1000
            for i in range(len(rectangle_states)):
                if rectangle_states[i][1] < min_val:
                    min_val = rectangle_states[i][1]
                    min_idx = i
            del rectangle_states[min_idx]

        while len(rectangle_states) < max_rectangles:
            rectangle_states.append(empty_rectangle_state)

        for rectangle_state in rectangle_states:
            state += rectangle_state

        # print(state)
        # print(self.score_controller.score)
        return state, self.score_controller.score - self.current_score + 1, self.died


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
            # ---------------
            # Changed for IA:

            cumulative_reward = Trainer.get_cumulative_reward()
            return_history = Trainer.get_return_history()

            return_history.append(cumulative_reward)

            agent = Trainer.get_agent()
            episodes = Trainer.get_episodes()
            agent.update_epsilon()

            if episodes % 10 == 0:
                Trainer.plot()

            Trainer.increase_episodes()
            Scene.change_scene(0)
            # Engine.end_game()
            # ---------------

    def game_over(self):
        """
        Is called just once to enable change scene
        """
        if not self.should_change_scene:
            # ---------------
            # Changed for IA:
            self.died = True
            # ---------------
            self.should_fade_out = True
