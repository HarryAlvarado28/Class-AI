import retro
import time

env = retro.make('SonicTheHedgehog-Genesis', 'GreenHillZone.Act1')

env.reset()

done = False



while not done:
    env.render()
    action = mt()
    ob, rew, done, info = env.step(action)
    if info['screen_x_end'] < (info['screen_x'] + 3):
        env.reset()
        pass
    print("Action ", action, "Reward ", rew)

def mt():
    # q0 - Corre al Frente
    action = [0,0,0,0,0,0,0,1,0,0,0,0]
    if round(time.time()) % 2 == 0:
        #q1 - Corre Al Frente y Salta
        action = [1,0,0,0,0,0,0,1,0,0,0,0]
    if round(time.time()) % 9 == 0:
        #q2 - Corre atrás y Salta
        action = [1,0,0,0,0,0,1,0,0,0,0,0]
    return action

"""
action = [0,0,0,0,0,0,0,0,0,0,0,0]
[
    1-Saltar_X,
    2-Saltar_Z,
    3-Tab,
    4-Enter,
    5-Mira_Arriba,
    6-Agacharse,
    7-Caminar_Atras,
    8-Caminar_AlFrente,
    9-Saltar_C,
    10-S,
    11-A,
    12-D
]
"""
