import retro
import numpy as np

env = retro.make('SonicTheHedgehog-Genesis', 'GreenHillZone.Act1')
env.reset()
done = False

while not done:
    env.render()
    action = [1,1,0,0,0,0,0,0,0,0,0,0];
    ob, rew, done, info = env.step(action)

    print("Action ", action, "Reward ", rew, " Ob ", np.shape(ob))
