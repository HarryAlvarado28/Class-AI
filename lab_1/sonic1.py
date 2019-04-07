import retro
import pygame
from pygame.locals import *    # Nuevo en la version 0.03

pygame.init()

env = retro.make('SonicTheHedgehog-Genesis', 'GreenHillZone.Act1')

ancho = 800
alto = 600
pantalla = pygame.display.set_mode( (ancho, alto) )

pygame.key.set_repeat(1,50)
env.reset()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True
    env.render()
    # action = [0,0,0,0,0,0,0,1,0,0,0,1]
    action = [1,0,0,0,1,0,0,0,0,0,0,0]
    # action = env.action_space.sample()
    keys = pygame.key.get_pressed()          # Nuevo en 0.03
    if keys[K_LEFT]:                         # Nuevo en 0.03
        action = [0,0,0,0,0,0,1,0,0,0,0,0]
        print('¡Izquierda! ', action)
        # rectanguloNave.left -= 4             # Nuevo en 0.03
    if keys[K_RIGHT]:
        action = [0,0,0,0,0,0,0,1,0,0,0,0]
        print('Derecha! ', action)                      # Nuevo en 0.03
        # rectanguloNave.left += 4             # Nuevo en 0.03
    if keys[K_UP]:
        action = [0,0,0,0,0,0,0,0,1,0,0,0]
        print('Saltar! ', action)                      # Nuevo en 0.03
        # rectanguloNave.left += 4             # Nuevo en 0.03
    if keys[K_RIGHT] and keys[K_UP]:
        action = [0,0,0,0,0,0,0,1,1,0,0,0]
        print('Derecha & Saltar! ', action)

    print('action:: ',action)
    ob, rew, done, info = env.step(action)
    pygame.display.flip()
    #print(key_action)
    # print(info)
    # print("Action ", action, "Reward ", rew)
