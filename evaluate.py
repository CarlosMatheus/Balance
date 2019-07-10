from balance import play
from trainer import Trainer
from game.scripts.constants import Constants

if __name__ == '__main__':
    Constants.is_training_ai = False
    Constants.evaluating_ai = True
    Trainer.train_dqn(
        play,
        num_episodes=30,
        epsilon=0.0,
        epsilon_decay=0.0,
        learning_rate=0.000,
        learning_rate_decay=0.0,
    )

