#!/usr/bin/env python3

# pip3 install git+https://github.com/openai/gym.git@c36450671090e52243f44fbd20314dd07df6263c
# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/.mujoco/mujoco210/bin

import gym
print("gym:", gym.__version__)

# https://github.com/DLR-RM/rl-baselines3-zoo#mujoco-environments
# https://github.com/openai/gym/wiki/Leaderboard#mujoco

# https://github.com/openai/gym/tree/master/gym/envs/mujoco
# env = gym.make("InvertedPendulum-v2")
env = gym.make("Hopper-v3")

env.reset() #seed=37) # https://github.com/openai/gym/pull/2422 but doesnt seed aaaahhhh
# env.seed(37)

for _ in range(999):
	env.render()
	env.step(env.action_space.sample())
env.close()

# https://github.com/nplan/gym-line-follower/blob/master/gym_line_follower/envs/line_follower_env.py
