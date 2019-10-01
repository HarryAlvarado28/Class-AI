import retro
import pygame
import numpy as np
from pygame.locals import *
import cv2
import imutils



video_size = 800,800
env = retro.make(game='SonicTheHedgehog-Genesis', state='GreenHillZone.Act2')

def key_action(world_observation):
    #["B", "A", "MODE", "START", "UP", "DOWN", "LEFT", "RIGHT", "C", "Y", "X", "Z"]
    keys = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    world = np.asarray(world_observation).reshape(-1)
    key=pygame.key.get_pressed()
    if key[K_LEFT]:
        keys[6] = 1
    if key[K_UP]:
        keys[0] = 1
    if key[K_RIGHT]:
        keys[7] = 1
    if key[K_DOWN]:
        keys[5] = 1
    eval = np.concatenate((world, np.array(keys)))
    print(eval)
    return keys

screen = pygame.display.set_mode(video_size)
observation = env.reset()
while True:
    img = env.render(mode='rgb_array')
    # ROTATE THE IMAGE THE MATRIX IS 90 grates and mirror
    img2 = np.flipud(np.rot90(img))
    img2 = imutils.resize(img2, width=800)
    image_np = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray image', image_np)
    cv2.waitKey(1)
    screen = pygame.display.set_mode(video_size)
    surf = pygame.surfarray.make_surface(img2)
    screen.blit(surf, (0, 0))
    pygame.display.update()
    action = key_action(image_np)
    observation, reward, done, info = env.step(action)
    if done:
        break