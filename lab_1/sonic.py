import retro

env = retro.make('SonicTheHedgehog-Genesis', 'GreenHillZone.Act1')

env.reset()

done = False

while not done:
    env.render()

    #action = [0,0,0,0,0,0,0,1,0,0,0,1]
    action = env.action_space.sample()
    ob, rew, done, info = env.step(action)
    #print(key_action)
    # print(info)
    # print("Action ", action, "Reward ", rew)
