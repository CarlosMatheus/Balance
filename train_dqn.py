from balance import play
from trainer import Trainer
from game.scripts.constants import Constants

if __name__ == '__main__':
    Constants.is_training_ai = True
    Constants.evaluating_ai = False
    Trainer.train_dqn(
        play,
        num_episodes=300,
        epsilon=0.5,
        epsilon_decay=0.98,
        learning_rate=0.001,
        learning_rate_decay=0.99,
    )

