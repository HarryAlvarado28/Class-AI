import retro
import pygame
from pygame.locals import *    # Nuevo en la version 0.03

pygame.init()

env = retro.make('SonicTheHedgehog-Genesis', 'GreenHillZone.Act1')

ancho = 1
alto = 1
pantalla = pygame.display.set_mode( (ancho, alto) )

pygame.key.set_repeat(1,200)
env.reset()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True
    env.render()

    action = [0,0,0,0,0,0,0,0,0,0,0,0]

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        action = [0,0,0,0,0,0,1,0,0,0,0,0]

    if keys[K_RIGHT]:
        action = [0,0,0,0,0,0,0,1,0,0,0,0]

    if keys[K_UP]:
        action = [0,0,0,0,0,0,0,0,1,0,0,0]

    if keys[K_RIGHT] and keys[K_UP]:
        action = [0,0,0,0,0,0,0,1,1,0,0,0]

    if keys[K_LEFT] and keys[K_UP]:
        action = [0,0,0,0,0,0,0,1,1,0,0,0]

    ob, rew, done, info = env.step(action)
    pygame.display.flip()

    print("Action ", action, "Reward ", rew)
