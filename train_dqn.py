import os
import numpy as np
import matplotlib.pyplot as plt
from dqn_agent import DQNAgent
from utils import reward_engineering_mountain_car
import pylab
from balance import play


NUM_EPISODES = 300
RENDER = False
fig_format = 'png'

# Comment this line to enable training using your GPU
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'


one_rectangle_state_size = 6
max_num_rec = 5

state_size = 1 + one_rectangle_state_size * max_num_rec
action_size = len(["turn_right", "turn_left", "nothing"])

# Creating the DQN agent
agent = DQNAgent(state_size, action_size)

# checking if weights from previous learning session exists
if os.path.exists('balance.h5'):
    print('Loading weights from previous learning session.')
    agent.load('balance.h5')
else:
    print('No weights found from previous learning session.')

done = False
batch_size = 32 # batch size used fro the experience replay
return_history = []

for episodes in range(1, NUM_EPISODES + 1):
    # initial angle position is 0.0
    initial_player_state = 0.0
    # [(is rectangle present?)=0, ]
    initial_rectangle_state = []
    initial_state =
    state = []
    state = np.reshape(state, )



