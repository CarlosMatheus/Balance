import os
import matplotlib.pyplot as plt
from dqn_agent import DQNAgent


class Trainer:
    __one_rectangle_state_size = 6
    __max_num_rec = 5
    __action_size = len(["turn_right", "turn_left", "nothing"])
    __state_size = 1 + __one_rectangle_state_size * __max_num_rec
    __agent = None
    __died = False
    __batch_size = 32
    __cumulative_reward = 0.0

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
    def train_dqn(cls, play, num_episodes=300, render=True):
        fig_format = 'png'

        # Comment this line to enable training using your GPU
        os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

        state_size = cls.get_state_size()
        action_size = cls.get_action_size()

        # Creating the DQN agent
        agent = DQNAgent(state_size, action_size)
        cls.set_agent(agent)

        # checking if weights from previous learning session exists
        if os.path.exists('balance.h5'):
            print('Loading weights from previous learning session.')
            agent.load('balance.h5')
        else:
            print('No weights found from previous learning session.')

        died = cls.set_died(False)
        died = cls.get_died()
        batch_size = cls.get_batch_size()  # batch size used fro the experience replay
        return_history = []

        for episodes in range(1, num_episodes + 1):

            play()

            cumulative_reward = cls.get_cumulative_reward()

            return_history.append(cumulative_reward)

            agent = cls.get_agent()
            agent.update_epsilon()

            # Update the plot for training monitoring
            if episodes % 20 == 0:
                plt.plot(return_history, 'b')
                plt.xlabel('Episode')
                plt.ylabel('Return')
                plt.show(block=False)
                plt.pause(0.1)
                plt.savefig('dqn_training.' + fig_format, fig_format=fig_format)
                # Saving the model to disk
                agent.save('balance.h5')
        plt.pause(1.0)
