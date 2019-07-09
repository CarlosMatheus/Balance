import os

for i in range(10000):
    print("Replay " + str(i))
    os.system("python train_dqn.py")
