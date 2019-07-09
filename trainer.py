import os
import matplotlib.pyplot as plt
from dqn_agent import DQNAgent


class Trainer:
    __one_rectangle_state_size = 8
    __max_num_rec = 3
    __action_size = len(["turn_right", "turn_left", "nothing"])
    # __action_size = len(["turn_right", "turn_left"])
    __state_size = 1 + __one_rectangle_state_size * __max_num_rec
    # __state_size = 3
    __agent = None
    __died = False
    __batch_size = 32
    __cumulative_reward = 0.0
    __episodes = 0
    __num_episodes = 300
    __return_history = []
    __Time_history = []

    @classmethod
    def set_one_rectangle_state_size(cls, size):
        cls.__one_rectangle_state_size = size

    @classmethod
    def set_max_num_rec(cls, num):
        cls.__max_num_rec = num

    @classmethod
    def get_action_size(cls):
        return cls.__action_size

    @classmethod
    def get_state_size(cls):
        return cls.__state_size

    @classmethod
    def get_agent(cls):
        return cls.__agent

    @classmethod
    def set_agent(cls, agent):
        cls.__agent = agent

    @classmethod
    def set_died(cls, died):
        cls.__died = died

    @classmethod
    def get_died(cls):
        return cls.__died

    @classmethod
    def get_batch_size(cls):
        return cls.__batch_size

    @classmethod
    def set_cumulative_reward(cls, cumulative_reward):
        cls.__cumulative_reward = cumulative_reward

    @classmethod
    def get_cumulative_reward(cls):
        return cls.__cumulative_reward

    @classmethod
    def get_episodes(cls):
        return cls.__episodes

    @classmethod
    def increase_episodes(cls):
        cls.__episodes += 1

    @classmethod
    def get_num_episodes(cls):
        return cls.__num_episodes

    @classmethod
    def get_return_history(cls):
        return cls.__return_history

    @classmethod
    def train_dqn(cls, play, num_episodes=500, render=True):

        cls.__num_episodes = num_episodes

        # Comment this line to enable training using your GPU
        os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

        state_size = cls.get_state_size()
        action_size = cls.get_action_size()

        agent = DQNAgent(
            state_size,
            action_size,
            gamma=0.95,
            epsilon=0.5,
            epsilon_min=0.01,
            epsilon_decay=0.992,
            learning_rate=0.4,
            learning_rate_decay=0.98,
        )

        cls.set_agent(agent)

        # checking if weights from previous learning session exists
        if os.path.exists('balance.h5'):
            print('Loading weights from previous learning session.')
            agent.load('balance.h5')
        else:
            print('No weights found from previous learning session.')

        cls.set_died(False)

        cls.__episodes = 1

        # Start playing the game:
        play()

        plt.pause(1.0)

    @classmethod
    def plot(cls):
        # Update the plot for training monitoring
        fig_format = 'png'
        return_history = cls.get_return_history()
        agent = cls.get_agent()

        plt.plot(return_history, 'b')
        plt.xlabel('Episode')
        plt.ylabel('Return')
        # plt.show(block=False)
        plt.pause(0.1)
        plt.savefig('dqn_training.' + fig_format, fig_format=fig_format)
        # Saving the model to disk
        agent.save('balance.h5')
