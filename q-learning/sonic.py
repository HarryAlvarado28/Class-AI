import retro
import gym
import numpy as np

env = retro.make('SonicTheHedgehog-Genesis', 'GreenHillZone.Act1')

env.reset()

done = False

while not done:
    env.render()
    action = [0,0,0,0,0,0,0,0,0,0,0,0]
    action = env.action_space.sample() 
    ob, rew, done, info = env.step(action)
    print("Action ", action, "Reward ", rew)
