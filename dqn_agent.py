import random
import numpy as np
from collections import deque
from keras import models, layers, optimizers, activations, losses


class DQNAgent:
    """
    Represents a Deep Q-Networks (DQN) agent.
    """
    def __init__(self, state_size, action_size, gamma=0.95, epsilon=0.5, epsilon_min=0.01, epsilon_decay=0.98, learning_rate=0.001, buffer_size=4098):
        """
        Creates a Deep Q-Networks (DQN) agent.

        :param state_size: number of dimensions of the feature vector of the state.
        :type state_size: int.
        :param action_size: number of actions.
        :type action_size: int.
        :param gamma: discount factor.
        :type gamma: float.
        :param epsilon: epsilon used in epsilon-greedy policy.
        :type epsilon: float.
        :param epsilon_min: minimum epsilon used in epsilon-greedy policy.
        :type epsilon_min: float.
        :param epsilon_decay: decay of epsilon per episode.
        :type epsilon_decay: float.
        :param learning_rate: learning rate of the action-value neural network.
        :type learning_rate: float.
        :param buffer_size: size of the experience replay buffer.
        :type buffer_size: int.
        """
        self.state_size = state_size
        self.action_size = action_size
        self.replay_buffer = deque(maxlen=buffer_size)  # giving a maximum length makes this buffer forget old memories
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay
        self.learning_rate = learning_rate
        self.model = self.make_model()

    def make_model(self):
        """
        Makes the action-value neural network model using Keras.
        :return: action-value neural network.
        :rtype: Keras' model.
        """

        model = models.Sequential()

        # 1 layer
        num_neurons = 24
        model.add(layers.Dense(
                units=num_neurons,
                activation=activations.relu,
                input_dim=self.state_size,
            ),
        )

        # 2 layer
        num_neurons = 24
        model.add(layers.Dense(
                units=num_neurons,
                activation=activations.relu,
            ),
        )

        # 3 layer
        num_neurons = self.action_size
        model.add(layers.Dense(
                units=num_neurons,
                activation=activations.linear
            ),
        )

        model.build(input_shape=(1, 2))
        model.summary()

        model.compile(
            loss=losses.mse,
            optimizer=optimizers.Adam(lr=self.learning_rate)
        )

        return model

    def act(self, state):
        """
        Chooses an action using an epsilon-greedy policy.

        :param state: current state.
        :type state: NumPy array with dimension (1, 2).
        :return: chosen action.
        :rtype: int.
        """

        try:
            actions = self.model.predict(state)[0]
        except Exception as e:
            print('Failed to upload to ftp: ' + str(e))

        if np.random.binomial(1, self.epsilon) == 1:
            action = np.random.choice([a for a in range(len(actions))])
        else:
            try:
                action = np.random.choice([action_ for action_, value_ in enumerate(actions) if value_ == np.max(actions)])
            except:
                print(1)

        return action

    def append_experience(self, state, action, reward, next_state, done):
        """
        Appends a new experience to the replay buffer (and forget an old one if the buffer is full).

        :param state: state.
        :type state: NumPy array with dimension (1, 2).
        :param action: action.
        :type action: int.
        :param reward: reward.
        :type reward: float.
        :param next_state: next state.
        :type next_state: NumPy array with dimension (1, 2).
        :param done: if the simulation is over after this experience.
        :type done: bool.
        """
        self.replay_buffer.append((state, action, reward, next_state, done))

    def replay(self, batch_size):
        """
        Learns from memorized experience.

        :param batch_size: size of the minibatch taken from the replay buffer.
        :type batch_size: int.
        :return: loss computed during the neural network training.
        :rtype: float.
        """
        minibatch = random.sample(self.replay_buffer, batch_size)
        states, targets = [], []
        for state, action, reward, next_state, done in minibatch:
            target = self.model.predict(state)
            if not done:
                target[0][action] = reward + self.gamma * np.max(self.model.predict(next_state)[0])
            else:
                target[0][action] = reward
            # Filtering out states and targets for training
            states.append(state[0])
            targets.append(target[0])
        history = self.model.fit(np.array(states), np.array(targets), epochs=1, verbose=0)
        # Keeping track of loss
        loss = history.history['loss'][0]
        return loss

    def load(self, name):
        """
        Loads the neural network's weights from disk.

        :param name: model's name.
        :type name: str.
        """
        self.model.load_weights(name)

    def save(self, name):
        """
        Saves the neural network's weights to disk.

        :param name: model's name.
        :type name: str.
        """
        self.model.save_weights(name)

    def update_epsilon(self):
        """
        Updates the epsilon used for epsilon-greedy action selection.
        """
        self.epsilon *= self.epsilon_decay
        if self.epsilon < self.epsilon_min:
            self.epsilon = self.epsilon_min
